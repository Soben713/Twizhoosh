from smart_handlers.base.base_handler import JustRepliedException
from utils import debug
import os.path
import sys, pkgutil
import inspect, importlib
from settings import HANDLERS_PACKAGE,INSTALLED_HANDLERS

def load_handlers(root_package):
	handlers=[]
	for handler in INSTALLED_HANDLERS:
		(package_name,dot,class_name) = handler.rpartition('.')
		module=importlib.import_module(root_package+dot+package_name)
		handlers.append(getattr(module,class_name))
	return handlers

class SmartHandlersManager:
	'''
	A timeline update dispatcher between Smart Handlers
	'''
	def __init__(self, twitter, *args, **kwargs):
		handler_classes = load_handlers(HANDLERS_PACKAGE)
		self.smart_handlers = [handler(twitter) for handler in handler_classes]

	def on_timeline_update(self, data):
		try:
			for smart_handler in self.smart_handlers:
				smart_handler.timeline_update(data)
		except JustRepliedException as e:
			debug(u'Just replied with:\n {0}'.format(e.tweet))
