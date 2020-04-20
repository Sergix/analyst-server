# This python script handles news api request
#created 4/19/2020
# Last Updated: 4/19/2020
# Credits:nóto


#Import request and parse from urllib so we can request from the api
from urllib import request as req
from urllib import parse
#Import json to manipulate api data
import json
#import os for env vars that hold api keys
import os

class NewsApi():
    def __init__(self):
        self.url = "https://newsapi.org/v2/"
        self.apiKey = os.environ['org_api_key']
    
    def createQuery(self, ticker, lan):
        self.queryParam = {
            "q":str(ticker) + " Stock",
            "language": lan,
            "apikey": str(self.apiKey)           
        }
        self.parseQuery()
    #END

    def parseQuery(self):
        #parse the api paramaters
        self.queryParam = parse.urlencode(self.queryParam)
        #create the api url query string
        self.query = self.url + "everything?" + self.queryParam
    #END

    def retrieveQuery(self):
        #query the srtring and the store api's response
        self.apiResp = req.urlopen(self.query)
        #if connection is connected
        if(self.apiResp.isclosed() == False):
            #Store json Data
            self.json = json.load(self.apiResp)
        else:
            raise ValueError('Error: Api Connection Failed')
    #END
    def format_data(self):
      data = self.json["articles"]
      data_json = {
          'articles': []
        }

      if(len(data) > 20):
          for i in range(20):
            data_json['articles'].append({
              'title': (data[i])['title'],
              'content': (data[i])['description'],
              'url': (data[i])['url'],
              'urlImage':(data[i])['urlToImage'],
              'timestamp': (data[i])['publishedAt']
            })
      else:
          for i in range(len(data)):
            data_json['articles'].append({
              'title': (data[i])['title'],
              'content': (data[i])['description'],
              'url': (data[i])['url'],
              'urlImage':(data[i])['urlToImage'],
              'timestamp': (data[i])['publishedAt']
            })
            
          self.json = data_json
    #END
    #to make life easy :)
    def autoQuery(self, t, lang):
        self.createQuery(t, lang)
        self.retrieveQuery()
        self.format_data()
        return(self.json)
    #END
