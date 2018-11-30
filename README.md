# mini_Project3
GoogleAPI.py is used to analyse each images downloaded from twitter account, and print labels on the images. Also, the twitter account name and labels would be saved in the database.


tweepyAPI.py is used to download images from twitter account. And the twitter account name and the number of images would be saved into the database.


ffmpegComm.py is used to convert images into a video.


sqlAPI.py and mgAPI.py both implement the method to search account by label and find out the top 5 labels in MongoDB and MySQL. 

## MySQL Database:

CREATE TABLE img(
    -> imgid INT NOT NULL AUTO_INCREMENT,
    -> twitterID VARCHAR(40),
    -> labels VARCHAR(20),
    -> PRIMARY KEY (imgid)
    -> );
    
CREATE TABLE tweetid(
    -> id INT NOT NULL AUTO_INCREMENT,
    -> twitterID VARCHAR(40),
    -> img_num INT,
    -> PRIMARY KEY (id)
    -> );


## MongoDB Database:
client = pymongo.MongoClient("mongodb://localhost:27017/")


db = client["proj3"]


tableid = db["tweetid"]


table_label = db["img_label"]
