"""
    YT : https://www.youtube.com/watch?v=aumxFs2DO5o
"""

from  dataclasses import dataclass
from typing import Iterable

@dataclass(frozen=True)
class Student:
    name: str
    age : int

    def __repr__ (self):
        return F'{self.name} is {self.age}y.o'
    


# NB : This function is not part of `Student` class
def print_students(students: Iterable[Student])-> None: 
    for item in students: 
        print(item)

if __name__ == "__main__":
    # Different Collection Types (List , Tuples, etc) are used
    # This is given the  `print_students ()` takes a generic Iteractor argument

    #List of Student Objects
    # students = [
    #     Student("Marcos", 53),
    #     Student("Rudy", 41),
    #     Student("Steve", 23),
    #     Student("JOhn", 42),
    #     Student("Peter", 23),
    # ]
    
    #Tuples of Student Objects    
    students = (
        Student("Marcos", 53),
        Student("Rudy", 41),
        Student("Steve", 23),
        Student("JOhn", 42),
        Student("Peter", 23),
     )

    print_students(students)