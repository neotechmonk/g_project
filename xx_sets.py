"""
    Sets are collection of things
        - unique values
        - unordered (no index)
        - can hold contents of different types
"""
nums_a = {1,2,3,4,5,10,12,13, 13}
nums_b = {2,3,4,5,25,26,27}

#Cannot have uniques
# print(nums_a) #13 was a duplciate

#Add a new item
nums_b.add("a") # a string added to a set of numbers
# print(nums_b)


#Removing items
nums_b.remove("a")
nums_b.discard("a") # Doesnt throw an error 
# print(nums_b)

#Union  - merge two sets except for the duplicates
print(nums_a.union(nums_b))
print(nums_a|nums_b)

#Set Different   - returns a new set that contains the elements that are in the first set but not in the second set. 
print(nums_a.difference(nums_b))
print(nums_a - nums_b)

#Sety Symmetrical Difference    - returns a new set that contains the elements that are in either of the sets, but not in both. In other words, it returns the set of elements that are unique to either of the sets, but not in both
print(nums_a.symmetric_difference(nums_b))
print(nums_a ^ nums_b)

try :
    print(nums_a[1]) # Wont work as sets are not indexed
except Exception as e :
    print(e)