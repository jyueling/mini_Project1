import tweepy
from tweepy import OAuthHandler
import json
import wget
from os import rename
from glob import glob
import sys
import pymysql

consumer_key = 'Enter the consumer_key'
consumer_secret = 'Enter the consumer_secret'
access_token = 'Enter the access_key'
access_secret = 'Enter the access_secret'

password = ''

def get_tweet(): 
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    #connect to mysql database
    db = pymysql.connect("localhost","root", password,"proj");
     
    api = tweepy.API(auth)
    
    inputname = sys.argv[1]
    
    tweets = api.user_timeline(screen_name=inputname,count=200, include_rts=False,
                               exclude_replies=True)
    
    last_id = tweets[-1].id
     
    while (True):
        more_tweets = api.user_timeline(screen_name=inputname,
                                    count=200,
                                    include_rts=False,
                                    exclude_replies=True,
                                    max_id=last_id-1)
        if (len(more_tweets) == 0):
              break
        else:
              last_id = more_tweets[-1].id-1
              tweets = tweets + more_tweets
        #load 200 images
        if (len(tweets) >= 20):
            break
        
    media_files = set()
    for status in tweets:
        media = status.entities.get('media', [])
        if(len(media) > 0):
            media_files.add(media[0]['media_url'])
    
    #write tweet objects to JSON
    file = open('tweet.json', 'w') 
    
    for status in tweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    file.close()
            
    #download all images
    for media_file in media_files:
        wget.download(media_file)
    
    #rename the images to 'img%d.jpg'
    images=glob('*.jpg')
    d=0
    for fname in images:
        filename="img_%d.jpg"%d
        
        d+=1
        rename(fname,filename)   
    #input number of images and twitterID to MySQL database
    cursor = db.cursor()
    sql = """INSERT INTO tweetid(twitterID,img_num) VALUES (%s,%s)"""
    try:
        cursor.execute(sql,(inputname,d))
        db.commit()
    except:
        db.rollback()
        
    return inputname,db,d

if __name__ == '__main__':
    get_tweet()
