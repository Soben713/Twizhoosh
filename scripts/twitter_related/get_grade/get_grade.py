import random
import re

from core.scripts.twitter_related import on_demand
from core.twitter_related_scripts_runner import EventDispatcherSingleton
from core.utils.logging import log
from core.utils.regex import combine_regexes


class GetGrade(on_demand.BaseOnDirectMessageOrTimelineDemandScript):
    command_pattern = combine_regexes([
        r'.*چند می( |‌)?ش((و)?م|(ه|(و)?د)).*',
        r'.*what grade will i get.*'
    ])

    def received_command(self, command, data, reply_message, *args, **kwargs):
        if re.search(self.command_pattern, command, re.IGNORECASE):
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
            log("rand: %s" % rand)

            _x = 0.0
            grade = 0

            for i in range(len(probs)):
                _x += probs[i][0]
                if rand <= _x:
                    grade = random.random() * (probs[i][2] - probs[i][1]) + probs[i][1]
                    break

            log("Guessed grade: %s" % grade)

            reply_message("{0:.1f}/20".format(grade))
            EventDispatcherSingleton().terminate_scripts()