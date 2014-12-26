#!/usr/bin/python
# -*- coding: utf-8 -*-

from ..base import smart_reply_by_keyword

class SayHi(smart_reply_by_keyword.SmartReplyByKeyword):
	replies = [{
		'keywords': ['تیزهوش', 'تویزهوش', 'tizho*u*sh', '(?<!@)tw*izho*u*sh'],
		'reply_messages': [
			'سلام. :)', 
			'جانم؟ :)',
			':)', 
			':D',
			'می‌دونستی اگه بجای اسمم رو گفتن، منشنم کنی ریپلای نمی‌کنم؟ :)',
			'سلام خاله. :)',
		]
	}]

	def timeline_update(self, data):
		super().timeline_update(data)