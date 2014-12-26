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

	def is_a_tweet(self, data):
		'''
		This is a dirty way to do it, I know. But what else can I do?
		'''
		if 'text' in data and 'user' in data and 'id_str' in data:
			return True
		return False

	def on_success(self, data):
		if self.is_a_tweet(data):
			log("Timeline update: %s [%s]" % (data[u'user'][u'screen_name'], data[u'id_str']))
			self.smart_handlers_manager.on_timeline_update(data)
		else:
			log("Got non status message: \n %s \n" % data)

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
