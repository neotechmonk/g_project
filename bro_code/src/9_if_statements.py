# #If elif, else
# x = 10
# if x > 10:
#     print("x is greater than 10")
# elif x == 10:
#     print("x is equal to 10")
# else:
#     print("x is less than 10")

# #Nested conditions
# x = 10
# if x > 5:
#     if x < 15:
#         print("x is between 5 and 15")
#     else:
#         print("x is greater than or equal to 15")
# else:
# #     print("x is less than or equal to 5")


# is_sunny = True
# temperature = 80
# is_windy = False
# # # Old 
# if is_sunny and not is_windy \
#     and (temperature >= 60 and temperature <= 90) :
#     print("Great! The picnic can proceed.")
# else:
#     print("Unfortunately, the picnic cannot proceed.")


# # New
# if is_windy: # pair : 36 ; condition group 1
#     print("Unfortunately, the picnic cannot proceed.")
   
# else: # is not windy   # pair : 33; condition group 1
#     print ('May be a picnic day')
#     if is_sunny : #condition group 2 ; pair 47 
#         if temperature < 90 : # False  #condition group 3 ; pairs 41, 43, 45
#             print(f"Great! Its sunny and {temperature} is less than 90 . The picnic can proceed.")
#         elif   temperature > 60 : # True #condition group 3 ; pairs 39, 43, 45
#             print(f"Great! Its sunny and {temperature} is greater than 60 . The picnic can proceed.")
#         elif (1==1): #condition group 3 ; pairs 39, 41, 45
#             print("1==1") 
#         else :  #condition group 3 ; pairs 39, 41, 43
#             print("Great! Its sunny but looks like it not picnic weather")
#     else: # condition group 2 ; pair 38
#         pass

            
    
age = 7
# Version 1 
# if age < 13:
#     print("You are a child.")
# elif age < 18:#************
#     print("You are a teenager.")
# else:
#     print("You are an adult.")


# # Version 2
# if age < 13:
#     print("You are a child.")
# if age < 18: #************
#     print("You are a teenager.")
# if age < 25:
#     print ('go get a trade')
# else:
#     print("You are an adult.")


score = 75



if score >= 90:
    grade = "Too good"
elif 79 <= score <= 89: 
    grade = "Pass"
else:
    grade = "Failure"

print("Your grade is:", grade)

if score >= 80 and score < 90:
    grade = "B"

