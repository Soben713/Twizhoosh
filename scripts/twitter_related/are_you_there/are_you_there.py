import re

from core.scripts.twitter_related import on_demand
from core.twitter_related_scripts_runner import EventDispatcherSingleton
from core.utils.farsi_tools import add_dummy_spaces


class AreYouThere(on_demand.BaseOnDirectMessageOrTimelineDemandScript):
    persian_pattern = r'هستی؟'
    english_pattern = r'are you there?'

    def received_command(self, command, data, reply_message, sender, *args, **kwargs):
        reply = None

        if re.search(self.persian_pattern, command, re.IGNORECASE):
            reply = 'آره'
        elif re.search(self.english_pattern, command, re.IGNORECASE):
            reply = 'Yep'

        if reply is not None:
            reply_message(add_dummy_spaces(reply, 10))
            EventDispatcherSingleton().terminate_scripts()
