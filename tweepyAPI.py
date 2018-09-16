import tweepy
from tweepy import OAuthHandler
import json
import wget
 
consumer_key = 'OY3mCXXhLBqIqamPhUa3AnCQE'
consumer_secret = '7sQ0pAB35FSTe1w3JrWNURyvUSeytxAbMjHIFVUg2E3hCENxuY'
access_token = '1039189163680178176-k2adgUlkb54l7VKWnrrVjzgmYmhNyT'
access_secret = 'b5GMpQN2V6MPqNeiuLJAoigP6P6lMh2WN0HsLf484fUnt'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name="@Discovery",count=200, include_rts=False,
                           exclude_replies=True)

last_id = tweets[-1].id
 
while (True):
    more_tweets = api.user_timeline(screen_name="@Discovery",
                                count=200,
                                include_rts=False,
                                exclude_replies=True,
                                max_id=last_id-1)
# There are no more tweets
    if (len(more_tweets) == 0):
          break
    else:
          last_id = more_tweets[-1].id-1
          tweets = tweets + more_tweets
         
media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])
        

for media_file in media_files:
    wget.download(media_file)
