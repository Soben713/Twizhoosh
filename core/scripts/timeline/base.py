from abc import ABCMeta, abstractmethod

from core.st_memory_singleton import STMemory
from core.twitter_singleton import TwitterSingleton


class BaseTimelineScript(object, metaclass=ABCMeta):
    def __init__(self):
        self.twitter = TwitterSingleton()
        self.st_memory = STMemory()

    @abstractmethod
    def timeline_update(self, data):
        """
        Called when someone @Twizhoosh follows, tweets something
        """
        pass