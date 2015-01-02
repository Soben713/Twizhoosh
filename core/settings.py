import os

# Import deploying related keys
CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY', None)
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', None)
OAUTH_TOKEN = os.environ.get('TWITTER_OAUTH_TOKEN', None)
OAUTH_TOKEN_SECRET = os.environ.get('TWITTER_OAUTH_TOKEN_SECRET', None)

DEBUG = os.environ.get('DEBUG', True)

TWEET_LENGTH = 140
TWEET_URL_LENGTH = 21

# TODO: Refactor the way modules are loaded. Since added some modules to
# core, had to delete HANDLERS_PACKAGE

TWIZHOOSH_USERNAME = 'twizhoosh'

# order is preserved
INSTALLED_TIMELINE_SCRIPTS = [
    "core.on_demand_scripts_manager.OnDemandScriptsManager",

    "scripts.timeline.spell_checker.spell_checker.SpellChecker",
    "scripts.timeline.goodnight.goodnight.GoodNight",
    "scripts.timeline.reply_by_learned_replies.reply_by_learned_replies.ReplyByLearnedReplies",
    # "scripts.timeline.say_hi.say_hi.SayHi"
]

INSTALLED_ON_DEMAND_SCRIPTS = [
    "scripts.on_demand.learn_to_reply.learn_to_reply.LearnToReply",
    "scripts.on_demand.mustachify.mustachify.Mustachify",
]
