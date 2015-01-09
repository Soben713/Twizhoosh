import re

from core.scripts.twitter_related import on_demand, base
from core.utils.logging import log
from core.twitter_related_scripts_runner import ParseStreamingData


class LearnToReply(on_demand.BaseOnDirectMessageDemandScript, on_demand.BaseOnTimelineDemandScript):
    MINIMUM_LENGTH = 7
    listen_to = [base.BaseTimelineScript.listen_to, base.BaseDirectMessageScript.listen_to]
    command_pattern = r'اگ(ر|ه) کسی( بهت)? گفت (?P<x>.*) بگو (?P<y>.*)'

    def received_command(self, command, data):
        data_type = ParseStreamingData.get_type_of_data(data)

        if data_type == base.BaseTimelineScript.listen_to:
            teacher_id = data['user']['id_str']
            teacher_screen_name = data['user']['screen_name']
        else:
            teacher_id = data['direct_message']['sender']['id_str']
            teacher_screen_name = data['direct_message']['sender']['screen_name']

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
                self.twitter.send_direct_message(text=error_msg, user=teacher_id)
                return

            self.st_memory.memory.setdefault('learned_replies', {}).setdefault(x, []).append({
                'text': y,
                'teacher_id': teacher_id,
                'teacher_screen_name': teacher_screen_name,
            })

            log("learned_replies size: {0}".format(
                len(self.st_memory.memory['learned_replies'])))
            reply_message = 'اوکی اگر کسی گفت {0} می‌گم {1}.'.format(x, y)
            self.twitter.send_direct_message(
                text=reply_message, user=teacher_id)
