from pymongo import MongoClient

conn=MongoClient('localhost',27017)

db=conn.rnews

collectionNewsapi=db.news

collectionNewscatcher=db.news

def checkSimilarNewsapi(title):
    result=collectionNewsapi.find_one({"title":title,"technology":"newsapi"})
    
    if result is None:
        return True
    else:
        return False


def checkSimilarNewsCatcher(title):
    result=collectionNewscatcher.find_one({"title":title,"technology":"newscatcher"})
    
    if result is None:
        return True
    else:
        return False




