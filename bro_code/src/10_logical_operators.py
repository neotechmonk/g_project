"""
and - all conditions  
or - at least one of the  conditions

"""

a, b = 5, 4


if (a == 5 and b == 4): 
    print(f"a == 5 and b == 4")

elif (a == 5 or b == 0): ## b == 0 is False
    print(f"a == 5 and b == 0")


if not(a is None and b is None ):
    print (f"{a} and {b} are not None")