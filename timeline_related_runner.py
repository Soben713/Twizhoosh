#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

from twython import *
from twython.exceptions import TwythonError, TwythonRateLimitError

from core.timeline_scripts_manager import TimelineScriptsManager
from core.utils import sample_tweet
from core.utils.logging import log
from core import settings


class MyStreamer(TwythonStreamer):
    def __init__(self, *args, **kwargs):
        super(MyStreamer, self).__init__(
            settings.CONSUMER_KEY,
            settings.CONSUMER_SECRET,
            settings.OAUTH_TOKEN,
            settings.OAUTH_TOKEN_SECRET,
            *args, **kwargs
        )
        self.timeline_scripts_manager = TimelineScriptsManager()

    def is_a_tweet(self, data):
        '''
        This is a dirty way to do it, I know. But what else can I do?
        '''
        if 'text' in data and 'user' in data and 'id_str' in data and data['user'][
            'screen_name'] != settings.TWIZHOOSH_USERNAME:
            return True
        return False

    def on_success(self, data):
        if self.is_a_tweet(data):
            log("Timeline update: %s [%s]" % (
                data['user']['screen_name'], data['id_str']))
            self.timeline_scripts_manager.on_timeline_update(data)
        else:
            log("Got non status message: \n %s \n" % data)

    def on_error(self, status_code, data):
        log(status_code)
        log(data)

    def user(self, *args, **kwargs):
        while True:
            try:
                super(MyStreamer, self).user(self, *args, **kwargs)
            except TwythonRateLimitError as e:
                log("Rate limit error, asks to retry after {0}".format(e.retry_after))
                time.sleep(min(int(e.retry_after), 5))
            except TwythonError as e:
                log("Twython error {0}".format(e))


def run():
    if not settings.DEBUG:
        log("starting")
        stream = MyStreamer()
        stream.user(replies="all")
    else:
        log("Start debugging")
        timeline_scripts_manager = TimelineScriptsManager()

        while True:
            timeline_update = input(
                "Specify a sample timeline update message to see what @Twizhoosh does\n")
            tweet_data = sample_tweet.data
            tweet_data['text'] = timeline_update
            timeline_scripts_manager.on_timeline_update(tweet_data)