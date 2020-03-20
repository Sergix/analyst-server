from flask import Flask, render_template, request, abort
from stock_api_handler import ApiHandler

app = Flask(__name__)


@app.route("/stockQuery/")
def client_side_query():
  #if client requesting data -get- 
  if request.method == "GET":
    api = ApiHandler()
    #our ticker aka stock letter
    t = request.args['ticker']
    #our query type 
    f = request.args['request']
    #optional query interval
    i = request.args.get('interval')
    #return api data
    return(str(api.autoQuery(t,f,i)))
  else:
    #abort bad request
    abort(400)

if __name__ == "__main__":
  app.run()
