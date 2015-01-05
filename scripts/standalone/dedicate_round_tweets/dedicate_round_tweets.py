import random
import re

from core import settings
from core.scripts.standalone.base import BaseStandaloneScript
from core.utils.logging import log


def cons_numbers(x):
    if len(x) < 2:
        return False

    inc_or_dec = 1 if x[1] > x[0] else -1

    for i in range(len(x) - 1):
        if int(x[i + 1]) - int(x[i]) != inc_or_dec:
            return False
    return True


class DedicateRoundTweets(BaseStandaloneScript):
    repeat_time = 10

    regex_patterns = [
        r'^[0-9]+00$',  # Numbers that end with 00
        r'^([0-9])\1+$',  # Numbers that are all equal
    ]

    function_patterns = [
        cons_numbers,  # Consecutive numbers, like 2345 or 8765
    ]

    def get_tweets_count(self):
        if settings.DEBUG:
            return random.randint(0, 10000)
        log("Getting tweets")
        data = self.twitter.twitter.verify_credentials()
        return data['statuses_count']

    def is_round(self, num):
        if len(str(num)) < 3:
            return
        for regex in self.regex_patterns:
            if re.match(regex, str(num)):
                return True
        for f in self.function_patterns:
            if f(str(num)):
                return True
        return False

    def dedicate_to(self):
        if not settings.DEBUG:
            friends = self.twitter.twitter.get_friends_ids(screen_name=settings.TWIZHOOSH_USERNAME)
            id = random.choice(friends['ids'])
            dedicated_to = self.twitter.twitter.show_user(user_id=id)['screen_name']
        else:
            dedicated_to = 'tester'
        return dedicated_to

    def on_called(self):
        tweets = self.get_tweets_count()
        log("welp")
        log("Number of tweets: " + str(tweets))
        print(self.twitter.twitter.get_lastfunction_header('x-rate-limit-remaining'))

        if self.is_round(tweets + 1):
            log("Next tweet is round")
            status = 'توییت {0} تقدیم به {1}.'.format(str(tweets + 1), '@' + self.dedicate_to())
            self.twitter.tweet(status=status)
