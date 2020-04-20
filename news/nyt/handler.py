# This python script handles news api request
#created 4/19/2020
# Last Updated: 4/19/2020
# Credits:nóto

#Import request and parse from urllib so we can request from the api
from urllib import request as req
from urllib import parse
#Import json to manipulate api data
import json
#import os for env vars that hold api-keys
import os

class NewsApi():
    def __init__(self):
        self.url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"
        self.apiKey = os.environ['nyt_api_key']
    
    def createQuery(self, ticker):
        self.queryParam = {
            "q":str(ticker),
            "api-key": str(self.apiKey)           
        }
        self.parseQuery()
    #END

    def parseQuery(self):
        #parse the api paramaters
        self.queryParam = parse.urlencode(self.queryParam)
        #create the api url query string
        self.query = self.url + self.queryParam
        print(self.query)
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
        self.new_json = {
            'articles': []
        }

        if(len(self.json['response']['docs']) > 5):
            for i in range(5):
                self.update_data(i)
            self.json = self.new_json
        else:
            for i in range(len(self.json['response']['docs'])):
                self.update_data(i)
            self.json = self.new_json

    def update_data(self, index):
        try:
            self.new_json['articles'].append({
                'title': self.json['response']['docs'][index]['abstract'],
                'timestamp': self.json['response']['docs'][index]['pub_date'],
                'content': self.json['response']['docs'][index]['lead_paragraph'],
                'url': self.json['response']['docs'][index]['web_url'],
                'urlImage':"https://www.nytimes.com/" + self.json['response']['docs'][index]['multimedia'][27]['url']
            })
        except:
            self.new_json['articles'].append({
                'title': self.json['response']['docs'][index]['abstract'],
                'timestamp': self.json['response']['docs'][index]['pub_date'],
                'content': self.json['response']['docs'][index]['lead_paragraph'],
                'url': self.json['response']['docs'][index]['web_url'],
                'urlImage':''
            })
    #to make life easy :)
    def autoQuery(self, t):
        self.createQuery(t)
        self.retrieveQuery()
        self.format_data()
        return(self.json)
    #END
