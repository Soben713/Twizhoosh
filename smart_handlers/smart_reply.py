#!/usr/bin/python
# -*- coding: utf-8 -*-

from base_handler import BaseHandler
from twython import *
import re
import random

class SmartReply(BaseHandler):
	'''
	If a tweet in timeline contains one of the keywords, @Twizhoosh
	replies with something random from reply_messages
	'''

	replies = [
		{
			'keywords': [u'تیزهوش', u'تویزهوش', u'tizho*u*sh', u'(?<!@)tw*izho*u*sh'],
			'reply_messages': [u'سلام', u'با من کار داشتی؟ :دی', u'جانم؟']
		}
	]

	def timeline_update(self, data):
		if 'text' in data:
			text = data['text']
			for reply in self.replies:
				for keyword in reply['keywords']:
					if re.findall(keyword, text):
						try:
							status = '@%s %s' % (data['user']['screen_name'], random.choice(reply['reply_messages']))
							self.twitter.update_status(status=status, in_reply_to_status_id=data['id'])
						except TwythonError as e:
							print e
