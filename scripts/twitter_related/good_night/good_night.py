#!/usr/bin/python
# -*- coding: utf-8 -*-

from core.scripts.twitter_related import reply_by_keyword_base
from scripts.twitter_related.good_night.good_night_responses import goodnight_responses


class GoodNight(reply_by_keyword_base.BaseReplyByKeywordScript):
    replies = [{
                   'keywords': [r'^(#)?شب(تون)?(\s|‌)*(بخیر|به خیر|به‌خیر|خوش)(.)?$'],
                   'reply_messages': goodnight_responses
               }]
    answer_once = True
