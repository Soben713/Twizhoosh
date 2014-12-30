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
