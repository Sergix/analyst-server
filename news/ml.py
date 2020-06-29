#Import request and parse from urllib so we can request from the api
from urllib import request as req
from urllib import parse
#Import json to manipulate api data
import json
#import os for env vars that hold api-keys
import os

class dataHandler():
  def __init__(self):
        self.url = "https://newsapi.org/v2/"
        self.apiKey = os.environ['org_api_key']