import pymysql
keyword = 'sky'
password = ''

def searchtweet():
    db = pymysql.connect("localhost","root", password,"proj");
    cursor = db.cursor()
        
    sql = 'SELECT twitterID FROM img WHERE labels like "%{}%"'.format(keyword)
    cursor.execute(sql)
    accounts = cursor.fetchall()
    result=[]
    for i in accounts:
        if not i in result:
            result.append(i)

    print("These twitter account have this label:")
    if result:
        for j in result:
           print(j[0]) 
    else:
        print("No one has this label")

def AnalyseTweet():
    db = pymysql.connect("localhost","root", password,"proj");
    cursor = db.cursor()
    sql = 'SELECT labels,count(*) FROM img GROUP BY labels order by count(*) desc limit 5'
    
    cursor.execute(sql)
    top_label = cursor.fetchall()#top 5 numbers of label

    print("Highest 5 labels")
    print(top_label)
    
if __name__ == '__main__':
    searchtweet()
    AnalyseTweet()
