from abc import ABCMeta, abstractmethod
import re

from core.st_memory_singleton import STMemory
from core.twitter_singleton import TwitterSingleton
from core.utils import farsi_tools
from core.utils.logging import log


class BaseTwitterRelatedScript(object, metaclass=ABCMeta):
    # List of events the script gets called for
    listen_to = None

    def __init__(self):
        self.twitter = TwitterSingleton()
        self.st_memory = STMemory()

    @abstractmethod
    def update(self, data, data_type):
        """
        Called when someone @Twizhoosh follows, tweets something
        """
        pass


class BaseTimelineScript(BaseTwitterRelatedScript):
    listen_to = 'timeline_update'

    @abstractmethod
    def timeline_update(self, data):
        pass

    def update(self, data, data_type):
        data['text'] = farsi_tools.normalize(data['text'])
        log("Timeline update:" + data['text'])
        self.timeline_update(data)


class BaseOnSelfStatusUpdate(BaseTwitterRelatedScript):
    listen_to = 'self_status_update'

    @abstractmethod
    def self_status_update(self, status):
        pass

    def update(self, data, data_type):
        self.self_status_update(data)


class BaseDirectMessageScript(BaseTwitterRelatedScript):
    listen_to = 'direct_message'

    @abstractmethod
    def received_direct_message(self, data):
        pass

    def update(self, data, data_type):
        self.received_direct_message(data)