import random
from twython.api import Twython
from twython.exceptions import TwythonError

from core import settings
from core.utils.logging import log


class TwitterDebugLogger():
    """
    Prints any function call with parameters
    """

    def _anything(self, name):
        def _dummyfunction(*args, **kwargs):
            print(name, args, kwargs)

        return _dummyfunction

    def __getattr__(self, attr):
        return self._anything(attr)


class TwitterSingleton():
    _instance = None
    twitter = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TwitterSingleton, cls).__new__(cls, *args, **kwargs)
            if settings.DEBUG:
                cls.twitter = TwitterDebugLogger()
            else:
                cls.twitter = Twython(
                    settings.CONSUMER_KEY,
                    settings.CONSUMER_SECRET,
                    settings.OAUTH_TOKEN,
                    settings.OAUTH_TOKEN_SECRET
                )
        return cls._instance

    def tweet(self, status, *args, **kwargs):
        try:
            self.twitter.update_status(status=status, *args, **kwargs)
        except TwythonError as e:
            log("Twython error: {0}".format(e))
            # To ensure at most one handler replies, we throw an exception

    def reply_to(self, tweet_data, status, *args, **kwargs):
        status = '@{0} {1}'.format(tweet_data['user']['screen_name'], status)
        self.tweet(status=status, in_reply_to_status_id=tweet_data['id_str'], *args, **kwargs)