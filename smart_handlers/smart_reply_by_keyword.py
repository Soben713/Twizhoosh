#!/usr/bin/python
# -*- coding: utf-8 -*-

from base_handler import BaseHandler
from twython import *
import re
import random
from utils.spelling_corrections import spelling_corrections

class SmartReplyByKeyword(BaseHandler):
	'''
	@replies contains a list of keywords and reply messages, If a tweet
	in timeline contains one of the keywords, @Twizhoosh replies with
	something random from its reply_messages
	'''

	replies = []


	def __init__(self, *args, **kwargs):
		super(SmartReplyByKeyword, self).__init__(*args, **kwargs)

		# Add spelling corrections to @replies
		for wrong in spelling_corrections.keys():
			self.replies.append({
				'keywords': [wrong],
				'reply_messages': [u'%s*' % spelling_corrections[wrong]]
			})

		# Reply with something if mentions twizhoosh
		self.replies.append({
			'keywords': [u'تیزهوش', u'تویزهوش', u'tizho*u*sh', u'(?<!@)tw*izho*u*sh'],
			'reply_messages': [u'سلام', u'با من کار داشتی؟ :دی', u'جانم؟']
		})


	def timeline_update(self, data):
		if 'text' in data:
			text = data['text']
			for reply in self.replies:
				for keyword in reply['keywords']:
					if re.findall(keyword, text):
						print 'matched'
						try:
							self.reply_to(data, random.choice(reply['reply_messages']))
						except TwythonError as e:
							print e
