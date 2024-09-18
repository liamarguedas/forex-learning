import investpy
import yfinance as yf


class pair_data:

    def __init__(self, source=None, pair: str, from: str, to: str, ):
        self.pair = pair
        self.from = from
        self.to = to
        self.source = source

    def investpy(self):
        return investpy.get_currency_cross_historical_data(currency_cross=self.pair, from_date=self.from, to_date=self.to)

    def yfinance(self):
        return yf.Ticker(f"{self.pair}=X").history(period="max")

    def fetch(self):
        if source == "yfinance":
            return self.yfinance()
        else: # change statement if more needed
            return self.investpy()

    def fetch_available(self):
        if self.source is not None:
            return self.fetch()
        
        try:
            return self.yfinance()
        
        except:
            return self.investpy()
        
        
        
        

        
