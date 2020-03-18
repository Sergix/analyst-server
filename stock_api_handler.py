# This python script handles stock api request
# Last Updated: 3/18/2020
# Credits:nóto

#Import request and parse from urllib so we can request from the api
from urllib import request, parse
#Import json to manipulate api data
import json


#create a class to handle our stock api
class ApiHandler:
    def __init__(Self):
        Self.Url = "https://www.alphavantage.co/"
        Self.apikey = "4WXA1UZXP1MVFLPG"
    #END

    #this method creates our api queryurls
    def createQuery(Self, t, r, i=None):
        # t -ticker- is the stock letters
        # r -response type- is the type of request we are going to be making to the api
        # i is the interval 
        # we will assume that all our parameters correct
        Self.Stock = t
        if(r == "points"):
            #We need to return stock points from the api for charting on the front end
            if(i == None):
                i = "5min"
            Self.queryParam = {
                "function":"TIME_SERIES_DAILY_ADJUSTED",
                "symbol":Self.Stock,
                "interval": i,
                "datatype":"json",
                "apikey":Self.apikey
                }

            Self.parseQuery()
            
        #END
        if(r == "stock"):
            #We need to return stock info from the api
            Self.queryParam = {
                "function":"GLOBAL_QUOTE",
                "symbol":Self.Stock,
                "datatype":"json",
                "apikey":Self.apikey
                }
            Self.parseQuery()
            
            #END
        if(r == "search"):
            #We need to search stock letters from the api
             Self.queryParam = {
                "function":"SYMBOL_SEARCH",
                "keywords":Self.Stock,
                "datatype":"json",
                "apikey":Self.apikey
                }
             
             Self.parseQuery()
             
            #END
             
    #END
    
    def parseQuery(Self):
        #parse the api paramaters
        Self.queryParam = parse.urlencode(Self.queryParam)
        #create the api url query string
        Self.query = Self.Url + "query?" + Self.queryParam
    #END
        
    def retrieveQuery(Self):
        #query the srtring and the store api's response
        Self.apiResp = request.urlopen(Self.query)
        #if connection is connected
        if(Self.apiResp.isclosed() == False):
            #Store json Data
            Self.queryData = json.load(Self.apiResp)
        else:
            raise ValueError('Error: Api Connection Failed')
