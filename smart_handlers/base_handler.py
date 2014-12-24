class BaseHandler:
	def __init__(self, twitter):
		self.twitter = twitter

	def timeline_update(self, data):
		'''
		Called when someone @Twizhoosh follows, tweets something
		'''
		pass