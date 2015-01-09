from time import sleep
import time

from twython.exceptions import TwythonError, TwythonRateLimitError

from core.script_loader import load_scripts
from settings import INSTALLED_STANDALONE_SCRIPTS, STAND_ALONE_REPEAT_TIME_CHUNKS
from core.utils.logging import log


def run():
    log("Standalone run")
    script_classes = load_scripts('scripts.standalone', INSTALLED_STANDALONE_SCRIPTS)
    scripts = [script() for script in script_classes]
    remaining_chunks = {}
    for script in scripts:
        remaining_chunks[script.__class__.__name__] = script.repeat_time

    while True:
        sleep(STAND_ALONE_REPEAT_TIME_CHUNKS)
        try:
            for script in scripts:
                remaining_chunks[script.__class__.__name__] -= 1
                if remaining_chunks[script.__class__.__name__] == 0:
                    remaining_chunks[script.__class__.__name__] = script.repeat_time
                    script.on_called()

        except TwythonRateLimitError as e:
            log("Rate limit error, asks to retry after {0}".format(e.retry_after))
            time.sleep(min(int(e.retry_after), 5*60*60))
        except TwythonError as e:
            log("Twython error: {0}".format(e))