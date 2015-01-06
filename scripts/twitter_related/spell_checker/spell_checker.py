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
                'reply_messages': [u'{0}*'.format(spelling_corrections[wrong])]
            })
