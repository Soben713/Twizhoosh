import re
from urllib import request

from core.scripts.twitter_related import on_demand


class DoMeA9gag(on_demand.BaseOnDirectMessageOrTimelineDemandScript):
    command_pattern = r'.*9gag.*'

    def received_command(self, command, data, reply_message, sender, *args, **kwargs):
        if re.search(self.command_pattern, command, re.IGNORECASE):
            r = request.Request('http://9gag.com/random')
            res = request.urlopen(r)
            reply_message(res.geturl())