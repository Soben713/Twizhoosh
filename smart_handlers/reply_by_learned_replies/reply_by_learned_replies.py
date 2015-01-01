#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

from core.smart_handlers.base.base_handler import BaseHandler
from core.utils.logging import debug


class ReplyByLearnedReplies(BaseHandler):
    def timeline_update(self, data):
        learned_replies = list(
            self.st_memory_manager.memory.get('learned_replies', {}).items())
        debug("Learned replies: {0}".format(learned_replies))
        random.shuffle(learned_replies)

        for k, v in learned_replies:
            if data['text'].find(k) > -1:
                reply_item = random.choice(v)
                reply_message = None
                teacher = reply_item['teaching_tweet']['user']['screen_name']
                if teacher == data['user']['screen_name']:
                    reply_message = reply_item['text']
                else:
                    reply_message = "@{0} {1}".format(
                        teacher, reply_item['text'])
                self.reply_to(data, reply_message)
                return
