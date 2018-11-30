import pymongo
from collections import Counter
keyword = 'sky'

def searchtweet_mg():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["proj3"]
    table_label = db["img_label"]
    
    accounts = table_label.find({'label':keyword})
    result=[]
    for i in accounts:
        if not i['tweetID'] in result:
            result.append(i['tweetID'])

    print("These twitter account have this label:")
    if result:
        for j in result:
           print(j) 
    else:
        print("No one has this label")
        
def AnalyseTweet_mg():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["proj3"]
    tableid = db["tweetid"]
    table_label = db["img_label"]
    
    result = []
    content = table_label.find()
    for i in content:
        result.append(i['label'])    
    
    print("Highest 5 labels")
    print(Counter(result).most_common(5))

        
if __name__ == '__main__':
    searchtweet_mg()
    AnalyseTweet_mg()

