#!/usr/bin/python
# -*- coding: utf-8 -*-

from ..base import smart_reply_by_keyword

class SayHi(smart_reply_by_keyword.SmartReplyByKeyword):
	replies = [{
		'keywords': [u'تیزهوش', u'تویزهوش', u'tizho*u*sh', u'(?<!@)tw*izho*u*sh'],
		'reply_messages': [u'سلام', u'با من کار داشتی؟ :دی', u'جانم؟']
	}]

	def timeline_update(self, data):
		super().timeline_update(data)