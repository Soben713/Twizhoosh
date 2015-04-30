import re

from .spelling_corrections import spelling_corrections
from core.scripts.twitter_related import reply_by_keyword_base


class SpellChecker(reply_by_keyword_base.BaseReplyByKeywordScript):
    def __init__(self, *args, **kwargs):
        super(SpellChecker, self).__init__(*args, **kwargs)
        # Add spelling corrections to @replies
        self.replies = []

        for wrong in spelling_corrections.keys():
            self.replies.append({
                'keywords': [wrong],
                'reply_messages': ['{0}*'.format(spelling_corrections[wrong])]
            })

    # Do not correct, when the twit is an spelling correction
    def reply(self, data, keyword, reply):
        # assumes there is only one correct form and therefore reply_messages has only one item
        # also, needs a [:-1] to remove the *
        right_word = reply['reply_messages'][0][:-1]
        if not re.findall(right_word, data['text']):
            super(SpellChecker, self).reply(data, keyword, reply)
