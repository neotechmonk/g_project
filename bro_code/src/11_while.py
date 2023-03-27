"""
    Executes so that long a as condition is true
"""

name = None

# while (len(name)==0): 
while not name: 
    name = input ("Enter your name : ")

print(f"You entered {name}")