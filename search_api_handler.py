# This python script handles stock search api request
#created 4/8/2020
# Last Updated: 4/8/2020
# Credits:nóto

#Import request and parse from urllib so we can request from the api
from urllib import request as req
from urllib import parse
#Import json to manipulate api data
import json

class SearchApi():
    def __init__(self):
        #create static url
        self.url = "https://ticker-2e1ica8b9.now.sh/keyword/"
    #END
    def search_data(self, keyword):
        self.query = self.url + keyword
        #query the srtring and the store api's response
        self.apiResp = req.urlopen(self.query)
        #if connection is connected
        if(self.apiResp.isclosed() == False):
            #Store json Data
            self.json = json.load(self.apiResp)
        else:
            raise ValueError('Error: Api Connection Failed')
        #return the data cleaned
       
        return self.json
    #END
    def clean_data(self):
        #create a dictionary to store new data 
        self.new_data = {}
        #loop over the array sent back by the api
        for i in self.json:
            #add data to our new dictionary
            self.new_data.update({i['symbol']:i['name']})
        #return that data
        return self.new_data
    #END
