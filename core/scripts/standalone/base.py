from abc import ABCMeta, abstractmethod


class BaseStandaloneScript(metaclass=ABCMeta):
    @abstractmethod
    def on_called(self):
        pass