import re
import wolframalpha

from core.scripts.twitter_related import on_demand
from core.twitter_related_scripts_runner import EventDispatcherSingleton
from settings import WOLFRAM_APPID


class Wolfram(on_demand.BaseOnDirectMessageOrTimelineDemandScript):
    pods_white_list = [
        'Result',
        'Response',
    ]

    replaces = [
        (r'wolfram\|alpha', 'Twizhoosh'),
        (r'Stephen Wolfram', '@soben713'),
        (r'wolfram', 'Twizhoosh'),
    ]

    def received_command(self, command, data, reply_function, sender, *args, **kwargs):
        if not self.st_memory.is_person_marked('wolfram', sender['screen_name'], 20):
            self.st_memory.mark_person('wolfram', sender['screen_name'])

            client = wolframalpha.Client(WOLFRAM_APPID)
            res = client.query(command)

            # Find the first pod that's not an input interpretation pot
            for pod in res.pods:
                if pod.title in self.pods_white_list and hasattr(pod, 'text'):
                    text = self.process_response(pod.text)
                    reply_function(text)
                    EventDispatcherSingleton().terminate_scripts()

    def process_response(self, text):
        for r, rep in self.replaces:
            regex = re.compile(r, re.IGNORECASE)
            text = regex.sub(rep, text)

        return text