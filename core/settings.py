import os

# Import deploying related keys
CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
OAUTH_TOKEN = os.environ['TWITTER_OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = os.environ['TWITTER_OAUTH_TOKEN_SECRET']

DEBUG = os.environ['DEBUG']

TWEET_LENGTH = 140
TWEET_URL_LENGTH = 21

# TODO: Refactor the way modules are loaded. Since added some modules to
# core, had to delete HANDLERS_PACKAGE

TWIZHOOSH_USERNAME = 'twizhoosh'

# order is preserved
INSTALLED_HANDLERS = [
    "core.command_dispatcher.CommandDispatcher",
    "smart_handlers.reply_by_learned_replies.reply_by_learned_replies.ReplyByLearnedReplies",
    "smart_handlers.spell_checker.spell_checker.SpellChecker",
    # "smart_handlers.say_hi.say_hi.SayHi"
]

INSTALLED_COMMAND_PARSERS = [
    "command_parsers.learn_to_reply.learn_to_reply.LearnToReply",
]
