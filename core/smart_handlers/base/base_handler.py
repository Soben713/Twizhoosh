from abc import ABCMeta,abstractmethod
from twython.exceptions import TwythonError
from core.utils.logging import log

class JustRepliedException(Exception):
	def __init__(self, tweet, *args, **kwargs):
		self.tweet = tweet
		super(JustRepliedException, self).__init__(*args, **kwargs)

class BaseHandler(object,metaclass=ABCMeta):
	def __init__(self, twitter, short_term_memory):
		self.twitter = twitter
		self.short_term_memory = short_term_memory

	@abstractmethod
	def timeline_update(self, data):
		'''
		Called when someone @Twizhoosh follows, tweets something
		'''
		pass

	def tweet(self, *args, **kwargs):
		try:
			self.twitter.update_status(*args, **kwargs)
			status = kwargs.get('status', '-> No status specified')
			raise JustRepliedException(tweet=status)
		except TwythonError as e:
			log("Twithon error: {0}".format(e))
		# To ensure at most one handler replies, we throw an exception

	def reply_to(self, tweet_data, status, *args, **kwargs):
		status = '@{0} {1}'.format(tweet_data['user']['screen_name'], status)
		self.tweet(status=status, in_reply_to_status_id=tweet_data['id_str'], *args, **kwargs)
