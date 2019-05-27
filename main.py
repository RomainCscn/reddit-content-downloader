import os
import sys
from pathlib import Path
import praw
import json
import youtube_dl
import urllib.request

config = json.load(open('config.json', 'r'))
reddit = praw.Reddit(client_id=config['clientId'],
                     client_secret=config['clientSecret'],
                     user_agent=config['userAgent'])

def create_download_folder():
  p = Path(f'./download')
  if not p.exists():
    os.makedirs(f'./download')

def replace_reserved_characters(title):
  characters = (('<', ''), ('>', ''), (':', ''), ('r/', ''), ('\\', ''), ('|', ''), ('*', ''), ('?', ''), ('%', ''))
  new_title = title
  for r in characters:
    new_title = new_title.replace(*r)
  return new_title

def shorten_title(title):
  if len(title) > 200:
    return title[:200]
  return title

def main(limit=10):
  create_download_folder()

  subreddits = json.load(open('subreddits.json', 'r'))

  for subreddit in subreddits:
    sub = reddit.subreddit(subreddit)
    for submission in sub.top(limit=limit):
      title = replace_reserved_characters(submission.title)
      title = shorten_title(title)

      ydl_opts = {
        'download_archive': 'downloaded.txt', 
        'outtmpl': f'./download/{sub.display_name}/{title}.%(ext)s',
      }
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
          ydl.download([submission.url])
        except youtube_dl.utils.DownloadError as download_error:
          if 'No media found' in str(download_error):
            pass
          else:
            print('=== Downloading image ===')
            p = Path(f'./download/{sub.display_name}')
            if not p.exists():
              os.makedirs(f'./download/{sub.display_name}')
            
            url = submission.url
            if 'i.imgur' not in url and 'imgur' in url:
              url = url.replace('imgur', 'i.imgur')
              url += '.jpg'
            
            file_extension = url.split('.')[-1]
            urllib.request.urlretrieve(url, f'./download/{sub.display_name}/{title}.{file_extension}')

if len(sys.argv) > 1:
  try:
    main(int(sys.argv[1]))
  except ValueError:
    print('Please enter an integer as limit')
else:
  main()