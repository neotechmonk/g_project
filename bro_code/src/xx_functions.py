"""
    Functions are an abstraction to wrap functionality

    Function may or may not take inputs

    Functions may or not retur values
"""

#Functions without input or returns
def print_name():
    name = input("Whats your name? ")
    print(f'Your name is {name}')
# print_name()

#Functions that return values
def get_name()-> str:
    return input("Whats your name, again? ")
# print(f'Input name is {get_name()}')

#Functions that take inputs and return values
def process_name(f_name:str, l_name:str)-> str:
    return f'{f_name} {l_name}'
# print(process_name('Peter','Parker')) #Positional
# print(process_name(l_name='Wilde', f_name='Oscar')) #Changed positions with parameter name

#Functions with default values
def raise_pow(base: int, power: int =2)-> int:
    return pow(base, power)
# print(raise_pow(3,2)) #Override default parameter
# print(raise_pow(4)) #Use the ß default parameter


# lambda function with no parameters
greeting = lambda: print("Hello, world!") #greeting now takes the lambda funciton
print(f'greeting() => ')
greeting()

# lambda function with one parameter
square = lambda number: number * number
print(f'square(5)) => {square(5)}')

# lambda function with two parameters
add_numbers = lambda num1, num2: num1 + num2
print(f'add_numbers(5, 7) => {add_numbers(5, 7)}')



# function with variable-length positional arguments
def add_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total

print(add_numbers(1, 2, 3)) #Calling directly 
print(add_numbers(4, 5, 6, 7))#Calling directly 

args_list = [4,3,5,6,]
print(f'add_numbers(*args) with list=> {add_numbers(*args_list)}')   #Using the unpacking operator (*):

args_tup = (23,4,35,2)
print(f'add_numbers(*args) with tuples=> {add_numbers(*args_tup)}')   #Using the unpacking operator (*):

#---------------

# function with variable-length keyword arguments
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=30, city="New York")


#------------------
#Lamba with Variable lenth positional arguments
lamba_add = lambda *args: sum(args)

print (f'lamba_add(1,2,3,3,4) == {lamba_add(1,2,3,3,4)}')


#------------------
#Lamba with Variable lenth k-v arguments

lamba_names = lambda **kwargs: print(", ".join(value for key, value in kwargs.items() if key == 'name'))



lamba_names(name="Alice", age=30, city="New York")# Call the lambda function with variable keyword arguments
lamba_names(name="Bob", city="San Francisco")

my_dict = {"name": "Samuel", "age": 30, "city": "New York", "name": "Peter"} # Call the lambda function with a dictionary; last name gets picked up 
lamba_names(**my_dict)

lamba_names1 = lambda **kwargs: print(", ".join(name if isinstance(name, str) else ", ".join(name) for key, name in kwargs.items() if key == 'name'))
my_dict1 = {"name": ["Ray", "Brett"], "age": 30, "city": "New York"} # Both names will be concat
lamba_names1(**my_dict1)
