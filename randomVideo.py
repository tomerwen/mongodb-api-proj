import credentials
from pymongo import MongoClient
from pymongo.server_api import ServerApi

apiPassword = credentials.password
client = MongoClient(f"mongodb+srv://tomerwen:{apiPassword}@test-1.jazb2pv.mongodb.net/?retryWrites=true&w=majority")
db = client["youtubeVideos"]
collection = db["listOfVideos"]

def findRandomVideo():
    pipeline = [{"$sample": {"size": 1}}]
    result = collection.aggregate(pipeline)
    random_video = next(result, None)
    print(random_video['id'])
    return random_video

findRandomVideo()