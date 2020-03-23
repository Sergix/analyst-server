# This python script handles stock api request
# Last Updated: 3/18/2020
# Credits:nóto

#Import request and parse from urllib so we can request from the api
from urllib import request as req
from urllib import parse
#Import json to manipulate api data
import json


#create a class to handle our stock api
class ApiHandler:
    def __init__(self):
        self.Url = "https://www.alphavantage.co/"
        self.apikey = "4WXA1UZXP1MVFLPG"
    #END

    #this method creates our api queryurls
    def createQuery(self, t, r, i=None):
        # t -ticker- is the stock letters
        # r -response type- is the type of request we are going to be making to the api
        # i is the interval 
        # we will assume that all our parameters correct
        self.function = r
        self.Stock = t
        if(r == "points"):
            #We need to return stock points from the api for charting on the front end
            if(i == None):
                i = "5min"
            self.queryParam = {
                "function":"TIME_SERIES_DAILY_ADJUSTED",
                "symbol":self.Stock,
                "interval": i,
                "datatype":"json",
                "apikey":self.apikey
                }

            self.parseQuery()
            
        #END
        elif(r == "stock"):
            #We need to return stock info from the api
            self.queryParam = {
                "function":"GLOBAL_QUOTE",
                "symbol":self.Stock,
                "datatype":"json",
                "apikey":self.apikey
                }
            self.parseQuery()
            
            #END
        elif(r == "search"):
            #We need to search stock letters from the api
             self.queryParam = {
                "function":"SYMBOL_SEARCH",
                "keywords":self.Stock,
                "datatype":"json",
                "apikey":self.apikey
                }
             
             self.parseQuery()
        else :
            raise ValueError('Error: Incorrect Handler Request Method')
            #END
    #END
    
    def parseQuery(self):
        #parse the api paramaters
        self.queryParam = parse.urlencode(self.queryParam)
        #create the api url query string
        self.query = self.Url + "query?"+ self.queryParam
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
        #clean Json and return Data
        self.cleanJson(len(self.json))   
    def cleanJson(self, a=1):
        self.data = {
                self.function:{
                        #We will update-insert- data here
                    }
             }
        if a == 2:
            #There is meta data let's get ride of it and clean our json
            #loop over json keys
            for i in self.json[(list(self.json)[1])]:
                #create final result
                self.data[self.function].update(
                    {
                        #We will fix this later lol
                         i:list(((self.json[(list(self.json)[1])])[i]).values())
                    })
            return(self.data)
        elif a == 1 and self.function == "stock":
            #There is no meta data but, we need to clean our json
            #loop counter
            loop_count = 0
            #loop over json keys
            for i in self.json[list(self.json)[0]]:
                #create final result
                self.data[self.function].update(
                    {
                        #We will fix this later lol
                        (str(i)[4:]):list(api.json[(list(api.json)[0])].values())[loop_count]
                     })
                loop_count += 1
        elif a == 1 and self.function=="search":
             #There is no meta data but, we need to clean our json
            #loop over json keys
            for i in self.json[list(self.json)[0]]:
                self.data[self.function].update(
                    {
                        #We will fix this later lol
                        (i[(list(i)[0])]):list(i.values())
                    })
        else:
            return  ValueError('Error: query_json was incorrectly structured')
            
        #END
    #make life easy :)
    def autoQuery(self, t, f, i="5min"):
        #create our query URL
        self.createQuery(t,f,i)
        #fetch data
        self.retrieveQuery()
        #return data
        return(json.dumps(self.data, indent=2))
        #END
    #END
