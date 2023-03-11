"""
    String slicing
        1. Indexing []
        2. slice()

    Benefits of Slice over indexing (@ChatGPT)
    Readbility / Reusability : For example, instead of writing my_list[0:5], you can use the slice my_slice = slice(0, 5) and then reference that slice in multiple places in your code.

    Flexibility: Slices are more flexible than indexing because they can handle missing indices and negative indices. For example, if you have a list my_list with 10 elements, you can use the slice my_slice = slice(0, 20) without getting an error, whereas if you tried to index my_list[0:20] you would get an IndexError. Similarly, you can use negative indices in a slice to select elements from the end of a list, whereas negative indices don't work with indexing

    Memory efficiency: When you slice a list or array, you create a new view into the same underlying data, rather than creating a new copy of the data. This can be more memory-efficient than creating a new copy of the data when indexing
"""

full_name = 'Justin Mathers'

#Indexing (0 indexed)=> start, stop, step (skip)
#-----------------------------------------------
#start => inclusive
#stop => exclusive
print(f'{full_name} => start, stop,  = {full_name[0:6]}')
print(f'{full_name} => start, stop, skip  = {full_name[0:6:2]}') #Skip every other letter J[u]s[t]i[n]
print(f'{full_name} => , stop,   = {full_name[:6:]}') 
print(f'{full_name} => start, ,   = {full_name[7:]}') 
print(f'{full_name} => start, ,   = {full_name[::-1]}')  #Reversing

#Gotchas
#Start>Stop
print(f'{full_name} => start, ,   = {full_name[7:2:]}') #Prints nothing
err_name = {full_name[7:2:]}
#Index out of bounds
print(f'{full_name} => start, ,   = {full_name[14:2:]}') #Prints nothing


#Slicing
#-----------------------------------------------
# The syntax for creating a slice object is slice(start, stop, step) where start, stop, and step are all optional arguments.

# start represents the starting index of the slice (inclusive). If start is not specified, the slice starts from the beginning of the sequence.
# stop represents the ending index of the slice (exclusive). If stop is not specified, the slice ends at the end of the sequence.
# step represents the step value for the slice. If step is not specified, it defaults to 1.

url = 'https://www.youtube.com'
#Definition of the extract. Similar to regex?
my_slice  = slice(12, -4) 
print(f'website => ' + url[my_slice])



#Chat GPT
my_string = "Hello, world!"

# Extract the last five characters of the string
substring = my_string[slice(-6, None)]
print(substring)  # Output: "world!"


my_string = "Hello, world!"

# Extract the first five characters of the string
substring = my_string[slice(5)]
print(substring)  # Output: "Hellow!"
