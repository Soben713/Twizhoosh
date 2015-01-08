import random
import re

from core.scripts.twitter_related import on_demand
from core.utils.logging import log


class GetGrade(on_demand.BaseOnTimelineDemandScript):
    command_pattern = r'.*چند می( |‌)?ش((و)?م|(ه|(و)?د)).*'

    def received_command(self, command, data):
        if re.search(self.command_pattern, command):
            # Probability of the grade being between second and third items
            probs = [
                (0.1, 20, 20),
                (0.4, 15, 19.9),
                (0.25, 12, 14.9),
                (0.10, 10, 11.9),
                (0.13, 7, 9.9),
                (0.02, 0, 6.9)
            ]

            rand = random.random()
            _x = 0.0
            for i in range(len(probs)):
                _x += probs[i][0]
                if rand <= _x:
                    grade = random.random() * (probs[i][2] - probs[i][1]) + probs[i][1]
                    break

            self.twitter.reply_to(data, "{0:.1f}".format(grade))