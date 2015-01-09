import threading

from core import standalone_runner, twitter_related_scripts_runner


class TwitterRelatedScripts(threading.Thread):
    def run(self):
        twitter_related_scripts_runner.run()


class StandaloneScripts(threading.Thread):
    def run(self):
        standalone_runner.run()


if __name__ == '__main__':
    t = TwitterRelatedScripts()
    s = StandaloneScripts()
    t.start()
    s.start()
