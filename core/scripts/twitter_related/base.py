from abc import ABCMeta, abstractmethod
import re

from core.st_memory_singleton import STMemory
from core.twitter_singleton import TwitterSingleton
from core.utils import farsi_tools
from core.utils.logging import log


class BaseTwitterRelatedScript(object, metaclass=ABCMeta):
    """
    All BaseTwitterRelatedScript sub classes should have at list one listen_to event.
    For every 'foo_event' in listen_to event there should be an on_foo_event function
    """
    listen_to = None

    def __init__(self):
        self.twitter = TwitterSingleton()
        self.st_memory = STMemory()


class BaseTimelineScript(BaseTwitterRelatedScript):
    listen_to = 'timeline_update'

    @abstractmethod
    def on_timeline_update(self, data):
        pass


class BaseOnSelfStatusUpdate(BaseTwitterRelatedScript):
    listen_to = 'self_status_update'

    @abstractmethod
    def on_self_status_update(self, status):
        pass


class BaseDirectMessageScript(BaseTwitterRelatedScript):
    listen_to = 'direct_message'

    @abstractmethod
    def on_direct_message(self, data):
        pass
