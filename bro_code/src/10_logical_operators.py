"""
and - all conditions  
or - at least one of the  conditions

additional for collections 
    - any - some 
    - all  - all 

"""

a, b = 5, 4


if (a == 5 and b == 4): 
    print(f"a == 5 and b == 4")

elif (a == 5 or b == 0): ## b == 0 is False
    print(f"a == 5 and b == 0")


if not(a is None and b is None ):
    print (f"{a} and {b} are not None")




# all

my_list = [True, False, True, True]

if all(my_list):
    print("All elements in the list are True")
else:
    print("Not all elements in the list are True")

# any
my_list = [False, False, True, False]

if any(my_list):
    print("At least one element in the list is True")
else:
    print("No elements in the list are True")

