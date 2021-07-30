import pymongo
import json

class tickerHandler():
   def __init__ (self):
      self.data = {}
      self.sortedData = []

   def fetchData(self, ticker, limit=15):
      client = pymongo.MongoClient("mongodb+srv://admin:Soccer121$@main.u7pjf.mongodb.net/Main?retryWrites=true&w=majority")
      db = client["app"]
      mycol = db["stocks"]
      data = mycol.find({ "$text": { "$search": str(ticker) } }, 
                        { "_id": 0, "symbol": 1, "name": 1 })
      return json.dumps( { "ticker_data": list(data) }, indent=2)