"""
    YT : https://youtu.be/aumxFs2DO5o?t=658
"""

from  dataclasses import dataclass
from typing import Iterable

#Note the dataclass offers a number if neat features like not defining the constructor
@dataclass()
class InfiniteIterator:
    num: int = 0

    def __iter__(self): 
        return self
    
    def __next__(self): 
        self.num += 1
        return self.num

@dataclass()
class FiniteIterator:
    max: int  # If the `__init__` is not overriden, this is assumed be 1st positinal argement
    num: int = 0 # Dont need to be passed in constructor as it has a default value


    def __iter__(self): 
        return self
    
    def __next__(self): 
        if(self.num >= self.max) : 
            raise StopIteration # this is not an exception ? Just break the iteraction
        
        self.num += 1
        return self.num
    

if __name__ == "__main__":
    for num in FiniteIterator(10): 
        print(num)