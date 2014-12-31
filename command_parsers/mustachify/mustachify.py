import re
import urllib
from io import BytesIO

import requests

from core.command_parsers.base import base_command_parser
from core.utils.logging import log


class Mustachify(base_command_parser.BaseCommandParser):
    command_pattern = '.*س(ی)?بیل.*'

    def command_update(self, command, data):
        match = re.search(self.command_pattern, command)
        mustaches = self.short_term_memory.setdefault('mustache', [])

        if match:
            log("Asked for a mustache, by {0}".format(data['user']['screen_name']))

            if not data['user']['id_str'] in mustaches:
                mustaches.append(data['user']['id_str'])
                avatar_url = data['user']['profile_image_url']
                avatar_url = avatar_url.replace('_normal', '')

                raw_url = 'http://mustachify.me/?src={0}'
                img_url = raw_url.format(urllib.request.quote(avatar_url))
                log("Image url: {0}".format(img_url))

                img = requests.get(url=img_url).content

                self.twitter.update_status_with_media(
                    status='@' + data['user']['screen_name'],
                    media=BytesIO(img),
                    in_reply_to_status_id=data['id_str']
                )

            else:
                self.reply_to(data, 'بسته دیگه :)')