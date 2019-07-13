import os
import sys
import argparse
import praw
import prawcore
import json
import youtube_dl
import urllib.request
from pathlib import Path
from PIL import Image

config = json.load(open('config.json', 'r'))
reddit = praw.Reddit(client_id=config['clientId'],
                     client_secret=config['clientSecret'],
                     user_agent=config['userAgent'])

TITLE_MAX_LENGHT = 200
TIME_FILTER = ['all', 'day', 'hour', 'month', 'week', 'year']
DEFAULT_LIMIT = 10
DEFAULT_TIME_FILTER = 'all'

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

def download_content(subreddits, limit, time):
  create_download_folder()

  for subreddit in subreddits:
    sub = reddit.subreddit(subreddit)
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
    except prawcore.exceptions.Redirect:
      print(f'=== Skipping r/{sub} as it does not exist ===')
    except:
      print(f'=== Oops, an unexpected error as occured... ===')

def get_arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument('subs', metavar='S', nargs='*', help='Subreddits, used instead of subreddits.json')
  parser.add_argument('-l','--limit', help='Limit of results', required=False)
  parser.add_argument('-t','--time', help='Time filter for top, can be one of: all, day, hour, month, week, year (default: all).', required=False)
  return vars(parser.parse_args())

def get_limit_arg(args):
  limit = DEFAULT_LIMIT
  if args['limit'] is not None:
    try:
      limit = int(args['limit'])
    except ValueError:
      raise
  return limit

def get_time_arg(args):
  time = DEFAULT_TIME_FILTER
  if args['time'] in TIME_FILTER:
    time = args['time']
  elif args['time'] is not None:
    raise ValueError('Please specify a correct time value. Can be one of: all, day, hour, month, week, year (default: all).')
  return time

def get_subs_arg(args):
  subreddits = json.load(open('subreddits.json', 'r'))
  if args['subs']:
    try:
      subreddits = args['subs']
    except ValueError:
      raise
  return subreddits

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

def main():
  args = get_arguments()
  limit = get_limit_arg(args)
  time = get_time_arg(args)
  subs = get_subs_arg(args)

  download_content(subs, limit, time)
  remove_unexisting_images()

main()