
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


