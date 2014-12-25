#!/usr/bin/python
# -*- coding: utf-8 -*-

from .base_handler import BaseHandler
from twython import *
import re, random
from utils import debug, log
from abc import ABCMeta,abstractmethod

class SmartReplyByKeyword(BaseHandler,metaclass=ABCMeta):
	'''
	@replies contains a list of keywords and reply messages, If a tweet
	in timeline contains one of the keywords, @Twizhoosh replies with
	something random from its reply_messages
	'''

	replies = []
	
	@abstractmethod
	def timeline_update(self, data):
		if 'text' in data:
			text = data['text']
			for i in range(len(self.replies)):
				reply = self.replies[i]
				for keyword in reply['keywords']:
					if re.findall(keyword, text):
						log('matched')
						try:
							self.reply_to(data, random.choice(reply['reply_messages']))
						except TwythonError as e:
							print(e)
