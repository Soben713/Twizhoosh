from abc import ABCMeta, abstractmethod
from core.twitter_singleton import TwitterSingleton


class BaseStandaloneScript(metaclass=ABCMeta):
    def __init__(self):
        self.twitter = TwitterSingleton()

    @abstractmethod
    def on_called(self):
        pass