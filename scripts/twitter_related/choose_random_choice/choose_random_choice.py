import random
import re

from core.scripts.twitter_related import on_demand, base
from core.twitter_related_scripts_runner import EventDispatcherSingleton
from core.utils.farsi_tools import add_dummy_spaces


class ChooseRandomChoice(on_demand.BaseOnDirectMessageOrTimelineDemandScript):
    def received_command(self, command, data, reply_function, *args, **kwargs):
        has_p_regex = r'\((?P<choices>.*)\)'
        p = re.search(has_p_regex, command)
        if not p:
            return

        choices_str = p.group('choices')
        choices = re.split(r'[\\|/|\|]', choices_str)

        if len(choices) <= 1:
            return

        choice = add_dummy_spaces(random.choice(choices), 10)

        reply_function(choice)
        EventDispatcherSingleton().terminate_scripts()