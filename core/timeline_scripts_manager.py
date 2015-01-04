from core.on_demand_scripts_manager import OnDemandScriptsManager
from core.script_loader import load_scripts

from core.utils.logging import debug
from core.utils import farsi_tools
from core.settings import INSTALLED_TIMELINE_SCRIPTS


class TimelineScriptsManager:
    """
    A timeline update dispatcher between Smart Handlers
    """

    def __init__(self, *args, **kwargs):
        script_classes = load_scripts('scripts.timeline', INSTALLED_TIMELINE_SCRIPTS)
        script_classes.insert(0, OnDemandScriptsManager)
        self.scripts = [script() for script in script_classes]

    def on_timeline_update(self, data):
        data['text'] = farsi_tools.normalize(data['text'])
        for script in self.scripts:
            script.timeline_update(data)
