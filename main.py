from fastapi import FastAPI
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import youtubesearch
import requests
import json
import credentials


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