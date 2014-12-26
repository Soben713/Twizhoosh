from .spelling_corrections import spelling_corrections
from ..base import smart_reply_by_keyword

class SpellChecker(smart_reply_by_keyword.SmartReplyByKeyword):

	def __init__(self, *args, **kwargs):
		super(SpellChecker, self).__init__(*args, **kwargs)
		# Add spelling corrections to @replies
		self.replies = []
		
		for wrong in spelling_corrections.keys():
			self.replies.append({
				'keywords': [wrong],
				'reply_messages': [u'{0}*'.format(spelling_corrections[wrong])]
			})

	def timeline_update(self, data):
		super().timeline_update(data)