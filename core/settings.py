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


# order is preserved
INSTALLED_TIMELINE_SCRIPTS = [
    "spell_checker",
    "good_night",
    "reply_by_learned_replies",
    "nobody_cares",
]

INSTALLED_ON_DEMAND_SCRIPTS = [
    "learn_to_reply",
    "mustachify",
]

INSTALLED_STANDALONE_SCRIPTS = [
    "call_sherrgoo",
    "dedicate_round_tweets",
]
# Stand-Alone repeat time chunks in seconds, every script may override number of chunks
STAND_ALONE_REPEAT_TIME_CHUNKS = 1