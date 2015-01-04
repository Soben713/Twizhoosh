import random
from core.scripts.standalone.tweet_per_day_base import TweetPerDayBase


class CallSherrgoo(TweetPerDayBase):
    expected_tweet_per_day = 2

    def update(self):
        account_name = "@SherrGoo"
        calls = [
            'شرگو :)',
            '{0} :)'.format(account_name),
            'شعرگو؟',
            account_name,
            'شرگو...',
        ]
        self.twitter.tweet(status=random.choice(calls))
