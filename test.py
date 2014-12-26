from smart_handlers_manager import SmartHandlersManager

class TestTwitter:
	def update_status(self, *args, **kwargs):
		print('update status was called')
		print('args: {0} \n kwargs: {1}'.format(args, kwargs))

if __name__ == '__main__':
	manager = SmartHandlersManager(twitter = TestTwitter())

	while True:
		timeline_update = input("Specify a sample timeline update message to see the what @Twizhoosh does\n")
		manager.on_timeline_update({
			'text': timeline_update,
			'id': 123456789,
			'id_str': '123456789',
			'user': {
				'screen_name': 'test_user',
			}
		})
