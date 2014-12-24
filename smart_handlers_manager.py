from smart_handlers_list import handler_classes
from smart_handlers.base.base_handler import JustRepliedException
from utils import debug


class SmartHandlersManager:
	'''
	A timeline update dispatcher between Smart Handlers
	'''
	def __init__(self, twitter, *args, **kwargs):
		self.smart_handlers = []
		for handler in handler_classes:
			self.smart_handlers.append(handler(twitter = twitter))

	def on_timeline_update(self, data):
		try:
			for smart_handler in self.smart_handlers:
				smart_handler.timeline_update(data)
		except JustRepliedException as e:
			debug(u'Just replied with:\n %s' % e.tweet)
