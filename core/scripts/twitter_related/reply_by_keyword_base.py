#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import random
from abc import ABCMeta

from twython import *

from core.scripts.twitter_related.base import BaseTimelineScript
from core.twitter_related_scripts_runner import EventDispatcherSingleton
from core.utils.logging import log


class BaseReplyByKeywordScript(BaseTimelineScript):
    """
    @replies contains a list of keywords and reply messages, If a tweet
    in twitter_related contains one of the keywords, @Twizhoosh replies with
    something random from its reply_messages
    """

    replies = []

    # If True, responds only once until short memory is cleaned
    answer_once = False

    def on_timeline_update(self, data):
        marked = self.st_memory.is_person_marked(self.__class__.__name__, data)

        if not self.answer_once or not marked:
            for i in range(len(self.replies)):
                reply = self.replies[i]
                for keyword in reply['keywords']:
                    if re.findall(keyword, data['text']):
                        log('matched')
                        try:
                            if self.answer_once:
                                self.st_memory.mark_person(self.__class__.__name__, data)
                            self.twitter.reply_to(data, random.choice(reply['reply_messages']))

                            EventDispatcherSingleton().terminate_scripts()

                        except TwythonError as e:
                            print(e)
