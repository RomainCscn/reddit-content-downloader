import os
import sys
import traceback
import argparse
import praw
import prawcore
import json
import youtube_dl
import urllib.request
from pathlib import Path
from PIL import Image
from PyQt5.QtCore import QThread, pyqtSignal, QSettings
from PyQt5.QtWidgets import QMessageBox

TITLE_MAX_LENGHT = 200

class MyLogger(object):
  def debug(self, msg):
    print(msg)

  def warning(self, msg):
    pass

  def error(self, msg):
    pass

def create_download_folder():
  p = Path(f'./download')
  if not p.exists():
    os.makedirs(f'./download')

def replace_reserved_characters(title):
  characters = (('<', ''), ('>', ''), (':', ''), ('r/', ''), ('/', ''), ('\\', ''), ('|', ''), ('*', ''), ('?', ''), ('%', ''))
  new_title = title
  for r in characters:
    new_title = new_title.replace(*r)
  return new_title

def shorten_title(title):
  if len(title) > TITLE_MAX_LENGHT:
    return title[:TITLE_MAX_LENGHT]
  return title

def is_image_similar(image1, image2):
    return open(image1,"rb").read() == open(image2,"rb").read()

def is_image(image):
  try:
    Image.open(image)
  except IOError:
    return False
  return True

def remove_unexisting_images():
  for directory in os.scandir('./download'): 
    if 'DS_Store' not in directory.path:
      for image in os.scandir(directory.path):
        if is_image(image.path) and is_image_similar('./empty_image', image.path):
          os.remove(image.path)
          print(f'=== Removed {image.path} as it was no longer available ===')

class DownloadThread(QThread):
  content_downloaded = pyqtSignal(int)
  sub_not_found = pyqtSignal(str)
  config_error = pyqtSignal()
  download_completed = pyqtSignal()

  def __init__(self, subreddits, limit, top):
    self.subreddits = subreddits
    self.limit = limit
    self.top = top
    settings = QSettings('Romain Cascino', 'Reddit Content Downloader')
    self.reddit = praw.Reddit(client_id = settings.value('client_id', type=str),
                     client_secret = settings.value('client_secret', type=str),
                     user_agent = settings.value('user_agent', type=str))
    QThread.__init__(self)

  def __del__(self):
      self.wait()

  def run(self):
    self.download_content(self.subreddits, self.limit, self.top)

  def done(self):
    print('done')

  def download_content(self, subreddits, limit, time):
    create_download_folder()
    download_index = 0
    for subreddit in subreddits:
      sub = self.reddit.subreddit(subreddit)
      try:
        for submission in sub.top(time, limit=limit):
          title = replace_reserved_characters(submission.title)
          title = shorten_title(title)

          ydl_opts = {
            'download_archive': 'downloaded.txt', 
            'outtmpl': f'./download/{sub.display_name}/{title}.%(ext)s',
            'logger': MyLogger(),
          }
          with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
              ydl.download([submission.url])
              download_index += 1
              self.content_downloaded.emit(download_index)
            except youtube_dl.utils.DownloadError as download_error:
              if 'No media found' in str(download_error):
                pass
              else:
                print('Downloading image')
                p = Path(f'./download/{sub.display_name}')
                if not p.exists():
                  os.makedirs(f'./download/{sub.display_name}')
                
                url = submission.url
                if 'i.imgur' not in url and 'imgur' in url:
                  url = url.replace('imgur', 'i.imgur')
                  url += '.jpg'
                
                file_extension = url.split('.')[-1]
                urllib.request.urlretrieve(url, f'./download/{sub.display_name}/{title}.{file_extension}')
                download_index += 1
                self.content_downloaded.emit(download_index)
      except prawcore.exceptions.Redirect:
        download_index = 0
        self.sub_not_found.emit(subreddit)
        print(f'=== Skipping r/{sub} as it does not exist ===')
      except prawcore.exceptions.ResponseException:
        download_index = 0
        self.config_error.emit()
        print(f'=== Oops, an error as occured. Please check your configuration values. ===')
        return
      except:
        download_index = 0
        print(f'=== Oops, an unexpected error as occured... ===')
        return
    self.download_completed.emit()
