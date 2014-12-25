#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
from twython import *
from smart_handlers_manager import SmartHandlersManager
from utils import log, debug

CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
OAUTH_TOKEN = os.environ['TWITTER_OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = os.environ['TWITTER_OAUTH_TOKEN_SECRET']
DEBUG = os.environ['DEBUG']
TWEET_LENGTH = 140
TWEET_URL_LENGTH = 21

class MyStreamer(TwythonStreamer):
	def __init__(self, *args, **kwargs):
		super(MyStreamer, self).__init__(*args, **kwargs)
		self.twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
		self.smart_handlers_manager = SmartHandlersManager(self.twitter)

	def on_success(self, data):
		self.smart_handlers_manager.on_timeline_update(data)

	def on_error(self, status_code, data):
		log(status_code)
		log(data)

def main():
	while True:
		log("starting")
		try:
			stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, 
				OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
			stream.user(replies="all")
		except TwythonRateLimitError as e:
			log("Rate limit error, retrying after {0} seconds".format(e.retry_after))
			time.sleep(e.retry_after)

if __name__ == '__main__':
	main()
