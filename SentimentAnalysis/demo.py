import tweepy
from textblob import TextBlob
#French adaptor
# from textblob_fr import PatternTagger, PatternAnalyzer

import numpy as np
import operator


# Step 1 - Authenticate
consumer_key='AOK56ynlXZeUuNrGHZqExHsEH'
consumer_secret='5wWahG3Z6MvyhAPqCI9mSO2T4TcsFlRr6nI6rI6cLGWVj2ZIMv'

access_token = '848229881074733056-WRwfiRSdwjpUi75vihtewiGKBWmc6No'
access_token_secret = 'Zyc87Ov237qma6LPBXp9B9VtLhDejY0TzgpwqGfu9d1OK'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 2 - Prepare query features

#List of candidates to French Republicans Primary Elections
candidates_names = ['Sarkozy', 'Kosciusko', 'Cope', 'Juppe', 'Fillon', 'Le Maire', 'Poisson']
#Hashtag related to the debate
name_of_debate = "PrimaireLeDebat" 
#Date of the debate : October 13th
since_date = "2016-10-13"
until_date = "2016-10-14"

#Step 2b - Function of labelisation of analysis
def get_label(analysis, threshold = 0):
	if analysis.sentiment[0]>threshold:
		return 'Positive'
	else:
		return 'Negative'


#Step 3 - Retrieve Tweets and Save Them
all_polarities = dict()
for candidate in candidates_names:
	this_candidate_polarities = []
	#Get the tweets about the debate and the candidate between the dates
	this_candidate_tweets = api.search(q=[name_of_debate, candidate], count=100, since = since_date, until=until_date)
	#Save the tweets in csv
	with open('%s_tweets.csv' % candidate, 'wb') as this_candidate_file:
		this_candidate_file.write('tweet,sentiment_label\n')
		for tweet in this_candidate_tweets:
			analysis = TextBlob(tweet.text)
			#Get the label corresponding to the sentiment analysis
			this_candidate_polarities.append(analysis.sentiment[0])
			this_candidate_file.write('%s,%s\n' % (tweet.text.encode('utf8'), get_label(analysis)))
	#Save the mean for final results
	all_polarities[candidate] = np.mean(this_candidate_polarities)
 
#Step bonus - Print a Result
sorted_analysis = sorted(all_polarities.items(), key=operator.itemgetter(1), reverse=True)
print ('Mean Sentiment Polarity in descending order :')
for candidate, polarity in sorted_analysis:
	print('%s : %0.3f' % (candidate, polarity))
