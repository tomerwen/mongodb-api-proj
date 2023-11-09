from fastapi import FastAPI
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import youtubesearch
import requests
import json
import credentials
import randomVideo

app= FastAPI()

url = "https://eu-central-1.aws.data.mongodb-api.com/app/data-nbgea/endpoint/data/v1/action/findOne"
payload = json.dumps({
    "collection": "youtubeVideos",
    "database": "listOfVideos",
    "dataSource": "Test-1",
    "projection": {
        "_id": 1
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': credentials.api_key,
}

@app.get("/")
async def root():
    return {"message" : "Hello world"}

@app.get("/search/{search_tag}")
async def search(search_tag: str):
    response = youtubesearch.youtube_search(search_tag)
    return {response}


@app.get("/random")
async def random():
    Video = randomVideo.findRandomVideo()
    videoTitle = Video['title']
    videoURL= f"https://www.youtube.com/watch?v={Video['id']}"
    embeded_video = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ videoTitle }} - Embedded Video</title>
</head>
<body>
    <h1>{{ videoTitle }}</h1>
    <iframe width="560" height="315" src="{{ videoURL }}" frameborder="0" allowfullscreen></iframe>
</body>
</html>
    """
    return embeded_video