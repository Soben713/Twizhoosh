#!/usr/bin/python
# -*- coding: utf-8 -*-

from core.smart_handlers.base.base_handler import BaseHandler
from core.utils import debug
import random

class ReplyByLearnedReplies(BaseHandler):
	def timeline_update(self, data):
		learned_replies = list(self.short_term_memory.get('learned_replies', {}).items())
		debug("Learned replies: {0}".format(learned_replies))
		random.shuffle(learned_replies)

		for k, v in learned_replies:
			if data['text'].find(k) > -1:
				reply_item = random.choice(v)
				reply_message = reply_item['text']
				self.reply_to(data, reply_message)
				return