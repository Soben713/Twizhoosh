from core.utils.logging import log
from core.utils.singleton import Singleton


class STMemory(metaclass=Singleton):
    memory = {}

    def mark_person(self, key, tweet_data):
        log('Mark {0} for {1}'.format(tweet_data['user']['screen_name'], key))
        username = tweet_data['user']['id_str']
        mark = self.memory.setdefault('mark', {})
        mark[key].setdefault(username, 0)
        mark[key][username] += 1

    def is_person_marked(self, key, tweet_data, max_mark_num=1):
        """
        Returns False if person is marked less than @max_mark_num otherwise True.
        """
        username = tweet_data['user']['id_str']
        return self.memory.setdefault('mark', {}).setdefault(key, {}).setdefault(username, 0) >= max_mark_num