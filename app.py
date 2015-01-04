import threading
from core.utils.logging import debug

import standalone_runner
import timeline_related_runner


class TimelineRelated(threading.Thread):
    def run(self):
        timeline_related_runner.run()


class Standalone(threading.Thread):
    def run(self):
        standalone_runner.run()


if __name__ == '__main__':
    t = TimelineRelated()
    s = Standalone()
    s.start()
    t.start()
