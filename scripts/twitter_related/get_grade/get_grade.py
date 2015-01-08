import random
import re

from core.scripts.twitter_related import on_demand
from core.utils.logging import log


class GetGrade(on_demand.BaseOnTimelineDemandScript):
    command_pattern = r'.*چند می( |‌)?ش(و)?م.*'

    def received_command(self, command, data):
        match = re.search(self.command_pattern, command)

        if match:
            log("{0} asked for grade".format(data['user']['screen_name']))
            self.twitter.reply_to(data, "{0:.1f}".format(min(random.random() * 30, 20)))