import random
import re

from core.scripts.twitter_related import on_demand
from core.twitter_related_scripts_runner import EventDispatcherSingleton
from core.utils.farsi_tools import add_dummy_spaces


class ChooseRandomChoice(on_demand.BaseOnDirectMessageOrTimelineDemandScript):
    synonyms = {
        'آره': ['اوهوم', 'بله'],
        'نه': ['خیر', 'نچ']
    }

    REPLACE_WITH_SYNONYM_POSSIBILITY = 0.5

    def received_command(self, command, data, reply_function, sender, *args, **kwargs):
        has_p_regex = r'\(([^)]*)\)'
        choices_list = re.findall(has_p_regex, command)
        if not choices_list:
            return

        answer = ""
        for choices_str in choices_list:
            choices = re.split(r'[\\|/|\|]', choices_str)
            if len(choices) <= 1:
                continue
            choice = random.choice(choices)
            if choice in self.synonyms and random.random() <= self.REPLACE_WITH_SYNONYM_POSSIBILITY:
                choice = random.choice(self.synonyms[choice])
            answer += choice + " "

        if answer == "":
            return

        reply_function(add_dummy_spaces(answer, 10))
        EventDispatcherSingleton().terminate_scripts()