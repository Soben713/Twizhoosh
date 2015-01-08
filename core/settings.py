import os

# Import deploying related keys
CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY', None)
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', None)
OAUTH_TOKEN = os.environ.get('TWITTER_OAUTH_TOKEN', None)
OAUTH_TOKEN_SECRET = os.environ.get('TWITTER_OAUTH_TOKEN_SECRET', None)

DEBUG = (os.environ.get('DEBUG', "True") == "True")

TWEET_LENGTH = 140
TWEET_URL_LENGTH = 21
TWIZHOOSH_USERNAME = 'twizhoosh'


INSTALLED_TWITTER_RELATED_SCRIPTS = [
    "dedicate_round_tweets",
    "mustachify",
    "spell_checker",
    "good_night",
    "nobody_cares",
    "reply_by_learned_replies",
    "learn_to_reply",
    "get_grade",
]

INSTALLED_STANDALONE_SCRIPTS = [
    "call_sherrgoo",
]

# Stand-Alone repeat time chunks in seconds, every script may override number of chunks
STAND_ALONE_REPEAT_TIME_CHUNKS = 10