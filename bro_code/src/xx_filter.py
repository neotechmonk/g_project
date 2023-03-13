"""
    Creates subset from data these collections
        Lists: [1, 2, 3, 4, 5]
        Tuples: (1, 2, 3, 4, 5)
        Sets: {1, 2, 3, 4, 5}
        Dictionaries: {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    
    The search criteria is passed as a function. This function can be
        1. Convetional named functio OR
        2. lamda function


    Filter returns the iterator that matches the type of the collection passed in as parameter

"""

jobs = [
    ('Software Engineer', 'San Francisco', 120000),
    ('Data Scientist', 'New York City', 110000),
    ('Product Manager', 'Seattle', 130000),
    ('UX Designer', 'Seattle', 95000),
    ('Marketing Manager', 'Chicago', 105000),
    ('Sales Representative', 'Los Angeles', 85000)
]
#Filter function doesnt take params
print('----------Over paying jobs - Default argument')
def filter_100k(job)->bool:
    return job[2]>= 100000 #access the salary through indexing

print(
     list(filter(filter_100k, jobs))
     )

print('----------Over paying jobs - additional argument')
#Filter function takes additional parameter
def filter_100k_with_params(job, thresh)->bool:
     return job[2]>= thresh

#Because filte only takes a function without additional arguments, any function that takes additional arguments needs to have an outer funciton. In this case its an lambda funcitonß
print(
     list(filter(lambda job:filter_100k_with_params(job, 100_000), jobs))
     )




#Filter as a lambda function
print('----------Under paying jobs')
print(
     list(filter(lambda job: job[2]<100_000, jobs))
     )
