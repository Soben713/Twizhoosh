from abc import abstractmethod
import re

from core.scripts.twitter_related import base
from core.scripts.twitter_related.base import BaseTwitterRelatedScript, BaseTimelineScript, BaseDirectMessageScript


class BaseOnDemandedScript(BaseTwitterRelatedScript):
    is_mentioned_regex = r'.*(tw*izho*u*sh|[ت|ط][ی|ي][ظ|ز|ذ|ض][ه|ح]و*ش)\S* (?P<command>.*)'

    @abstractmethod
    def received_command(self, command, data, reply_function, *args, **kwargs):
        """
        :param command: The command text
        :param reply_function: A function that receives the reply message and replies. This may tweet, or send direct
        message or etc.
        """
        pass

    def is_mentioned_command(self, text):
        """
        :param text: A text to be checked
        :return: Extracts command from text or returns False
        """
        match = re.search(self.is_mentioned_regex, text, re.IGNORECASE | re.DOTALL)
        if match:
            command = match.group('command')
            return command
        return False


class BaseOnTimelineDemandScript(BaseTimelineScript, BaseOnDemandedScript):
    def received_timeline_command(self, command, data):
        reply_function = lambda x: self.twitter.reply_to(data, x)
        self.received_command(command, data, reply_function)

    def on_timeline_update(self, data):
        command = self.is_mentioned_command(data['text'])
        if command:
            self.received_timeline_command(command, data)


class BaseOnDirectMessageDemandScript(BaseDirectMessageScript, BaseOnDemandedScript):
    def received_direct_command(self, command, data):
        reply_function = lambda x: self.twitter.send_direct_message(text=x,
                                                                    user_id=data['direct_message']['sender']['id_str'])
        self.received_command(command, data, reply_function)

    def on_direct_message(self, data):
        """
        :return: First checks to see if it is a mentioned command, if not considers the whole string to be a command
                 you probably don't mention twizhoosh if you're sending a direct message
        """
        command = self.is_mentioned_command(data['direct_message']['text'])
        if command:
            self.received_direct_command(command, data)
        else:
            self.received_direct_command(data['direct_message']['text'], data)


class BaseOnDirectMessageOrTimelineDemandScript(BaseOnDirectMessageDemandScript, BaseOnTimelineDemandScript):
    listen_to = [base.BaseTimelineScript.listen_to, base.BaseDirectMessageScript.listen_to]