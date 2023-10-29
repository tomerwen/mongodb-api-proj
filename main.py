from fastapi import FastAPI
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import youtubesearch
app= FastAPI()



@app.get("/")
async def root():
    return {"message" : "Hello world"}

@app.get("/test/{search_tag}")
async def test(search_tag: str):
    response = youtubesearch.youtube_search(search_tag)
    return {"test": {response}}