from core.scripts.timeline.base.base_handler import BaseHandler
from core.utils.logging import debug
import random
from io import BytesIO

class NobodyCares(base_handler.BaseHandler):

	def timeline_update(self, data):
		do_reply = (random.uniform(0, 500) > 498)
		if not do_reply or not 'text' in data or len(data['in_reply_to_status_id_str'])!=0:
			return
		
		photo_address = 'assets/nobody_cares.jpg'
		
		try:
			#photo = self.twitter.upload_media(photo)
			#self.reply_to(data, status='...', media_ids=[photo['media_id']])
            self.twitter.update_status_with_media(
                status='@' + data['user']['screen_name'] + ' NOBODY CARES!!',
                media=BytesIO(photo_address),
                in_reply_to_status_id=data['id_str']
            )
		except TwythonError as e:
			print (e)
