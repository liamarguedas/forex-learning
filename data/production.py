from datetime import datetime
from pathlib import Path
import os
import json
import requests
import pandas

PATH = Path(__file__).parent


class AlphaVantage:
    """todo"""
    def __init__ (self, from_pair, to_pair, training_data=False, timeline="FX_DAILY"):

        self.to_pair = to_pair
        self.from_pair = from_pair
        self.timeline = timeline
        self.training_data = training_data
        self.outputsize = "full" if self.training_data else "compact"
        self.api_key = os.getenv('alpha_vantage')

    @staticmethod
    def export_to_csv(json_file, name):
        """todo"""
        data = pandas.read_json(json_file).T
        data.to_csv(name)

    @staticmethod
    def log_metadata(source_metadata: dict, path: Path ):

        """todo"""
        now = datetime.now()
        file_name = now.strftime("%d-%m-%Y-%H%M%S") + ".txt"

        with open(path / file_name, "a", encoding="utf-8") as log_file:
            for key in source_metadata.keys():
                log_file.write(f'{key.split(".")[1][1:]}: {source_metadata[key]}\n')

    def retrieve_data(self):
        """todo"""
        function_call = f"function={self.timeline}"
        from_symbol_call = f"&from_symbol={self.from_pair}"
        to_symbol_call = f"&to_symbol={self.to_pair}"
        api_key_call = f"&apikey={self.api_key}"
        data_amount = f"&outputsize={self.outputsize}"
        api_call = "https://www.alphavantage.co/query?"
        response = requests.get(
            api_call + function_call + from_symbol_call + to_symbol_call + api_key_call + data_amount,
            timeout=10
        )
        return response.json()


    def create_data(self):
        """todo"""
        data = self.retrieve_data()
        now = datetime.now()

        file_name = f"{self.from_pair}{self.to_pair}" + now.strftime("%d-%m-%Y %H-%M-%S")

        save_path = PATH / "train" if self.training_data else PATH / "prod"

        json_file = file_name + ".json"
        csv_file = file_name + ".csv"

        self.log_metadata(data['Meta Data'], save_path / "logs")

        with open(save_path / "json" / json_file , "a", encoding="utf-8") as file:
            json.dump(data["Time Series FX (Daily)"], file)

        self.export_to_csv(save_path / "json" / json_file, save_path / "csv" / csv_file)

    def get(self):
        """todo"""
        self.create_data()
