
import tweepy 
from textblob import TextBlob

#this will be gone by time you try to access.
consumer_key='AOK56ynlXZeUuNrGHZqExHsEH'
consumer_secret='5wWahG3Z6MvyhAPqCI9mSO2T4TcsFlRr6nI6rI6cLGWVj2ZIMv'

access_token = '848229881074733056-WRwfiRSdwjpUi75vihtewiGKBWmc6No'
access_token_secret = 'Zyc87Ov237qma6LPBXp9B9VtLhDejY0TzgpwqGfu9d1OK'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api = tweepy.API(auth)

public_tweets = api.search('Trump')


counter=0
for tweet in public_tweets:
	# print(tweet.text)
	counter = counter+1

	analysis = TextBlob(tweet.text)
	polarity = analysis.sentiment.polarity 

	if(polarity != 0):
		print(tweet.text)
		print(analysis.sentiment)	
		print(counter)




