from fastapi import FastAPI, Request
import youtubesearch
import json
import credentials
import randomVideo
from fastapi.templating import Jinja2Templates
from html import unescape


app = FastAPI()
templates = Jinja2Templates(directory="templates")

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
async def random(request: Request):
    Video = randomVideo.findRandomVideo() #gets id,channelId,title,description,channelTitle,publishTime
    videoTitle = unescape(Video['title'])
    VideoID = "test"
    videoURL= f"https://www.youtube.com/embed/{VideoID}"
    return templates.TemplateResponse(f"embedVideo.html", {"request": request, "videoTitle": videoTitle, "videoURL": 'https://www.youtube.com/watch?v=nscKKYbZpsE&ab_channel=AddictedtoAmericanDad'})