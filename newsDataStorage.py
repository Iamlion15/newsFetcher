from pymongo import MongoClient;
from pymongo.errors import WriteError

conn=MongoClient('localhost',27017)

db=conn.rnews
collectionNewsapi=db.news
collectionNewscacther=db.news

def saveNewsapiData(source,title,description,summary,publishedAt,url,sentiment):
    data={
        "technology":"newsapi",
        "source":source,
        "title":title,
        "summary":summary,
        "description":description,
        "publishedAt":publishedAt,
        "url":url,
        "sentiment":sentiment
        }
    
    try:
       result = collectionNewsapi.insert_one(data).inserted_id
       return result
    except WriteError as e:
        return 0
    

def saveNewscatcherData(source,title,summary,publishedAt,url,sentiment):
    data={
        "technology":"newscatcher",
        "source":source,
        "title":title,
        "summary":summary,
        "publishedAt":publishedAt,
        "url":url,
        "sentiment":sentiment
        }
    
    try:
       result = collectionNewscacther.insert_one(data).inserted_id
       return result
    except WriteError as e:
        return 0    
