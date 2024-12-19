from pathlib import Path
import pandas

PATH = Path(__file__).parents[1]

class UtilityPipelines:
    """todo"""

    def __init__(self) -> None:
        self.training_path = PATH / "data" / "train"
        self.production_path = PATH / "data" / "prod"

    @staticmethod
    def load_csv(csv):
        """todo"""

        try:
            temp = pandas.read_csv(csv)
            temp.rename( columns={'Unnamed: 0':'date',
                                  '1. open': 'open',
                                  '2. high':'high',
                                  '3. low':'low',
                                  '4. close':'close'}, inplace=True )

            print(f"Data range: {temp.iloc[-1]["date"]} to {temp.iloc[0]["date"]}")

            return temp

        except Exception as e:
            return e

    @staticmethod
    def last_modified_file(folder_path: Path):
        """todo"""

        folder_files = list(folder_path.iterdir())

        if folder_files is None:
            raise FileNotFoundError(f"No files found in {folder_path}.")

        folder_files.sort(key=lambda file: file.stat().st_mtime, reverse=True)

        return folder_files[0]

    def get_lastest_train_data(self):
        """todo::"""
        last_file = self.last_modified_file(self.training_path / "csv")
        return self.load_csv(last_file)
