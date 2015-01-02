import importlib

from core.st_memory_manager import STMemoryManager
from core.scripts.timeline.base.base_handler import JustRepliedException
from core.utils.logging import debug
from core.utils import farsi_tools
from core.settings import INSTALLED_TIMELINE_SCRIPTS


def load_handlers():
    scripts = []
    for script in INSTALLED_TIMELINE_SCRIPTS:
        (package_name, dot, class_name) = script.rpartition('.')
        module = importlib.import_module(package_name)
        scripts.append(getattr(module, class_name))
    return scripts


class TimelineScriptsManager:
    """
    A timeline update dispatcher between Smart Handlers
    """

    def __init__(self, twitter, *args, **kwargs):
        st_memory_manager = STMemoryManager()
        script_classes = load_handlers()
        self.scripts = [script(twitter, st_memory_manager) for script in script_classes]

    def on_timeline_update(self, data):
        try:
            data['text'] = farsi_tools.normalize(data['text'])
            for script in self.scripts:
                script.timeline_update(data)
        except JustRepliedException as e:
            debug(u'Just replied with:\n {0}'.format(e.tweet))
