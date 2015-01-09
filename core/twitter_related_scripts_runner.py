#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

from twython import *
from twython.exceptions import TwythonError, TwythonRateLimitError

from core.utils.sample_twitter_responses import sample_tweet, sample_direct_message
from core.utils.singleton import Singleton
from core.utils.logging import log
from core import script_loader
import settings


class ParseStreamingData():
    @staticmethod
    def get_type_of_data(data):
        keys = list(data.keys())

        if len(keys) == 1:
            # Many streaming api data like messages, friends etc have only one key
            return keys[0]

        if 'event' in data:
            # See list of events here:
            # https://dev.twitter.com/streaming/overview/messages-types#user_stream_messsages
            return data['event']

        if 'text' in data and 'favorite_count' in data:
            if data['user']['screen_name'] == settings.TWIZHOOSH_USERNAME:
                return 'self_status_update'
            return 'timeline_update'

        # Add any other types that I forgot (didn't care about)

        return None


class StreamingSingleton(TwythonStreamer, metaclass=Singleton):
    # dict of events to list of subscribing script instances
    scripts = {}

    def __init__(self, *args, **kwargs):
        super(StreamingSingleton, self).__init__(
            settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.OAUTH_TOKEN, settings.OAUTH_TOKEN_SECRET,
            *args, **kwargs
        )
        self.load_scripts()

    def load_scripts(self):
        """
        Loads scripts to self.scripts
        """
        script_classes = script_loader.load_scripts('scripts.twitter_related',
                                                    settings.INSTALLED_TWITTER_RELATED_SCRIPTS)
        log("Loading twitter related scripts")
        for script in script_classes:
            listen_to = script.listen_to if isinstance(script.listen_to, list) else [script.listen_to]
            for event in listen_to:
                self.scripts.setdefault(event, []).append(script())
                log("Loaded {0} for type {1}".format(script.__name__, event))

    def on_success(self, data):
        data_type = ParseStreamingData.get_type_of_data(data)

        if not data_type:
            log("Type of data unknown \n {0}".format(data))
            return

        log("Data received, with type: " + data_type)
        log("Data: {0}".format(data))
        for script in self.scripts.setdefault(data_type, []):
            log("Data type: {1} script found: {0}".format(script.__class__.__name__, data_type))
            try:
                getattr(script, 'on_' + data_type)(data)
            except TwythonError as e:
                log("Twython error when occured when running script {0}\nError is:{1}".format(
                    script.__class__.__name__, e))

    def on_error(self, status_code, data):
        log("Error streaming [{0}]: {1}".format(status_code, data))

    def user(self, *args, **kwargs):
        while True:
            try:
                super(StreamingSingleton, self).user(self, *args, **kwargs)
            except TwythonRateLimitError as e:
                log("Rate limit error, asks to retry after {0}".format(e.retry_after))
                time.sleep(min(int(e.retry_after), 5))
            except TwythonError as e:
                log("Twython error {0}".format(e))


class Testing(StreamingSingleton):
    def __init__(self, *args, **kwargs):
        self.load_scripts()

    def user(self, *args, **kwargs):
        while True:
            input_type = input("Enter a data type number or just tweet something \n 1. Direct Message \n 2. Custom data \n")

            if input_type == '1':
                message_text = input("Enter a direct message to @" + settings.TWIZHOOSH_USERNAME + "\n")
                data = sample_direct_message
                data['direct_message']['text'] = message_text
            elif input_type == '2':
                data = eval(input("Enter your data object \n"))
            else:
                timeline_text = input_type
                data = sample_tweet
                data['text'] = timeline_text

            self.on_success(data)


def run():
    if not settings.DEBUG:
        log("Starting streamer...")
        stream = StreamingSingleton()
        stream.user(replies="all")
    else:
        stream = Testing()
        stream.user(replies="all")