from time import sleep
from twython.exceptions import TwythonError
from core.script_loader import load_scripts
from core.settings import STAND_ALONE_REPEAT_TIME, INSTALLED_STANDALONE_SCRIPTS
from core.utils.logging import log


def run():
    log("Standalone run")
    script_classes = load_scripts('scripts.standalone', INSTALLED_STANDALONE_SCRIPTS)
    scripts = [script() for script in script_classes]

    while True:
        sleep(STAND_ALONE_REPEAT_TIME)

        try:
            for script in scripts:
                script.on_called()
        except TwythonError as e:
            log("Twython error: {0}".format(e))
            pass