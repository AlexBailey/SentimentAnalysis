import tweepy
from textblob import TextBlob

consumer_key = 'ENTER THIS INFO'
consumer_secret = 'ENTER THIS INFO'

access_token = 'ENTER THIS INFO'
access_token_secret = 'ENTER THIS INFO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('@united')

for tweet in public_tweets:
	print(tweet.text)

	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print("")