from core.timeline_scripts_manager import TimelineScriptsManager


class TestTwitter:
    def print_args_kwargs(self, args, kwargs):
        print('args: {0} \n kwargs: {1}'.format(args, kwargs))

    def update_status(self, *args, **kwargs):
        print('update status was called')
        self.print_args_kwargs(args, kwargs)

    def send_direct_message(self, *args, **kwargs):
        print('direct message was called')
        self.print_args_kwargs(args, kwargs)

    def update_status_with_media(self, *args, **kwargs):
        print('update_status_with_media was called')
        self.print_args_kwargs(args, kwargs)


if __name__ == '__main__':
    manager = TimelineScriptsManager(twitter=TestTwitter())

    while True:
        timeline_update = input(
            "Specify a sample timeline update message to see what @Twizhoosh does\n")
        manager.on_timeline_update({
            'text': timeline_update,
            'id': 123456789,
            'id_str': '123456789',
            'user': {
                'screen_name': 'test_user',
                'id_str': '23487',
                'profile_image_url': 'http://example.com',
            }
        })
