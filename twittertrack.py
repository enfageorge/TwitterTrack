import tweepy

# Consumer API keys
API_KEY = '#'
API_SECRET_KEY = '#'
ACCESS_TOKEN = '#'
ACCESS_TOKEN_SECRET = '#'

# override tweepy.StreamListener to add logic to on_status


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)


trackwho = 'bbc'#Enter keyword here.

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=[trackwho])
