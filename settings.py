import os

# Import deploying related keys
CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY', None)
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', None)
OAUTH_TOKEN = os.environ.get('TWITTER_OAUTH_TOKEN', None)
OAUTH_TOKEN_SECRET = os.environ.get('TWITTER_OAUTH_TOKEN_SECRET', None)
WOLFRAM_APPID = os.environ.get('WOLFRAM_APPID', None)

DEBUG = (os.environ.get('DEBUG', "True") == "True")

TWEET_LENGTH = 140
TWEET_URL_LENGTH = 21
TWIZHOOSH_USERNAME = 'twizhoosh'


# Ordered list of installed twitter related scripts
INSTALLED_TWITTER_RELATED_SCRIPTS = [
    "dedicate_round_tweets",
    "remind_round_tweets",
    "spell_checker",
    "choose_random_choice",
    "mustachify",
    "hungry",
    "do_me_a_9gag",
    "get_grade",
    # "good_night",
    "reply_by_learned_replies",
    "learn_to_reply",
    "wolfram",
    "nobody_cares",
]

# Ordered list of installed standalone scripts
INSTALLED_STANDALONE_SCRIPTS = [
    # "call_sherrgoo",
    "give_advice",
]

# Stand-Alone repeat time chunks in seconds, every script may override number of chunks
STAND_ALONE_REPEAT_TIME_CHUNKS = 10