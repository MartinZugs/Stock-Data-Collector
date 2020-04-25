import json
import requests

class DataHandler:

    def __init__(self, ticker_symbols, api_token):
        self.ticker_symbols = ticker_symbols
        self.api_token = api_token

    '''
    This function will use the API to get all of the current metadata for all of the stock tickers provided
    '''
    def get_current_data(self):
        
        data = requests.get(f"https://cloud-sse.iexapis.com/stable/stock/market/batch?symbols={self.ticker_symbols}&types=quote&token={self.api_token}")
        
        return data.json()

    '''
    This function will take the raw response from the API and properly parse it into data that is wanted
    '''
    def data_parsing(self, data):
        
        print(data['AAPL']['quote']['previousVolume'])

        return 0

    '''
    This function will take the raw data and parse through and send only the important parts to the flask API
    '''
    def send_data(self, data):
        
        for ticker in data:
            print(ticker)
            for metadata in data[ticker]['quote']:
                print(metadata)
                print(data[ticker]['quote'][metadata])
                
