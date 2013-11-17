This is a template for creating your own twitter bot using python and heroku. The only programming necessary is to update the function ```get_message()``` in ```app.py``` to create your bot's tweets.

Confused? Try reading [this](http://tinysubversions.com/2013/09/how-to-make-a-twitter-bot/). Or contact me [@jehosafet](https://twitter.com/jehosafet).

Requirements
--------
* __python__
   * Install [Twython](https://github.com/ryanmcgrath/twython) (```pip install Twython```): _for generating/posting tweets in python app_
* __heroku__
   * [account](https://www.heroku.com/) and [toolbelt](https://toolbelt.heroku.com/): _for hosting python app and keeping it running_

Instructions
--------
0. Fork and pull this repo.

1. In your local repo, create a new heroku app.
    * ```heroku create --stack cedar```
    * ```heroku apps:rename YOUR_APP_NAME```
    * Your heroku app will now keep the python script ```app.py``` running as often as possible.

2. Create a [new twitter account](https://twitter.com/).
    * Use your current email to create the account by adding [a tag](http://en.wikipedia.org/wiki/Email_address#Address_tags).
       - Ex: _email@gmail.com_ => _email+twitterbot@gmail.com_
    * Confirm the email address associated with this new twitter account.

3. From your main twitter account create a [new twitter app](https://dev.twitter.com/apps).
    * Under _Settings_ / _Application Type_:
        - Enable _"Read and Write"_
        - Check _"Allow this application to be used to Sign in with Twitter"_
    * Under _Details_:
        - Click _"Create My Access Token"_
    * Connect this app to your bot's twitter acount (help [here](http://dghubble.com/blog/posts/twitter-app-write-access-and-bots/))
        - `$ gem install twurl`
        - `$ twurl authorize --consumer-key "REPLACE_THIS" --consumer-secret "REPLACE_THIS"`

4. Create environment variables.
    * In your local repo, create a file called ```.env``` that contains your twitter app keys, one per line:
        - ```TWITTER_CONSUMER_KEY=replace_this```
        - ```TWITTER_CONSUMER_SECRET=replace_this```
        - ```TWITTER_OAUTH_TOKEN=replace_this```
        - ```TWITTER_OAUTH_TOKEN_SECRET=replace_this```
    * For [heroku](https://devcenter.heroku.com/articles/config-vars), use ```heroku-config``` to copy contents of ```.env``` to your heroku app.
        - Install heroku-config: ```heroku plugins:install git://github.com/ddollar/heroku-config.git```.
        - Now run ```heroku config:push```.
            - NOTE: To update heroku environment variables later, run ```heroku config:push --overwrite```
            - Alternatively, add heroku environment variables manually using ```heroku config:set YOUR_ENV_VAR=replace_this```

__Okay, now here's the fun part:__

5. Update the function ```get_message()``` in ```app.py``` to create your bot's tweets.
    * Read about [twitter bot etiquette](http://tinysubversions.com/2013/03/basic-twitter-bot-etiquette/) for bot guidelines.
    * Use the [wordnik api](https://github.com/wordnik/wordnik-python) for getting random parts of speech.

6. Test your bot locally.
    * Running ```foreman start``` should generate your tweets once every minute, or at whatever rate you set in ```app.py```.

7. Commit and push local changes to heroku and github.
    * ```git push heroku master``` pushes all commits to heroku and starts up your app.
    * Your bot should now tweet as long as your heroku app is running (via the worker dyno).
