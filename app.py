from flask import Flask, render_template, request, abort
from stock_api_handler import ApiHandler
from news_api_handler import NewsApi 

app = Flask(__name__)


@app.route("/stockQuery/")
def stock_query():
  #if client requesting data -get- 
  if request.method == "GET":
    stockApi = ApiHandler()
    #our ticker aka stock letter
    t = request.args['ticker']
    #our query type 
    f = request.args['request']
    #optional query interval
    i = request.args.get('interval')
    #return api data
    return(stockApi.autoQuery(t,f,i))
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
      return("<pre style='word-wrap: break-word; white-space: pre-wrap;'>" + newsApi.autoQuery(t, "en") +  "</pre>")
    else:
      return("<pre style='word-wrap: break-word; white-space: pre-wrap;'>" + newsApi.autoQuery(t,l) +  "</pre>")
  else:
    #abort bad request
    abort(400)
if __name__ == "__main__":
  app.run()
