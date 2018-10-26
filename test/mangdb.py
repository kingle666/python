import pymongo
client = pymongo.MongoClient("172.16.1.161",port=27017)
db = client.zhihu
collection = db.qa
# collection.insert({"username":"aaa"})
cursor = collection.find()
print (cursor)