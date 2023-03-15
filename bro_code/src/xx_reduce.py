"""
    - Reduce takes two neighboring values from an iterable (e.g. list, dict, etc)
    - Applies a function with two neighboring values from the iterables as arguments (E.g. pos x, x+1)
    - Replaces last position with the return of the function. I.e. pos x+1  = fn(x, x+1)
    - Retpeats above until the there is only only remain value in the interable

"""
from  functools import reduce


nums = [2,3,3,2]
def double (x,x1):
    """
        2*2 = 4
        4*2 = 8
        8*2 = 16

        x becomes x1 and x1 never gets multiplied
    """
    return x*2

doubles = reduce(double, nums)
print(doubles)

cum_sum = reduce(lambda a, b : a+b, nums)
print(cum_sum)


##Array of dictionaries

data = [
    {"name": "Alice", "age": 25, "score": 80},
    {"name": "Bob", "age": 30, "score": 90},
    {"name": "Charlie", "age": 35, "score": 85},
    {"name": "Dave", "age": 40, "score": 95},
    {"name": "Eve", "age": 45, "score": 75}
]

# Calculate the total score
# x=> key e.g. last score defaulting at 0 at the start
# y = next value
# The lambda function takes two arguments, x and y, 
# where x is the accumulated total score so far, and
# y is the current dictionary being processed. We access the "score"
# key of the dictionary and add it to the accumulated total score.


total_score = reduce(lambda x, y: x + y["score"], data, 0)


# Calculate the average score
average_score = total_score / len(data)

print("Average score:", average_score)


#Dot product of two arrayes 
# We use the zip() function to create a list of tuples, 
# where each tuple contains the corresponding components of the two vectors.
# For example, the first tuple would be (1, 4), 
# the second tuple would be (2, 5), and so on.

a = [1, 2, 3]
b = [4, 5, 6]

dot_product = reduce(lambda x, y: x + y[0] * y[1], zip(a, b), 0)

print(dot_product)


#Portfolio Returns
portfolio = [
    {"symbol": "AAPL", "shares": 100, "buy_price": 120.50, "sell_price": 135.25},
    {"symbol": "GOOG", "shares": 50, "buy_price": 1500.00, "sell_price": 1550.75},
    {"symbol": "AMZN", "shares": 75, "buy_price": 3100.00, "sell_price": 3200.50},
    {"symbol": "FB", "shares": 200, "buy_price": 250.00, "sell_price": 275.50},
]

total_return = reduce(lambda x, y: x + ((y["sell_price"] - y["buy_price"]) * y["shares"]), portfolio, 0)

print("Total return:", total_return)