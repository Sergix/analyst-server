from flask import Flask, render_template, request, abort
from flask_cors import CORS
from search_api_handler import SearchApi
from stock_api_handler import StockApi
import news.handler as news
import json



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
    try:
      if(interval) and (period):
        return(stockApi.request_data(ticker, period, interval))
      else:
        return(stockApi.request_data(ticker))
    except OSError as err:
      print(err)
      return abort(404, description="Failed to compute")
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
    try:
      return(searchApi.search_data(keyword))
    except OSError as err:
      print(err)
      return abort(404, description="Resource not found")
  else:
    #abort bad request
    abort(400)
@app.route("/newsQuery/")
def news_query():
  #if client requesting data -get- 
  if request.method == "GET":
    newsApi = news
    #our ticker aka stock letter
    t = request.args['ticker']
    #our data language return type
    try:
      return(newsApi.newsQuery(t))
    except OSError as err:
      print(err)
      return abort(404, description="Resource not found")
  else:
    #abort bad request
    abort(400)
    
    
if __name__ == "__main__":
  app.run()
