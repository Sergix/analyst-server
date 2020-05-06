# This python script handles stock api request from yfinance
# Last Updated: 4/7/2020
# Credits:nóto

#Import yfinance api lib
import yfinance as yf
#Import pandas lib
import pandas as pd
#Import json to manipulate api data
import json
#Import math
import math

class StockApi():
    def __init__(self):
        self.panda = pd

    def request_data(self, t, p='1d', i="5m"):
        #set the stock we would like to search for
        stock = yf.Ticker(t)
        #Retrieve data and store as Panda Data Frame
        self.unclean_data = stock.history(period=p,interval=i)
        print(self.unclean_data)
        #unclean_data selectors stored in an array
        self.data_selectors = list(self.unclean_data.columns)
        #create list of the index values which the  values are equal to the time stamps of our data
        self.time_stamps = list(self.unclean_data.index)
        #get the length
        self.time_stamp_total_length = len(self.time_stamps)
        #now let us clean the data
        self.clean_data()
        #lets convert the data  and return it back to what ever called us
        return self.convert_data()
    #END
    
    #function to organize 'clean' the stock data
    def clean_data(self):
        #function to clean panda data returned by Api
        #
        self.new_data = {

            }
        for count in range(self.time_stamp_total_length):
            #get the next timestamp and store it as a string
            self.new_time_stamp = str(self.time_stamps[count])
            #insert new data here
            if(not math.isnan((self.unclean_data.iloc[count].to_list())[0])):
                self.new_data.update({self.new_time_stamp:self.unclean_data.iloc[count].to_list()})
        #return the new data
        return self.new_data
    #END
    
    #function to convert the data so the front end can read it
    def convert_data(self):
        self.new_data = json.dumps(self.new_data, indent=2)
        #print(self.new_data)
        return self.new_data
    #END
