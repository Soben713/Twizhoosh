from core.scripts.twitter_related.base import BaseTimelineScript
from scripts.twitter_related.dedicate_round_tweets.dedicate_round_tweets import is_round


class RemindRoundTweets(BaseTimelineScript):
    def on_timeline_update(self, data):
        if is_round(data['user']['statuses_count'] + 1):
            text = 'توییت بعدی شما رند است'
            self.twitter.send_direct_message(text, data['user']['id'])