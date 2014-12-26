# Twizhoosh

[@Twizhoosh](https://twitter.com/twizhoosh) is a smart Persian twitter-bot, written in Python and aimed to be easily readable and contributable.
 
## Know Him Better
- Twizhoosh does not talk too much and will not bother people who follow him.
- He does not reply to a tweet more than once.
- He never replies to people he is not following.
- He does not have any memory.
- He would not be rude to anyone, unless it is neccessary.
- He is smart.
 
## How to Contribute
 
Are you willing to contribute to Twizhoosh? Great. If you only need to edit a file (e.g. adding a spelling correction entry) you may just browse the file on Github and click on the edit icon. Github will do the rest for you. But if you are trying to implement a feature for Twizhoosh (called a smart handler) you should:

1. Fork Twizhoosh.
2. Create your feature branch: `git checkout -b my-new-feature`
3. Implement your feature.
4. Commit your changes: `git commit -am 'Add some feature'`
5. Push to the branch: `git push origin my-new-feature`
6. Submit a pull request.
 
## Implementing a Feature
 
Features like spelling correction, etc are called smart handlers. When someone Twizhoosh follows, tweets. The tweet is passed to smart handlers in the order specified in `settings.py`. The process ends as soon as a smart handler replies or the list ends.

For adding a smart handler, create a python package in `smart_handlers` with name of your feature. Create a python module in your package that contains a subclass of `BaseHandler` (which is implemented in `smart_handlers/base/base_handler.py`). This is the class you will implement your feature in. You must implement the `timeline_update` method, which gets called for each new tweet in the timeline. For more information, I suggest you to take a look at the current smart handlers.

## Testing
Before submitting a pull request, test your feature. You can do it by running `test.py` and simulating the timeline.

## Requirements
You need `Python 3.4` or later and `twython 3.2` to run the code.
