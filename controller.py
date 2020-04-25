import sys
from data_handler import DataHandler

''' 
This method takes any of the input provided in the command line and sanatizes, parses, and returns it       
'''
def parse_data():
    # Setting variables from command line arguements 
    ticker_symbols = sys.argv[1]
    api_key = sys.argv[2]

    return ticker_symbols, api_key

ticker_symbols, api_key = parse_data()

dh = DataHandler(ticker_symbols, api_key)

raw_data = dh.get_current_data()

clean_data = dh.send_data(raw_data)

