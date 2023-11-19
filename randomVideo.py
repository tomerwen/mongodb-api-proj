import credentials
from pymongo import MongoClient
from pymongo.server_api import ServerApi

apiPassword = credentials.password
client = MongoClient("mongodb://mongo-service:27017/")
db = client["youtubeVideos"]
collection = db["listOfVideos"]

def findRandomVideo(): #will return id,channelId,title,description,channelTitle,publishTime
    pipeline = [{"$sample": {"size": 1}}]
    result = collection.aggregate(pipeline)
    random_video = next(result, None)
    return random_video

findRandomVideo()