#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

from core.scripts.twitter_related import base


class ReplyByLearnedReplies(base.BaseTimelineScript):
    MAX_REPLY_TIME = 3

    def on_timeline_update(self, data):
        learned_replies = list(self.st_memory.memory.get('learned_replies', {}).items())
        random.shuffle(learned_replies)

        for k, v in learned_replies:
            if data['text'].find(k) > -1 and len(v):
                reply_item = random.choice(v)
                teacher_screen_name = reply_item['teacher_screen_name']

                if teacher_screen_name == data['user']['screen_name']:
                    reply_message = reply_item['text']
                else:
                    reply_message = "@{0} {1}".format(teacher_screen_name, reply_item['text'])

                self.twitter.reply_to(data, reply_message)

                reply_item['times_used'] += 1
                if reply_item['times_used'] >= self.MAX_REPLY_TIME:
                    text = 'عبارت «{0}»، {1} بار استفاده شد و دیگر به آن پاسخی داده نمی‌شود.'.format(k, reply_item[
                        'times_used'])
                    self.twitter.send_direct_message(text=text, user_id=reply_item['teacher_id'])
                    self.st_memory.memory['learned_replies'][k].remove(reply_item)
