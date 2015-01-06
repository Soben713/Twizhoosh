#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from core.scripts.twitter_related import base

from core.scripts.twitter_related.base import BaseTwitterRelatedScript
from core.utils.logging import debug


class ReplyByLearnedReplies(base.BaseTimelineScript):
    def on_timeline_update(self, data):
        learned_replies = list(
            self.st_memory.memory.get('learned_replies', {}).items())
        debug("Learned replies: {0}".format(learned_replies))
        random.shuffle(learned_replies)

        for k, v in learned_replies:
            if data['text'].find(k) > -1:
                reply_item = random.choice(v)
                teacher_screen_name = reply_item['teacher_screen_name']
                if teacher_screen_name == data['user']['screen_name']:
                    reply_message = reply_item['text']
                else:
                    reply_message = "@{0} {1}".format(
                        teacher_screen_name, reply_item['text'])
                self.twitter.reply_to(data, reply_message)
                return
