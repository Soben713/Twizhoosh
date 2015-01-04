#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

from core.script_loader import load_scripts
from core.scripts.timeline import base
from core.settings import INSTALLED_ON_DEMAND_SCRIPTS


# TODO: Every dispatcher should return a

class OnDemandScriptsManager(base.BaseTimelineScript):
    is_mentioned_regex = r'.*(tw*izho*u*sh|[ت|ط][ی|ي][ظ|ز|ذ|ض][ه|ح]و*ش)\S* (?P<command>.*)'

    def __init__(self, *args, **kwargs):
        super(OnDemandScriptsManager, self).__init__(*args, **kwargs)

        script_classes = load_scripts('scripts.on_demand', INSTALLED_ON_DEMAND_SCRIPTS)
        self.scripts = []

        for script_class in script_classes:
            self.scripts.append(script_class())

    def timeline_update(self, data):
        match = re.search(self.is_mentioned_regex, data['text'], re.IGNORECASE)
        if match:
            command = match.group('command')
            for script in self.scripts:
                script.command_update(command, data)
