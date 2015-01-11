import re

from core.scripts.twitter_related import on_demand, base
from core.utils.logging import log
from core.twitter_related_scripts_runner import DataParser


class LearnToReply(on_demand.BaseOnDirectMessageOrTimelineDemandScript):
    MINIMUM_LENGTH = 7
    listen_to = [base.BaseTimelineScript.listen_to, base.BaseDirectMessageScript.listen_to]
    command_pattern = r'(هر|اگ(ر|ه)) کسی( بهت)? گفت (?P<x>.*) بگو (?P<y>.*)'

    def received_direct_command(self, command, data):
        self.teacher_id = data['direct_message']['sender']['id_str']
        self.teacher_screen_name = data['direct_message']['sender']['screen_name']
        super(LearnToReply, self).received_direct_command(command, data)

    def received_timeline_command(self, command, data):
        self.teacher_id = data['user']['id_str']
        self.teacher_screen_name = data['user']['screen_name']
        super(LearnToReply, self).received_timeline_command(command, data)

    def received_command(self, command, data, reply_function, *args, **kwargs):
        match = re.search(self.command_pattern, command)
        if match:
            x = match.group('x')
            y = match.group('y')

            error_msg = None
            if len(x) < self.MINIMUM_LENGTH:
                error_msg = '{0} از {1} حرف کمتره'.format(x, self.MINIMUM_LENGTH)
            elif '@' in x:
                error_msg = 'به منشن‌ها جواب نمی‌دم. :)'

            if error_msg:
                self.twitter.send_direct_message(text=error_msg, user_id=self.teacher_id)
                return

            self.st_memory.memory.setdefault('learned_replies', {}).setdefault(x, []).append({
                'text': y,
                'teacher_id': self.teacher_id,
                'teacher_screen_name': self.teacher_screen_name,
                'times_used': 0,
            })

            log("learned_replies size: {0}".format(
                len(self.st_memory.memory['learned_replies'])))
            reply_message = 'اوکی اگر کسی گفت {0} می‌گم {1}.'.format(x, y)

            # reply_function is not used because we send a direct message regardless of message type
            self.twitter.send_direct_message(text=reply_message, user_id=self.teacher_id)
