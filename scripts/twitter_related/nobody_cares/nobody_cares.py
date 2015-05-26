import os
import random
from io import BytesIO
import requests

from twython.exceptions import TwythonError

from core.scripts.twitter_related import base
from core.twitter_related_scripts_runner import EventDispatcherSingleton
from core.utils.google_image import get_random_google_image
from core.utils.logging import log


class NobodyCares(base.BaseTimelineScript):
    search_phrases = ["I don't care sponge bob meme"]

    def on_timeline_update(self, data):
        do_reply = (random.randint(0, 400) == 0)
        if not do_reply or data.get('in_reply_to_status_id_str', None) or data['entities']['user_mentions'] or len(
                data['text']) == 0:
            return

        log('Ok...sending nobody cares')

        img_url = get_random_google_image(random.choice(self.search_phrases))
        img = requests.get(url=img_url).content
        log('image: %s' % img_url)

        try:
            self.twitter.update_status_with_media(
                status='@' + data['user']['screen_name'],
                media=BytesIO(img),
                in_reply_to_status_id=data['id_str']
            )
            EventDispatcherSingleton().terminate_scripts()
        except TwythonError as e:
            print(e)
