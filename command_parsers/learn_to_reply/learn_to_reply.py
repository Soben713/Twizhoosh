from core.command_parsers.base import base_command_parser
from core.utils import debug
import re

class LearnToReply(base_command_parser.BaseCommandParser):
	command_pattern = 'اگ(ر|ه) کسی گفت (?P<x>.*) بگو (?P<y>.*)'

	def command_update(self, command, data):
		match = re.search(self.command_pattern, command)
		if match:
			x = match.group('x')
			y = match.group('y')

			if len(x) < 5:
				self.reply_to(data, 'نمی‌تونم کلمه‌های کوچیکتر از ۵ حرف رو یاد بگیرم. :|')
				return

			self.short_term_memory.setdefault('learned_replies', {}).setdefault(x, []).append({
				'text': y,
				'teaching_tweet': data,
			})

			reply_message = 'چشم اگر کسی گفت {0} می‌گم {1}.'.format(x, y)
			self.reply_to(data, reply_message)
