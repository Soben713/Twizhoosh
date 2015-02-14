from core.utils.logging import log
from core.utils.singleton import Singleton


class STMemory(metaclass=Singleton):
    memory = {}

    def mark_person(self, key, username):
        log('Mark {0} for {1}'.format(username, key))
        mark = self.memory.setdefault('mark', {})
        mark[key].setdefault(username, 0)
        mark[key][username] += 1

    def is_person_marked(self, key, username, max_mark_num=1):
        """
        Returns False if person is marked less than @max_mark_num otherwise True.
        """
        return self.memory.setdefault('mark', {}).setdefault(key, {}).setdefault(username, 0) >= max_mark_num