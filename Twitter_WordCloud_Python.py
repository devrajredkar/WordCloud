
import tweepy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import json



consumer_key = "---"
consumer_secret = "---"
access_token = "---"
access_token_secret = "---"


auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)





results = [status._json for status in tweepy.Cursor(api.user_timeline, 
                            screen_name='@sports_freak_rd', 
                            tweet_mode="extended").items(20000)]



print(type(results))


df = pd.json_normalize(results)

df.head()

len(df)
    



df['full_text'].to_csv("tweets.csv",index = False)



import stylecloud
stylecloud.gen_stylecloud(file_path='tweets.csv',
                          icon_name= 'fab fa-twitter',
                          palette='colorbrewer.qualitative.Paired_3', #https://jiffyclub.github.io/palettable/
                          background_color='black',
                          gradient='horizontal',
                          stopwords = True,
                          custom_stopwords=['RT','THE','IS','WITH',
                                            'ON','THIS','HTTPS','CO','TO','AND','OF','IT','MY','FOR','IN','a', 'about', 'above', 'after', 
                                            'again', 'against', 'ain', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', "aren't", 'as', 
                                            'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 
                                            'can',          'couldn', "couldn't", 'd', 'did', 'didn', "didn't", 'do', 'does', 'doesn', 
                                            "doesn't", 'doing', 'don', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further',
                                            'had', 'hadn', "hadn't", 'has', 'hasn', "hasn't", 'have', 'haven', "haven't", 'having', 'he', 
                                            'her', 'here',           'hers', 'herself', 'him', 'himself', 'his', 'how',          'i', 
                                            'if', 'in', 'into', 'is', 'isn', "isn't", 'it', "it's", 'its', 'itself', 'just', 'll', 'm', 
                                            'ma', 'me', 'mightn', "mightn't", 'more', 'most', 'mustn', "mustn't", 'my', 'myself', 'needn', 
                                            "needn't", 'no', 'nor', 'not', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 
                                            'our', 'ours', 'ourselves', 'out', 'over', 'own', 're', 's', 'same', 'shan', "shan't", 'she', 
                                            "she's", 'should', "should've", 'shouldn', "shouldn't", 'so', 'some', 'such', 't', 'than', 
                                            'that', "that'll",           'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 
                                            'these', 'they',                                            'this', 'those', 'through', 'to', 
                                            'too', 'under', 'until', 'up', 've', 'very', 'was', 'wasn', "wasn't", 'we',        
                                            'were', 'weren', "weren't", 'what',           'when',           'where',            'which', 
                                            'while', 'who',          'whom', 'why', 'will',          'with', 'won', "won't",          
                                            'wouldn', "wouldn't", 'y', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 
                                            'yourself', 'yourselves', 'even', 'n', 'would', 'like', 'v', '>']
)
from IPython.display import Image
Image('stylecloud.png')


