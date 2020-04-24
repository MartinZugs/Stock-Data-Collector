import sys
from data_handler import DataHandler

''' 
This method takes any of the input provided in the command line and sanatizes, parses, and returns it       
'''
def parse_data():
    # Setting variables from command line arguements 
    ticker_symbol = sys.argv[1]
    api_key = sys.argv[2]

    return ticker_symbol, api_key

ticker_symbol, api_key = parse_data()

dh = DataHandler(ticker_symbol, api_key)

