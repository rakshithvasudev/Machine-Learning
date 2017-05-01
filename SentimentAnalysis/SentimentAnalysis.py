import csv
import tweepy 
from textblob import TextBlob



'''
 this will be gone by time you try to access.
'''

consumer_key='AOK56ynlXZeUuNrGHZqExHsEH'
consumer_secret='5wWahG3Z6MvyhAPqCI9mSO2T4TcsFlRr6nI6rI6cLGWVj2ZIMv'

access_token = '848229881074733056-WRwfiRSdwjpUi75vihtewiGKBWmc6No'
access_token_secret = 'Zyc87Ov237qma6LPBXp9B9VtLhDejY0TzgpwqGfu9d1OK'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)





def get_label(polarity):
	if (polarity>0):
		return 'Positive'
	elif(polarity<0):
		return 'Negative'
	else:
		return 'Neutral'



polarities=[]	
api = tweepy.API(auth)
public_tweets = api.search('Trump',count=100)
print('searching successful')
	

with open("tweets.csv",'w') as csvfile:
	csvfile.write('tweet, Sentiment_label\n')
	for tweet in public_tweets:
		analysis = TextBlob(tweet.text)
		polarity = analysis.sentiment.polarity 
		polarities.append(polarity)
		csvfile.write('%s,%s\n' % (tweet.text.encode('utf8'), get_label(polarity)))
		 