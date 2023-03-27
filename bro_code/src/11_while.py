"""
    Executes so that long a as condition is true
"""

name = None

# while (len(name)==0): 
while not name: 
    name = input ("Enter your name : ")

print(f"You entered {name}")


# Chat GPT examples
#-------------------
# Breaks in While - completely comes out of the while block
# The if statement checks if "num" is equal to 5, 
# and the break statement terminates the loop. 
num = 1
while num <= 10:
    if num == 5:
        break
    print(num)
    num += 1
print("Loop ended")

# Continue in while - Skips the current iteration
# statement skips the rest of the loop body
#  and goes to the next iteration when continue is hit

num = 1
while num <= 10:
    if num == 5:
        num += 1
        continue
    print(num)
    num += 1


num = 1
while num <= 10:
    print(num)
    num += 1



num = 5
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(factorial)




string1 = "hello"
reversed_string = ""
index = len(string1) - 1
while index >= 0:
    reversed_string += string1[index]
    index -= 1
print(reversed_string)




list1 = [1, 2, 3, 4, 5]
sum = 0
index = 0
while index < len(list1):
    sum += list1[index]
    index += 1
print(sum)
