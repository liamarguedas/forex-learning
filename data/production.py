import os
import json
import requests
import pandas
from datetime import datetime
from pathlib import Path

class AlphaVantage:
    def __init__ (self, from_pair, to_pair, timeline="FX_DAILY"):

        self.to_pair = to_pair
        self.from_pair = from_pair
        self.timeline = timeline
        self.api_key = os.getenv('alpha_vantage')

    @staticmethod
    def log_metadata(source_metadata: dict):

        """todo"""
        logs_dir = Path(__file__).parent / "logs"
        now = datetime.now()
        file_name = now.strftime("%d-%m-%Y-%H%M%S") + ".txt"

        with open(logs_dir / file_name, "a", encoding="utf-8") as log_file:
            for key in source_metadata.keys():
                log_file.write(f'{key.split(".")[1][1:]}: {source_metadata[key]}\n')

    def retrieve_data(self):
        """todo"""
        function_call = f"function={self.timeline}"
        from_symbol_call = f"&from_symbol={self.from_pair}"
        to_symbol_call = f"&to_symbol={self.to_pair}"
        api_key_call = f"&apikey={self.api_key}"
        api_call = "https://www.alphavantage.co/query?"
        response = requests.get(
            api_call + function_call + from_symbol_call + to_symbol_call + api_key_call,
            timeout=10
        )
        return response.json()


    def convert_to_table(self):
        """todo"""

        data = self.retrieve_data()
        self.log_metadata(data['Meta Data'])
        
               # 'Time Series FX (Daily)':
                # {'2024-12-06': {'1. open': '1.05846', '2. high': '1.06298', '3. low': '1.05419', '4. close': '1.05680'},
        with open(Path(__file__).parent / "test.csv", "a", encoding="utf-8") as file:
            json.dump(data["Time Series FX (Daily)"], file)



    def get(self):
        """todo"""
        self.convert_to_table()
