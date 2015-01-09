# Twizhoosh

[@Twizhoosh](https://twitter.com/twizhoosh) is a smart Persian twitter-bot, written in Python and aimed to be easily
readable and contributable.
 
## Know Him Better
- Twizhoosh does not talk too much and will not bother people who follow him.
- He does not have any long term memory.
- He would not be rude to anyone, unless it is necessary.
- He is smart.
 
## How to Contribute
 
Are you willing to contribute to Twizhoosh? Great. If you only need to edit a file (e.g. adding a spelling
correction entry) you may just browse the file on Github and click on the edit icon. Github will do the rest
for you. But if you are trying to implement a script for Twizhoosh you should:

1. Fork Twizhoosh.
2. Create your script branch: `git checkout -b my-new-script`
3. Implement your script.
4. Commit your changes: `git commit -am 'Add some script'`
5. Push to the branch: `git push origin my-new-script`
6. Submit a pull request.
 
## Implementing a Script

There are two types of scripts:

1. Twitter related scripts: These scripts listen to events returned by Twitter's streaming API.
2. Stand-alone scripts: Called repeatedly.

Take a look at current scripts in `scripts` folder. Do not forget to add your scripts to `settings.py` after
implementing.

## Testing
Before submitting a pull request, test your script by running `twizhoosh.py`.

## Requirements
You need `Python 3.4` or later and `twython 3.2` to run the code.
