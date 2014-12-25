from smart_handlers.base.base_handler import JustRepliedException
from utils import debug
import pkgutil
import sys
import inspect
import smart_handlers
import importlib
import os.path

handlers_path = 'smart_handlers'

def load_all_plugins(dirname):
	loaded_plugins = []
	# these are the plugin packages
	for importer, package_name, _ in pkgutil.iter_modules([dirname]):
		full_package_name = '{0}.{1}'.format(dirname, package_name)
		plugins=importlib.import_module(full_package_name)
		# now search all the modules for classes
		for importer, plugin_name, _ in pkgutil.iter_modules([os.path.join(dirname,package_name)]):
			module_name = '{0}.{1}'.format(full_package_name, plugin_name)
			module=importlib.import_module(module_name)
			for name, obj in inspect.getmembers(module, lambda m: hasattr(m,'timeline_update')):
				if inspect.getmodule(obj) is module and not inspect.isabstract(obj):
					loaded_plugins.append(obj)
	return loaded_plugins

class SmartHandlersManager:
	'''
	A timeline update dispatcher between Smart Handlers
	'''
	def __init__(self, twitter, *args, **kwargs):
		self.smart_handlers = []
		handler_classes = load_all_plugins(handlers_path)
		for handler in handler_classes:
			self.smart_handlers.append(handler(twitter = twitter))

	def on_timeline_update(self, data):
		try:
			for smart_handler in self.smart_handlers:
				smart_handler.timeline_update(data)
		except JustRepliedException as e:
			debug(u'Just replied with:\n %s' % e.tweet)
