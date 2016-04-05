import re
import urllib
from io import BytesIO

import requests

from core.scripts.twitter_related import on_demand
from core.twitter_related_scripts_runner import EventDispatcherSingleton
from core.utils.logging import log
from core.utils.regex import combine_regexes


class HowOld(on_demand.BaseOnTimelineDemandScript):
    command_pattern = combine_regexes([
        '.*چند سالمه.*',
        r'.*how old.*',
    ])

    def received_command(self, command, data, reply_function, sender, *args, **kwargs):
        match = re.search(self.command_pattern, command, re.IGNORECASE)

        if match:
            log("Asked for how old, by {0}".format(sender['screen_name']))

            if not self.st_memory.is_person_marked('how-old', sender['screen_name']):
                # Mark them
                self.st_memory.mark_person('how-old', sender['screen_name'])

                avatar_url = sender['profile_image_url']
                avatar_url = avatar_url.replace('_normal', '')
                avatar_img = requests.get(url=avatar_url).content



                self.twitter.update_status_with_media(
                    status='@' + sender['screen_name'],
                    media=BytesIO(img),
                    in_reply_to_status_id=data['id_str']
                )

                EventDispatcherSingleton().terminate_scripts()

            else:
                self.twitter.reply_to(data, ':)')