from time import sleep
from core.script_loader import load_scripts
from core.settings import STAND_ALONE_REPEAT_TIME, INSTALLED_STANDALONE_SCRIPTS
from core.utils.logging import log


def run():
    log("Standalone run")
    script_classes = load_scripts('scripts.standalone', INSTALLED_STANDALONE_SCRIPTS)
    scripts = [script() for script in script_classes]

    while True:
        sleep(STAND_ALONE_REPEAT_TIME)

        for script in scripts:
            script.on_called()