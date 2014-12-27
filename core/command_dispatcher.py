#!/usr/bin/python
# -*- coding: utf-8 -*-
from core.smart_handlers.base import base_handler
from core.settings import INSTALLED_COMMAND_PARSERS
import inspect, importlib
import re
import sys, pkgutil


def load_command_parser_classes():
	parsers=[]
	for parser in INSTALLED_COMMAND_PARSERS:
		(package_name,dot,class_name) = parser.rpartition('.')
		module=importlib.import_module(package_name)
		parsers.append(getattr(module,class_name))
	return parsers


class CommandDispatcher(base_handler.BaseHandler):
	is_mentioned_regex = r'.*(tw*izho*u*sh|[ت|ط]ی[ظ|ز|ذ|ض][ه|ح]و*ش)\S* (?P<command>.*)'

	def timeline_update(self, data):
		match = re.search(self.is_mentioned_regex, data['text'], re.IGNORECASE)
		if match:
			command = match.group('command')
			parser_classes = load_command_parser_classes()
			parsers = []

			for parser_class in parser_classes:
				parsers.append(parser_class(self.twitter, self.short_term_memory))

			for parser in parsers:
				parser.command_update(command, data)
