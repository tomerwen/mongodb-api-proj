import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import credentials
from pymongo import MongoClient
from pymongo.server_api import ServerApi


apiPassword = credentials.password
client = MongoClient(f"mongodb+srv://tomerwen:{apiPassword}@test-1.jazb2pv.mongodb.net/?retryWrites=true&w=majority")
db = client["youtubeVideos"]
collection = db["listOfVideos"]

def youtube_search(options):  #start search with youtube api
  youtube = build('youtube', 'v3',
    developerKey=credentials.api_key)

  # Call the search.list method to retrieve results matching the specified query term.
  search_response = youtube.search().list(
    q=options,
    maxResults=10,
    part='id,snippet',
  ).execute()

  videos = []

  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append('%s (%s)' % (search_result['snippet']['title'],
                                 search_result['id']['videoId']))
      video_details = {
        'id':search_result['id']['videoId'],
        'channedId':search_result['snippet']['channelId'],
        'title':search_result['snippet']['title'],
        'description':search_result['snippet']['description'],
        'channelTitle':search_result['snippet']['channelTitle'],
        'publishTime':search_result['snippet']['publishTime'] 
      }
      print(search_result)
      if video_details['id'] not in [doc['id'] for doc in collection.find()]:
          collection.insert_one(video_details)
          print(f"added {video_details} to {collection}")
      videos.append(video_details)
  return str(videos)