from smart_handlers_manager import SmartHandlersManager


class TestTwitter:
	def update_status(self, *args, **kwargs):
		print 'update status was called'
		print 'args: %s \n kwargs: %s' % (args, kwargs)


if __name__ == '__main__':
	manager = SmartHandlersManager(twitter = TestTwitter())

	while True:
		timeline_update = raw_input("Enter a tweet message to see how @Twizhoosh responses\n").decode('utf-8')
		manager.on_timeline_update({
			'text': timeline_update,
			'id': 123456789,
			'id_str': '123456789',
			'user': {
				'screen_name': 'test_user',
			}
		})