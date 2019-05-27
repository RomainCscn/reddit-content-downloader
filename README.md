# Reddit content downloader

A python program to download content (images and videos) of multiples subreddits.

## Prerequisites

- install [ffmpeg](https://ffmpeg.org)

Run `pip install -r requirements.txt` to install dependencies.

## Configuration

To make this works, you have to replace the values in `config.sample.json` with yours and save the file as `config.json`.

Check out [this guide](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps) to get your app's **client ID** and **secret**. 

Check out [this guide](https://github.com/reddit-archive/reddit/wiki/API#rules) to set up a correct **user agent**.

Finally, add your subreddits in the `subreddits.sample.json` file and save the file as `subreddits.json`.

## Run

Use `python main.py` to run the script and download subreddits content. This will create a `download/` folder and a folder for each subreddits.

You can specify a limit for each subreddit using the command `python main.py <LIMIT>` where `<LIMIT>` is an integer. 

This command `python main.py 3` will only download the first top 3 posts.