from abc import abstractmethod
import re

from core.scripts.twitter_related.base import BaseTwitterRelatedScript, BaseTimelineScript, BaseDirectMessageScript


class BaseOnDemandedScript(BaseTwitterRelatedScript):
    is_mentioned_regex = r'.*(tw*izho*u*sh|[ت|ط][ی|ي][ظ|ز|ذ|ض][ه|ح]و*ش)\S* (?P<command>.*)'

    @abstractmethod
    def received_command(self, command, data):
        pass

    def is_command(self, text):
        match = re.search(self.is_mentioned_regex, text, re.IGNORECASE)
        if match:
            command = match.group('command')
            return command
        return False


class BaseOnTimelineDemandScript(BaseOnDemandedScript, BaseTimelineScript):
    def timeline_update(self, data):
        command = self.is_command(data['text'])
        if command:
            self.received_command(command, data)


class BaseOnDirectMessageDemandScript(BaseOnDemandedScript, BaseDirectMessageScript):
    def received_direct_message(self, data):
        command = self.is_command(data['direct_message']['text'])
        if command:
            self.received_command(command, data)