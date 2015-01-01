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
INSTALLED_HANDLERS = [
    "core.command_dispatcher.CommandDispatcher",

    "smart_handlers.spell_checker.spell_checker.SpellChecker",
    "smart_handlers.goodnight.goodnight.GoodNight",
    "smart_handlers.reply_by_learned_replies.reply_by_learned_replies.ReplyByLearnedReplies",
    # "smart_handlers.say_hi.say_hi.SayHi"
]

INSTALLED_COMMAND_PARSERS = [
    "command_parsers.learn_to_reply.learn_to_reply.LearnToReply",
    "command_parsers.mustachify.mustachify.Mustachify",
]
