import os
import random
from io import BytesIO
from twython.exceptions import TwythonError
from core.scripts.timeline.base import BaseTimelineScript
from core.utils.logging import log


class NobodyCares(BaseTimelineScript):
    def timeline_update(self, data):
        do_reply = (random.randint(0, 100) == 0)
        if not do_reply or not 'text' in data or data.get('in_reply_to_status_id_str', None):
            return

        log('Ok...sending nobody cares')

        script_dir = os.path.dirname(__file__)
        photo_rel_address = 'assets/nobody_cares.jpg'
        photo_path = os.path.join(script_dir, photo_rel_address)
        photo = open(photo_path, 'rb')

        log('Photo found')

        try:
            self.twitter.twitter.update_status_with_media(
                status='@' + data['user']['screen_name'],
                media=photo,
                in_reply_to_status_id=data['id_str']
            )
        except TwythonError as e:
            print(e)
