from abc import ABCMeta, abstractmethod
import re

from core.st_memory_singleton import STMemory
from core.twitter_singleton import TwitterSingleton
from core.utils import farsi_tools
from core.utils.logging import log


class BaseTwitterRelatedScript(object, metaclass=ABCMeta):
    # List of events the script gets called for
    listen_to = []

    def __init__(self):
        self.twitter = TwitterSingleton()
        self.st_memory = STMemory()

    @abstractmethod
    def update(self, data):
        """
        Called when someone @Twizhoosh follows, tweets something
        """
        pass


class BaseTimelineScript(BaseTwitterRelatedScript):
    listen_to = ['timeline_update']

    @abstractmethod
    def timeline_update(self, data):
        pass

    def update(self, data):
        data['text'] = farsi_tools.normalize(data['text'])
        log("Timeline update:" + data['text'])
        self.timeline_update(data)


class BaseOnSelfStatusUpdate(BaseTwitterRelatedScript):
    listen_to = ['self_status_update']

    @abstractmethod
    def self_status_update(self, status):
        pass

    def update(self, data):
        self.self_status_update(data)


class BaseOnDemandedScript(BaseTimelineScript):
    is_mentioned_regex = r'.*(tw*izho*u*sh|[ت|ط][ی|ي][ظ|ز|ذ|ض][ه|ح]و*ش)\S* (?P<command>.*)'

    @abstractmethod
    def received_command(self, command, data):
        pass

    def timeline_update(self, data):
        match = re.search(self.is_mentioned_regex, data['text'], re.IGNORECASE)
        if match:
            command = match.group('command')
            self.received_command(command, data)


class BaseDirectMessageScript(BaseTwitterRelatedScript):
    listen_to = ['direct_message']

    @abstractmethod
    def received_direct_message(self, data):
        pass

    def update(self, data):
        self.received_direct_message(data)