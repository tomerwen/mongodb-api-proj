import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import credentials

DEVELOPER_KEY = credentials.api_key
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
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
      video_details = { 'videos': [ {
        'id':search_result['id']['videoId'],
        'channedId':search_result['snippet']['channelId'],
        'title':search_result['snippet']['title'],
        'description':search_result['snippet']['description'],
        'channelTitle':search_result['snippet']['channelTitle'],
        'publishTime':search_result['snippet']['publishTime'] }]
      }
      videos.append(video_details)
  print(videos)
  return str(videos)