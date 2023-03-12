#If elif, else
x = 10
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")

#Nested conditions
x = 10
if x > 5:
    if x < 15:
        print("x is between 5 and 15")
    else:
        print("x is greater than or equal to 15")
else:
    print("x is less than or equal to 5")
