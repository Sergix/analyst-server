from flask import Flask, render_template, request, abort
from flask_cors import CORS
# from search_api_handler import SearchApi
from beta_search_api_handler import tickerHandler
from stock_api_handler import StockApi
import news.handler as news
# import news.ml as news_data_set
# from web_scraper import webScraper as wb
import yfinance as yf
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
  if request.method == "GET":
    t = request.args['ticker']
    try:
      return tickerHandler().fetchData(t)
    except OSError as err:
        print(err)
        return abort(404, description="Failed to compute")
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

@app.route('/ml-news-data-set/')
def data_set():
  if request.method == "GET":
    #our ticker aka stock letter
    #t = request.args['ticker']
    return abort(404, description="The Requested Resource is not Available.")
  else:
    abort(400)

# @app.route('/scrape/')
# def scrape_data():
#   if request.method == "GET":
#     return wb().scrape()
#   else:
#     abort(400)

@app.route('/analyst-report/')
def report():
  t = request.args['ticker']
  test = yf.Ticker(t)
  return json.dumps(
    {
      "name": test.info["longName"],
      "BusinessSummary": test.info["longBusinessSummary"], 
      "employees": test.info["fullTimeEmployees"],
      "sector": test.info["sector"],
      "volume": test.info["volume"],
      "open": test.info["open"],
      "high": test.info["fiftyTwoWeekHigh"],
      "low": test.info["fiftyTwoWeekLow"],
      "close": test.info["previousClose"],
      "dividend": test.info["dividendRate"],
      "marketCap": test.info["marketCap"]
    }, indent=2)

if __name__ == "__main__":
  app.run()
