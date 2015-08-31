from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pymongo import MongoClient
import json
from twittercredentials import access_token, access_token_secret, consumer_key, consumer_secret

#Tells which DB to use, or creates it if it does not exist.
client = MongoClient()
db = client['twitter-watch']

class StdOutListener(StreamListener):

    def on_data(self, data):
        parsed_data = json.loads(data)
        tweet = { "created_at": parsed_data['created_at'],
                  "text": parsed_data['text']
                  }
        tweet_id = db.tweets.insert_one(tweet).inserted_id
        tweet_id
        print(parsed_data['text'])
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['python', 'javascript', 'ruby'], languages=['no', 'en'])