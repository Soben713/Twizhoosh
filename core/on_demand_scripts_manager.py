#!/usr/bin/python
# -*- coding: utf-8 -*-
import importlib
import re

from core.scripts.timeline.base import base_handler
from core.settings import INSTALLED_ON_DEMAND_SCRIPTS


def load_command_parser_classes():
    scripts = []
    for script in INSTALLED_ON_DEMAND_SCRIPTS:
        (package_name, dot, class_name) = script.rpartition('.')
        module = importlib.import_module(package_name)
        scripts.append(getattr(module, class_name))
    return scripts


# TODO: Every dispatcher should return a

class OnDemandScriptsManager(base_handler.BaseHandler):
    is_mentioned_regex = r'.*(tw*izho*u*sh|[ت|ط][ی|ي][ظ|ز|ذ|ض][ه|ح]و*ش)\S* (?P<command>.*)'

    def __init__(self, *args, **kwargs):
        super(OnDemandScriptsManager, self).__init__(*args, **kwargs)

        script_classes = load_command_parser_classes()
        self.scripts = []

        for script_class in script_classes:
            self.scripts.append(script_class(self.twitter, self.st_memory_manager))

    def timeline_update(self, data):
        match = re.search(self.is_mentioned_regex, data['text'], re.IGNORECASE)
        if match:
            command = match.group('command')
            for script in self.scripts:
                script.command_update(command, data)
