from abc import ABCMeta, abstractmethod

from core.twitter_singleton import TwitterSingleton


class BaseStandaloneScript(metaclass=ABCMeta):
    # Repeats every repeat_time * settings.STAND_ALONE_REPEAT_TIME_CHUNKS seconds
    repeat_time = 1

    def __init__(self):
        self.twitter = TwitterSingleton()

    @abstractmethod
    def on_called(self):
        pass