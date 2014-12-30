from abc import abstractmethod

from ...smart_handlers.base import base_handler


class BaseCommandParser(base_handler.BaseHandler):
    @abstractmethod
    def command_update(self, command, data):
        '''
        Called when CommandDispatcher class recieves a command
        '''
        pass

    def timeline_update(self, data):
        super(BaseCommandParser, self).timeline_update(self, data)
