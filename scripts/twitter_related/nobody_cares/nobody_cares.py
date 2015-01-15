import os
import random

from twython.exceptions import TwythonError

from core.scripts.twitter_related import base
from core.twitter_related_scripts_runner import EventDispatcherSingleton
from core.utils.logging import log


class NobodyCares(base.BaseTimelineScript):
    def on_timeline_update(self, data):
        do_reply = (random.randint(0, 500) == 0)
        if not do_reply or data.get('in_reply_to_status_id_str', None) or data['entities']['user_mentions'] or len(
                data['text']) == 0:
            return

        log('Ok...sending nobody cares')

        script_dir = os.path.dirname(__file__)
        photo_rel_address = 'assets/nobody_cares.jpg'
        photo_path = os.path.join(script_dir, photo_rel_address)
        photo = open(photo_path, 'rb')

        log('Photo found')

        try:
            self.twitter.update_status_with_media(
                status='@' + data['user']['screen_name'],
                media=photo,
                in_reply_to_status_id=data['id_str']
            )
            EventDispatcherSingleton().terminate_scripts()
        except TwythonError as e:
            print(e)
