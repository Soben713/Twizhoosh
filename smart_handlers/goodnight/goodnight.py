#!/usr/bin/python
# -*- coding: utf-8 -*-

from ..base import smart_reply_by_keyword

class GoodNight(smart_reply_by_keyword.SmartReplyByKeyword):
	replies = [{
		'keywords': [u'شب بخیر', u'شب خوش', u'شبتون بخیر'],
		'reply_messages': [u'خوب بخوابی‫.‬ ‫:)‬', u'شب بخیر‫.‬', u'خواب‌های خوب ببینی‫.‬ ‫:)‬', u'خوب بخوابی‫...‬']
	}]
