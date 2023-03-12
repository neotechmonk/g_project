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





#Functional programming features
#Passing functions as arguments to other functions

def add_func(x :int , y: int) -> int: 
    return x + y


def multiply_func(x :int , y: int) -> int: 
    return x * y

def do_math(math_func,x, y): 
    return math_func(x,y)

print(f'do_math(add_func, 5, 6)  => {do_math(add_func, 5, 6)}')
print(f'do_math(multiply_func, 5, 6)  => {do_math(multiply_func, 5, 6)}')


#Returning functions
def adjust_total(sales): 
    def add_tax(sales):
        return sales*1.1
    return add_tax(sales)

print(f'adjust_total(100) => {adjust_total(100):.2f} after tax')