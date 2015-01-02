#!/usr/bin/python
# -*- coding: utf-8 -*-

from core.scripts.timeline.smart_reply_by_keyword import smart_reply_by_keyword
from scripts.timeline.goodnight.goodnight_responses import goodnight_responses


class GoodNight(smart_reply_by_keyword.SmartReplyByKeyword):
    replies = [{
                   'keywords': [r'^(#)?شب(تون)?(\s|‌)*(بخیر|به خیر|به‌خیر|خوش)$'],
                   'reply_messages': goodnight_responses
               }]
    answer_once = True

    def timeline_update(self, data):
        super(GoodNight, self).timeline_update(data)