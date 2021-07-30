import pymongo
import json
import os

class tickerHandler():
   def __init__ (self):
      self.data = {}
      self.sortedData = []

   def fetchData(self, ticker, limit=15):
      mongoKey = os.environ.get('mongo_key')
      client = pymongo.MongoClient("mongodb+srv://admin:" + mongoKey + "@main.u7pjf.mongodb.net/Main?retryWrites=true&w=majority")
      db = client["app"]
      mycol = db["stocks"]
      data = mycol.find({ "$text": { "$search": str(ticker) } }, 
                        { "_id": 0, "symbol": 1, "name": 1 })
      return json.dumps( { "ticker_data": list(data) }, indent=2)