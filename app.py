# Main -Brain- Backend Code for Analyst 
from flask import Flask, request
import stock_api_handler

#create Flask instance
app = Flask(__name__)

@app.route('/')
def on_request():
    #here we will handle all of our request
