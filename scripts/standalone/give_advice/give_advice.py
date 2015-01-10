from core.scripts.standalone.tweet_per_day_base import TweetPerDayBase
from core.utils.logging import log

import urllib.request
import json


print(obj)

class GiveAdvice(TweetPerDayBase):
    expected_tweet_per_day = 1
    def update(self):
        url = 'http://api.adviceslip.com/advice' # TODO: get json from http://api.adviceslip.com/advice/{i} 0<i<188, for non-repetitive results
        obj = json.loads(urllib.request.urlopen(url).readall().decode('utf-8'))
        log('Loaded json object for random advice')
        slip = obj['slip']
        self.twitter.tweet(status=slip['advice'])
