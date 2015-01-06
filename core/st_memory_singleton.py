from core.utils.logging import log
from core.utils.singleton import Singleton


class STMemory(metaclass=Singleton):
    memory = {}

    def mark_person(self, key, tweet_data):
        log('Mark {0} for {1}'.format(tweet_data['user']['screen_name'], key))
        self.memory.setdefault(key, set([])).add(tweet_data['user']['id_str'])

    def is_person_marked(self, key, tweet_data):
        return tweet_data['user']['id_str'] in self.memory.setdefault(key, set([]))