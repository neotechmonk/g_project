import csv

class Candle:
    """
    Demonstrate
        - Object attributes
        - Object methods
        - Contructor  (__init__)
        - Class attribute
        - Class methods
        - Object vs Class property hierarchy
        - Static method
        - __repr__ override
    """

    #Class variable to hold a colleciton of candles
    all = list()

    #Default Class level attribute changed by `ticker` setter
    __is_modified: bool = False

    # Static method to format a ticker string
    # Lambda functions that are class methods are already static methods
    # Cannot explictly decorate them as static methods
    format_ticker = lambda t: t.lower()


    #Constructor 
    def __init__(
        self, 
        ticker: str, 
        open: float, 
        high: float, 
        low: float, 
        close: float
    ) -> None:
        

        #Validate attributes
        assert ticker is not None and ticker != "", "Ticker cannot be empty"
        assert all(x > -1 for x in [open, high, low, close]), "OHLC prices must be > 0"

        #Initialise instance attributes to be private attributes to make them immuntable
        # only ticker is mutable with @property and @setter 
        self.__open = open
        self.__close = close
        self.__high = high
        self.__low = low
        self.__ticker = Candle.format_ticker(ticker)

        #add the candle to collection
        Candle.all.append(self)

    #For system debugging 
    def __repr__(self):
        return f"Candle({self.__ticker}, {self.__open}, {self.__high}, {self.__low}, {self.__close})"

    #Human readable 
    def __str__(self):
        return f"Candle({self.__ticker}, Open:{self.__open}, High:{self.__high}, Low:{self.__low}, Close:{self.__close}, Mutated: {self.__is_modified})"

    #load candles from csv price feed
    @classmethod
    def from_csv(cls, csv_path: str):
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            candles = [
                Candle(
                    row['ticker'], 
                    float(row['open']), 
                    float(row['high']),
                    float(row['low']), 
                    float(row['close'])
                )
                for row in reader
            ]
            Candle.all.extend(candles)
        return Candle.all

    @property
    def ticker(self):
        return self.__ticker
    
    @ticker.setter
    def ticker(self, new_ticker):
        self.__ticker = Candle.format_ticker(new_ticker)
        self.__is_modified = True
