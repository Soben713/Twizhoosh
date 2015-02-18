from io import BytesIO
import re
from urllib import request

from bs4 import BeautifulSoup
import requests
from core.scripts.twitter_related import on_demand
from core.twitter_related_scripts_runner import EventDispatcherSingleton
from core.utils.logging import log
import settings


class DoMeA9gag(on_demand.BaseOnTimelineDemandScript):
    command_pattern = r'.*9gag.*'

    def received_command(self, command, data, reply_message, sender, *args, **kwargs):
        if re.search(self.command_pattern, command, re.IGNORECASE):
            while True:
                r = request.Request('http://9gag.com/random')
                opened = request.urlopen(r)
                parsed = BeautifulSoup(opened)

                log("Found 9gag link: %s" % (opened.geturl()))

                if parsed.select('.gif-post'):
                    # Ignore gif posts
                    log("Ignoring... was a gif post")
                    continue

                try:
                    log("Trying to send %s" % opened.geturl())
                    img_url = parsed.select('.badge-item-img')[0].get('src')
                    title = parsed.select('.badge-item-title')[0].getText()

                    img = requests.get(url=img_url).content

                    status = '@%s %s - %s' % (sender['screen_name'], title, opened.geturl())
                    if len(status) > settings.TWEET_LENGTH:
                        status = '@%s %s' % (sender['screen_name'], title)

                    self.twitter.update_status_with_media(
                        status=status,
                        media=BytesIO(img),
                        in_reply_to_status_id=data['id_str']
                    )

                    EventDispatcherSingleton().terminate_scripts()
                    break
                except Exception:
                    pass
