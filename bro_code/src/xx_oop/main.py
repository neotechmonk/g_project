from candle import Candle
"""
    TODO : Inheritance demo
"""

#Instantiate Obbject
# c1 = Candle()
# print(c1)  #<candle.Candle object at 0x1011b25d0>
# c1.ticker='AAPL' #Directly assign attributes

##Create a single Candle
c2 = Candle("BTC", 3, 0, 2, 5)
print(c2) #Inspect. Note Mutated descriptor

c3 = Candle("ADA", 3, 0, 2, 5)

#Change the candle name through the setter method
c2.ticker="ztc"
print(c2) #Note Mutated descriptor

#Print the collection of candles created so far - c2, c3
print(list(Candle.all))  #Note that __repr__ vs __str__ formatting


#Create candles based on the a CSV File
# Note that c2, c3 are still present due to 
print('---------------------')
csv_candles = Candle.from_csv('price_feed.csv')
print(csv_candles)