import re

from core.command_parsers.base import base_command_parser
from core.utils.logging import log
from core.smart_handlers.base.base_handler import JustRepliedException


class LearnToReply(base_command_parser.BaseCommandParser):
    command_pattern = 'اگ(ر|ه) کسی( بهت)? گفت (?P<x>.*) بگو (?P<y>.*)'

    def command_update(self, command, data):
        match = re.search(self.command_pattern, command)
        if match:
            x = match.group('x')
            y = match.group('y')

            if len(x) < 5:
                self.reply_to(
                    data, 'نمی‌تونم کلمه‌های کوچیکتر از ۵ حرف رو یاد بگیرم. :|')
                return

            self.st_memory_manager.memory.setdefault('learned_replies', {}).setdefault(x, []).append({
                'text': y,
                'teaching_tweet': data,
            })

            log("learned_replies size: {0}".format(
                len(self.st_memory_manager.memory['learned_replies'])))
            reply_message = 'اوکی اگر کسی گفت {0} می‌گم {1}.'.format(x, y)
            self.twitter.send_direct_message(
                text=reply_message, user=data['user']['id_str'])

            # TODO: throw suitable exception
            raise JustRepliedException(tweet=reply_message)
