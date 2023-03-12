"""
Syntax
    try => dangerous code
    except => specific type of Exception/Error
    else => thing to if there will no errors
    finally => thing to do whether try or error


Specific exceptions should be handled before high level exceptions


Error as e properties
    args: a tuple of arguments used to create the exception

    message: the error message associated with the exception

    strerror: an alias for message

    filename: the name of the file where the exception occurred

    lineno: the line number where the exception occurred
    
    traceback: a traceback object that encapsulates the call stack at the point where the exception was raised
"""

import math

def square_root(x):
    try:
        result = math.sqrt(x)
    except ValueError as e:
        #Catching and throwing a customer error 
        # `form e` stipulates chaining of errors so that link can be established to the original error
        raise ValueError(f"You passed a negative number: ") from e
    # Catching multiple exceptions 
    except (ValueError, ZeroDivisionError) as e:
        print(f"An error occurred: {type(e).__name__}")
    else:
        print(f"The square root of {x} is {result}.")
    finally:
        print("Done calculating the square root.")

# square_root(4) # Output: The square root of 4 is 2.0. Done calculating the square root.
square_root(-4) # Output: Cannot calculate the square root of a negative number. Done calculating the square root.


#Additional tricks
# # Passing the name of the exception as a string
# print(f"An error occurred: {type(e).__name__}")