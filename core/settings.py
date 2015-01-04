import os

# Import deploying related keys
CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY', None)
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', None)
OAUTH_TOKEN = os.environ.get('TWITTER_OAUTH_TOKEN', None)
OAUTH_TOKEN_SECRET = os.environ.get('TWITTER_OAUTH_TOKEN_SECRET', None)

DEBUG = os.environ.get('DEBUG', True)

TWEET_LENGTH = 140
TWEET_URL_LENGTH = 21
TWIZHOOSH_USERNAME = 'twizhoosh'


# order is preserved
INSTALLED_TIMELINE_SCRIPTS = [
    "spell_checker",
    "good_night",
    "reply_by_learned_replies",
]

INSTALLED_ON_DEMAND_SCRIPTS = [
    "learn_to_reply",
    "mustachify",
]

INSTALLED_STANDALONE_SCRIPTS = [
    "call_sherrgoo",
]
# Stand-Alone repeat time (seconds)
STAND_ALONE_REPEAT_TIME = 1