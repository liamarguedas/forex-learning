from data import AlphaVantage

def main():
    """todo"""

    data = AlphaVantage(from_pair="EUR", to_pair="USD", training_data=True)
    data.get()

if __name__ == "__main__":

    main()
