from twython.api import Twython
from twython.exceptions import TwythonError

import settings
from core.utils.logging import log
from core.utils.singleton import Singleton


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


class TwitterSingleton(metaclass=Singleton):
    twitter = None

    def __init__(self):
        if settings.DEBUG:
            self.twitter = TwitterDebugLogger()
        else:
            self.twitter = Twython(
                settings.CONSUMER_KEY,
                settings.CONSUMER_SECRET,
                settings.OAUTH_TOKEN,
                settings.OAUTH_TOKEN_SECRET
            )

    def status_update_hooks(self):
        pass

    def tweet(self, status, *args, **kwargs):
        try:
            self.twitter.update_status(status=status, *args, **kwargs)
            self.status_update_hooks()
        except TwythonError as e:
            log("Twython error, tweeting: {0}".format(e))

    def reply_to(self, tweet_data, status, *args, **kwargs):
        status = '@{0} {1}'.format(tweet_data['user']['screen_name'], status)
        self.tweet(status=status, in_reply_to_status_id=tweet_data['id_str'], *args, **kwargs)

    def update_status_with_media(self, *args, **kwargs):
        try:
            self.twitter.update_status_with_media(*args, **kwargs)
            self.status_update_hooks()
        except TwythonError as e:
            log("Twython error, updating status with media: {0}".format(e))

    def send_direct_message(self, text, user_id=None, screen_name=None):
        if user_id:
            self.twitter.send_direct_message(text=text, user_id=user_id)
        elif screen_name:
            self.twitter.send_direct_message(text=text, screen_name=screen_name)