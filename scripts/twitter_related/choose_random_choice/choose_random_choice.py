import random
import re

from core.scripts.twitter_related import on_demand, base
from core.twitter_related_scripts_runner import EventDispatcherSingleton
from core.utils.farsi_tools import add_dummy_spaces
import settings


class ChooseRandomChoice(on_demand.BaseOnDirectMessageOrTimelineDemandScript):
    def received_command(self, command, data, reply_function, *args, **kwargs):
        has_p_regex = r'\(([^)]*)\)'
        choices_list = re.findall(has_p_regex, command)
        if not choices_list:
            return

        answer = ""
        for choices_str in choices_list:
            choices = re.split(r'[\\|/|\|]', choices_str)
            if len(choices) <= 1:
                continue
            answer += random.choice(choices) + " "

        if answer == "":
            return

        reply_function(add_dummy_spaces(answer, 10))
        EventDispatcherSingleton().terminate_scripts()