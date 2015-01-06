import re
from core.exceptions import DontReplyAnymore
from core.scripts.twitter_related import base
from core.utils.logging import log


class LearnToReply(base.BaseOnDemandedScript):
    command_pattern = r'اگ(ر|ه) کسی( بهت)? گفت (?P<x>.*) بگو (?P<y>.*)'

    def received_command(self, command, data):
        match = re.search(self.command_pattern, command)
        if match:
            x = match.group('x')
            y = match.group('y')

            if len(x) < 5:
                self.twitter.reply_to(
                    data, 'نمی‌تونم کلمه‌های کوچیکتر از ۵ حرف رو یاد بگیرم. :|')
                return

            self.st_memory.memory.setdefault('learned_replies', {}).setdefault(x, []).append({
                'text': y,
                'teaching_tweet': data,
            })

            log("learned_replies size: {0}".format(
                len(self.st_memory.memory['learned_replies'])))
            reply_message = 'اوکی اگر کسی گفت {0} می‌گم {1}.'.format(x, y)
            self.twitter.send_direct_message(
                text=reply_message, user=data['user']['id_str'])
