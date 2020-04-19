from flask import Flask, render_template, request, abort
from flask_cors import CORS
from search_api_handler import SearchApi
from stock_api_handler import StockApi
from news.nyt import handler as org



app = Flask(__name__)
CORS(app)

@app.route("/stockQuery/")
def stock_query():
  #if client requesting data -get- 
  if request.method == "GET":
    stockApi = StockApi()
    #our ticker aka stock letter
    ticker = request.args['ticker']
    #period tag
    period = request.args.get('period')
    #interval tag
    interval = request.args.get('interval')
    #call api and return data
    if(interval) and (period):
      return(stockApi.request_data(ticker, period, interval))
    else:
      return(stockApi.request_data(ticker))
  else:
    #abort bad request
    abort(400)
    
@app.route("/searchQuery/")
def search_query():
  #if client requesting data -get- 
  if request.method == "GET":
    searchApi = SearchApi()
    #our ticker aka stock letter
    keyword = request.args['ticker']
    return(searchApi.search_data(keyword))
  else:
    #abort bad request
    abort(400)
@app.route("/newsQuery/")
def news_query():
  #if client requesting data -get- 
  if request.method == "GET":
    newsApi = org.NewsApi()
    #our ticker aka stock letter
    t = request.args['ticker']
    #our data language return type
    l = request.args.get('language')
    #return api data
    if(l == None) or (type(l) != "String"):
      return(newsApi.autoQuery(t, "en"))
    else:
      return(newsApi.autoQuery(t,l))
  else:
    #abort bad request
    abort(400)
if __name__ == "__main__":
  app.run()
