import random
import re

from core.scripts.twitter_related import on_demand
from core.twitter_related_scripts_runner import EventDispatcherSingleton
from core.utils.farsi_tools import add_dummy_spaces


class ChooseRandomChoice(on_demand.BaseOnTimelineDemandScript):
    def received_command(self, command, data):
        has_p_regex = r'\((?P<choices>.*)\)'
        p = re.search(has_p_regex, command)
        if not p:
            return

        choices_str = p.group('choices')
        choices = re.split(r'[\\|/|\|]', choices_str)

        if len(choices) <= 1:
            return

        choice = add_dummy_spaces(random.choice(choices), 10)

        self.twitter.reply_to(data, choice)
        EventDispatcherSingleton().terminate_scripts()