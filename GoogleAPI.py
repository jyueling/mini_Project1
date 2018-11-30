import io
import os
from glob import glob

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import tweepyAPI
import pymongo

inputname,db,d = tweepyAPI.get_tweet()

client = pymongo.MongoClient("mongodb://localhost:27017/")
mgdb = client["proj3"]
tableid = mgdb["tweetid"]
table_label = mgdb["img_label"]

data1 = {'tweetID':inputname,'img_num':d}
tableid.insert(data1)

client = vision.ImageAnnotatorClient()
d=0

for image in os.listdir('./'):
    if image.endswith('.jpg'):
        file_name = os.path.join(os.path.dirname(__file__),image)
        
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
            
        img = types.Image(content=content)
        response = client.label_detection(image=img)
        labels = response.label_annotations
        print('Labels:')
        img = Image.open(image)
        img.resize((128,128))
        draw = ImageDraw.Draw(img)
        a=0
        for label in labels:
            print(label.description)
            #font=ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf", 30)
            #draw.text((0, a),label.description,(255,255,255),font=font)
            draw.text((0, a),label.description,(255,255,255))
            
            a+=20
	#MySQL input twitterId and Labels in Database
            cursor = db.cursor()
            sql = """INSERT INTO img(twitterID,labels) VALUES (%s,%s)"""
            try:
                cursor.execute(sql,(inputname,label.description))
                db.commit()
            except:
                db.rollback()
        #MongoDB input twitterID and lables in Database     
            data2 = {'tweetID':inputname,'label':label.description}
            table_label.insert(data2)
        draw = ImageDraw.Draw(img)
        img.save('./pic/'+image)
        d+=1
