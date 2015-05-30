#!/usr/bin/python
# -*- coding: utf-8 -*-
from io import BytesIO
import random

import requests

from core.scripts.twitter_related import reply_by_keyword_base
from core.twitter_related_scripts_runner import EventDispatcherSingleton
from core.utils.google_image import get_random_google_image
from core.utils.logging import log


class GoodNight(reply_by_keyword_base.BaseReplyByKeywordScript):
    replies = [{
                   'keywords': [r'^(#)?شب(تون)?(\s|‌)*(بخیر|به خیر|به‌خیر|خوش)(.)?$'],
                   'reply_messages': []
               }]

    search_phrases = ['goodnight', 'goodnight quotes', 'goodnight quotes tumblr']
    max_answers = 2

    def reply(self, data, keyword, reply):
        img_url = get_random_google_image(random.choice(self.search_phrases))
        img = requests.get(url=img_url).content
        log('Sending image: %s' % img_url)
        self.twitter.update_status_with_media(
            status='@' + data['user']['screen_name'],
            media=BytesIO(img),
            in_reply_to_status_id=data['id_str']
        )
        EventDispatcherSingleton().terminate_scripts()
