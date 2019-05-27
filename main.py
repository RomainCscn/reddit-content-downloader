import os
import sys
import argparse
from pathlib import Path
import praw
import json
import youtube_dl
import urllib.request

config = json.load(open('config.json', 'r'))
reddit = praw.Reddit(client_id=config['clientId'],
                     client_secret=config['clientSecret'],
                     user_agent=config['userAgent'])

TITLE_MAX_LENGHT = 200
TIME_FILTER = ['all', 'day', 'hour', 'month', 'week', 'year']
DEFAULT_LIMIT = 10
DEFAULT_TIME_FILTER = 'all'

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
  if len(title) > TITLE_MAX_LENGHT:
    return title[:TITLE_MAX_LENGHT]
  return title

def download_content(limit, time):
  create_download_folder()

  subreddits = json.load(open('subreddits.json', 'r'))

  for subreddit in subreddits:
    sub = reddit.subreddit(subreddit)
    for submission in sub.top(time, limit=limit):
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

def get_arguments():
  parser = argparse.ArgumentParser()
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

def main():
  args = get_arguments()

  limit = get_limit_arg(args)
  time = get_time_arg(args)

  download_content(limit, time)

main()