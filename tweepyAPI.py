import tweepy
from tweepy import OAuthHandler
import wget
 
consumer_key = 'Enter the consumer_key'
consumer_secret = 'Enter the consumer_secret'
access_token = 'Enter the access_key'
access_secret = 'Enter the access_secret'
 
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
    if (len(more_tweets) == 0):
          break
    else:
          last_id = more_tweets[-1].id-1
          tweets = tweets + more_tweets
    #load certain number of images, if need to download all, command these two lines
    if (len(tweets) >= 20):
        break
    
media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])
        
#download all images
for media_file in media_files:
    wget.download(media_file)

#rename the images to 'img_%d.jpg'
images=glob('*.jpg')
d=0
for fname in images:
    filename="img_%d.jpg"%d
    
    d+=1
    rename(fname,filename) 
