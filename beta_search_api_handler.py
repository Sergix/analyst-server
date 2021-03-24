import json

class tickerHandler():
   def __init__ (self):
      self.data = {}
      self.sortedData = []

   def fetchData(self, ticker, limit=15):
      with open('search_tikers.json') as json_file:
         self.data = json.load(json_file)["data"]["rows"]
      if(ticker.strip() == "" ):
         for x in range(limit):
            self.sortedData.append({ 'name': self.data[x]['name'], 'symbol': self.data[x]['symbol'] })
      else:
         for i in range(len(self.data)):
            if (len(self.sortedData) <= limit):
               if (ticker.strip().upper() in self.data[i]['name'].upper()[0:len(ticker)]) or (ticker.strip().upper() in self.data[i]['symbol'].upper()[0:len(ticker)]):
                  self.sortedData.append({ 'name': self.data[i]['name'], 'symbol': self.data[i]['symbol'] })
      return json.dumps({ 'ticker_data': self.sortedData }, indent=2)
