# TODO: Refactor the way modules are loaded. Since added some modules to core, had to delete HANDLERS_PACKAGE

# order is preserved
INSTALLED_HANDLERS = [
	"core.command_dispatcher.CommandDispatcher",
	"smart_handlers.spell_checker.spell_checker.SpellChecker",
	#"smart_handlers.say_hi.say_hi.SayHi"
]

INSTALLED_COMMAND_PARSERS = [
	"command_parsers.learn_to_say.learn_to_say.LearnToSay",
]
