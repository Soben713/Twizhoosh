import urllib.request
import json

from core.scripts.standalone.tweet_per_day_base import TweetPerDayBase
from core.utils.logging import log


class GiveAdvice(TweetPerDayBase):
    expected_tweet_per_day = 2

    def update(self):
        # TODO: get json from http://api.adviceslip.com/advice/{i} 0<i<188, for non-repetitive results
        url = 'http://api.adviceslip.com/advice'
        obj = json.loads(urllib.request.urlopen(url).readall().decode('utf-8'))
        log('Loaded json object for random advice')
        slip = obj['slip']

        tags = "#advice #اندرز"
        status = "{0} {1}".format(slip['advice'], tags)
        self.twitter.tweet(status=status)
