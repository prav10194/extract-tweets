from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
consumer_key = "xJ3bfmVFkMHY0zegrQfxC7Qtu"
consumer_secret = "GonIvFlmBdyvluwqxSqcRdP5SrqY02dFnbzQA3P28I9F5SxXj6"
access_key = "2413044493-18vqGOAPbHZBmDi5SXLtnfC3VwpbUJ0sVRBG6PN"
access_secret = "NuUnbuHVbPHJ4boCENtVdeavBB7PEyCxFzCi1RYHK2awR"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print status

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key, access_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["pranavbhatia"])
		
