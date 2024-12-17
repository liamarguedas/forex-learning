from data import AlphaVantage

def main():

    data = AlphaVantage(from_pair="EUR", to_pair="USD")
    data.get()

if __name__ == "__main__":

    main()
