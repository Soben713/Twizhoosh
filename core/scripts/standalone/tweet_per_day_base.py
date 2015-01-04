from abc import abstractmethod
from random import randint
from core import settings
from core.scripts.standalone.base import BaseStandaloneScript
from core.twitter_singleton import TwitterSingleton
from core.utils.logging import debug


class TweetPerDayBase(BaseStandaloneScript):
    expected_tweet_per_day = 10

    def __init__(self):
        self.twitter = TwitterSingleton()

    @abstractmethod
    def update(self):
        """
        Called by on_called, approximately @expected_tweet_per_day times each day
        """
        pass

    def on_called(self):
        SECONDS_PER_DAY = 24 * 60 * 60
        num_of_calls = SECONDS_PER_DAY / settings.STAND_ALONE_REPEAT_TIME

        if randint(0, num_of_calls) < self.expected_tweet_per_day:
            self.update()
        pass