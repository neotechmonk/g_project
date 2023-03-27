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


dict1 = {'a': 10, 'b': 20, 'c': 30}
print(f"--All values  > 5 {all(val > 5 for val in dict1.values())}")



list2 = [1, 2, 'three', 4, 5]
print (f"All are ints : {all(isinstance(val, int) for val in list2)}")

# any
my_list = [False, False, True, False]

if any(my_list):
    print("At least one element in the list is True")
else:
    print("No elements in the list are True")

list1 = [1, 2, 3, 4, 5]
print(f"**At least one value is > 5 {any(val > 5 for val in list1)}")


list3 = ['hello', 'world', 'python']
string1 = 'hello python!'

print(f"at least one of {list3} is in {string1} : {any(val in string1 for val in list3)}")
