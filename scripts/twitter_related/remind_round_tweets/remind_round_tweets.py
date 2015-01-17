from core.scripts.twitter_related.base import BaseTimelineScript
from scripts.twitter_related.dedicate_round_tweets.dedicate_round_tweets import is_round


class RemindRoundTweets(BaseTimelineScript):
    def on_timeline_update(self, data):
        next_tweet = data['user']['statuses_count'] + 1
        if is_round(next_tweet):
            text = 'توییت بعدی شما توییت {0}ام است.'.format(next_tweet)
            self.twitter.send_direct_message(text=text, user_id=data['user']['id'])