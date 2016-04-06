import re
import urllib
from io import BytesIO

import requests

from core.scripts.twitter_related import on_demand
from core.twitter_related_scripts_runner import EventDispatcherSingleton
from core.utils.logging import log
from core.utils.regex import combine_regexes


class Mustachify(on_demand.BaseOnTimelineDemandScript):
    command_pattern = combine_regexes([
        '.*س(ی)?بیل.*',
        r'.*mustache.*',
    ])

    def received_command(self, command, data, reply_function, sender, *args, **kwargs):
        match = re.search(self.command_pattern, command, re.IGNORECASE)

        if match:
            log("Asked for a mustache, by {0}".format(sender['screen_name']))

            if not self.st_memory.is_person_marked('mustache', sender['screen_name']):
                # Mark them
                self.st_memory.mark_person('mustache', sender['screen_name'])

                avatar_url = sender['profile_image_url']
                avatar_url = avatar_url.replace('_normal', '')

                raw_url = 'http://mustachify.me/?src={0}'
                img_url = raw_url.format(urllib.request.quote(avatar_url))
                log("Image url: {0}".format(img_url))
                img = BytesIO(requests.get(url=img_url).content)

                self.twitter.update_status_with_media(
                    status='@' + sender['screen_name'],
                    media=img,
                    in_reply_to_status_id=data['id_str']
                )

                EventDispatcherSingleton().terminate_scripts()

            else:
                self.twitter.reply_to(data, ':)')