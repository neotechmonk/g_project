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

from pprint import pprint


jobs_tuple_list = [
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
     list(filter(filter_100k, jobs_tuple_list))
     )

print('----------Over paying jobs - additional argument')
#Filter function takes additional parameter
def filter_100k_with_params(job, thresh)->bool:
     return job[2]>= thresh

#Because filte only takes a function without additional arguments, any function that takes additional arguments needs to have an outer funciton. In this case its an lambda funcitonß
print(
     list(filter(lambda job:filter_100k_with_params(job, 100_000), jobs_tuple_list))
     )




#Filter as a lambda function
print('----------Under paying jobs')
print(
     list(filter(lambda job: job[2]<100_000, jobs_tuple_list))
     )


## Dictionary examples
print('----------Dictionary ==> Seatle jobs')
jobs_dict = {}
for job in jobs_tuple_list:
    title = job[0]
    city = job[1]
    salary = job[2]
    jobs_dict[title] = {"city": city, "salary": salary}


# filtered_jobs = dict(filter(lambda job: job[1]['city'] == 'Seattle', jobs_dict.items()))

#Note that we are using the any() function to check if any of the job dictionary values have a 'city' key that is equal to 'Seattle'. This is necessary because the job dictionary may have more than one value, and we want to filter out the job if any of the values have the wrong city

filtered_jobs = dict(
                    filter(
                        lambda job: any(
                                        job_val['city'] == 'Seattle' 
                                            for job_val in jobs_dict.values()
                                        ), 
                    jobs_dict.items())
                    )


print(filtered_jobs)