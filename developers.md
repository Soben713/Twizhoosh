---
layout: developers_base
title: Developers Guide
permalink: /developers/
---

# Developer's Guide
If you are already using Twizhoosh, you may be encouraged to contribute something back to it. In fact that is why
Twizhoosh was made. You could:

- Implement a new script
- Find bugs or typos
- Fix bugs
- Translate an existing script to a new language
- Help us complete the documentations

This document explains how to implement new scripts and how to modify the documentations. 

## First Steps With Git

You don't need to be a git master to contribute to Twizhoosh. If you only need to edit a file you could just 
browse the file on [Github](https://github.com/Soben713/Twizhoosh) and click on the edit icon.

But if you are trying to do more (like implementing a new script) you should:

1. Fork Twizhoosh.
2. Create your script branch: `git checkout -b my-new-script`
3. Implement your script.
4. Commit your changes: `git commit -am 'Add some script'`
5. Push to the branch: `git push origin my-new-script`
6. Submit a pull request.
 
## Implementing a Script

There are two types of scripts, *twitter related scripts* and *stand-alone scripts*.

Twitter related scripts listen to events returned by
[Twitter's streaming API](https://dev.twitter.com/streaming/overview/messages-types).
Such as new tweets, new direct messages and many more.

But Stand-alone scripts get called repeatedly (every second, but don't count on it). These kind of scripts are useful to
implement features like tweeting a random advice at random times.

### Implementing a Twitter related script

See the list of twitter-related scripts in `scripts/twitter_related`. Every script has its own package containing a 
python file with the same name as its package's name and a `README.md` file. The empty `__init__.py` file is also necessary
to indicate that it's a python package.

Inside the python file, there should at least be a class with again the same name of the python file but in camel case form.

Your class should be a subclass of `BaseTwitterRelatedScript`.
But you will usually extend a sub-class of this class like `BaseTimelineScript` or `BaseDirectMessageScript` 
to implement your script.

Twitter related base classes are written in `core/scripts/twitter_related`.

### Implementing a Stand-alone script ###

Structure of stand-alone scripts are very much like twitter-related scripts but they should extend `BaseStandaloneScript`.

Standalone base classes are written in `core/scripts/standalone`.

## Testing
Before submitting a pull request, test your script by running `twizhoosh.py`.

## Requirements
You need `Python 3.4` or later and `twython 3.2` to run the code.