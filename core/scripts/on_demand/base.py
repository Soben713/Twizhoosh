from abc import abstractmethod

from core.scripts.timeline import base


class BaseOnDemandScript(base.BaseTimelineScript):
    @abstractmethod
    def command_update(self, command, data):
        """
        Called when OnDemandScriptsManager class receives a command
        """
        pass

    def timeline_update(self, data):
        super(BaseOnDemandScript, self).timeline_update(self, data)
