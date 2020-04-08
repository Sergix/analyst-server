from flask import Flask, render_template, request, abort
from flask_cors import CORS
from stock_api_handler import StockApi
from news_api_handler import NewsApi 

app = Flask(__name__)
CORS(app)

@app.route("/stockQuery/")
def stock_query():
  #if client requesting data -get- 
  if request.method == "GET":
    stockApi = StockApi()
    #our ticker aka stock letter
    t = request.args['ticker']
    return(stockApi.request_data(t))
  else:
    #abort bad request
    abort(400)

@app.route("/newsQuery/")
def news_query():
  #if client requesting data -get- 
  if request.method == "GET":
    newsApi = NewsApi()
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
