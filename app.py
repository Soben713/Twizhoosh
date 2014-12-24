import os
import time
from twython import *
from smart_handlers_list import handler_classes

CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
OAUTH_TOKEN = os.environ['TWITTER_OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = os.environ['TWITTER_OAUTH_TOKEN_SECRET']
TWEET_LENGTH = 140
TWEET_URL_LENGTH = 21


class MyStreamer(TwythonStreamer):
	def __init__(self, *args, **kwargs):
		super(MyStreamer, self).__init__(*args, **kwargs)
		self.twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

		self.smart_handlers = []
		for handler in handler_classes:
			self.smart_handlers.append(handler(twitter = self.twitter))

	def on_success(self, data):
		for smart_handler in self.smart_handlers:
			smart_handler.timeline_update(data)

	def on_error(self, status_code, data):
		print status_code, data


def main():
	while True:
		print "Starting"
		try:
			stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, 
				OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
			stream.user(replies="all")
		except TwythonRateLimitError as e:
			print "Rate limit error, retrying after %s seconds" % e.retry_after
			time.sleep(e.retry_after)


if __name__ == '__main__':
	main()
