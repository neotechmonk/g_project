#strings
f_name = "Zhou"
l_name = 'Wang' #single quote

full_name =  f_name+" "+l_name #string concatenation - must be same type
print(full_name)

#QUESTION - are there different types of floats and ints. E.g int32, float64?
#int
age= 30
print("{} is not {} y.o".format(f_name,str(age))) 
age+=50


#float 
height = 209.12
print(f"{full_name} is actally {str(age)} y.o") 
print(f"{full_name} is actually {age} y.o and {height}cm tall") #works without type casting int to str because f-string forces the conversion

#Checking date types
print(type(full_name)) #<class 'str'>

#numbers
int

#boolean
do_print = True
print("you got a print") if do_print else None


#Multiple assignments
city, country, temp = "Austin, TX", "Murica", 67
print("Temperature in {}, {} is {}".format(city, country, temp))

#Assigning the same value to multiple variables
#Box
height = width  = depth = 10
print(f"the volume is {height*width*depth}cm")