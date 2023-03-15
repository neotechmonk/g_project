from candle import Candle


#Instantiate Obbject
# c1 = Candle()
# print(c1)  #<candle.Candle object at 0x1011b25d0>
# c1.ticker='AAPL' #Directly assign attributes

c2 = Candle("BTCSß", 3, 0, 2, 5)
print(c2)
c2.ticker="ztc"
print(c2)
print(list(Candle.all))

csv_candles = Candle.from_csv('price_feed.csv')
print(csv_candles)