"""
    ## Scope
    - Write a program
    - That takes numbers as user input
    - Prints out
        1. Fizz if number is divisible by 3
        2. Buzz if number is divisible by 5
        3. Fizzbuzz if number is divisible by 3 and 5
        4. Just the number otherwise

    
    ## Updates
    - 20230327 - Initial working game
"""

def show_output(msg : str)-> None:
    """
    Prints the given message to the standard output.

    Args:
    - msg (str): The message to be printed.

    Returns:
    - None: This function does not return any value.
    """
    print(msg)

def process_input(input :str)-> float:
    """
    Validate input to be a number and return it as an integer.

    Args:
    - input (str): The input value to be validated.

    Raises:
    - ValueError: If input is None or empty.
    - TypeError: If input is not a valid integer.

    Returns:
    - int: The input value converted to an integer.
    """
    if input is None:
        raise ValueError("Input cannot be empty; Enter a number")
    elif input == "":
        raise ValueError("Input cannot be empty; Enter a number")
    elif not input.isnumeric():
        raise TypeError("Input must be a number")
    else: 
        return int(input)


def apply_game_logic(input: int) -> str:
    """
    Apply the FizzBuzz game logic to the given input.

    Args:
    - input (int): The input number to apply the game logic to.

    Returns:
    - str: The result of the game logic applied to the input, pre and suffixed in "--" 

    The FizzBuzz game rules are as follows:
    - If the input is divisible by 3, return "fizz".
    - If the input is divisible by 5, return "buzz".
    - If the input is divisible by both 3 and 5, return "fizzbuzz".
    - Otherwise, return the input number as a string.
    """
    response: str = ""
    if input % 5  == 0 and input % 3  == 0 :
        response= "fizzbuzz"
    elif input % 3 == 0:
        response= "fizz"
    elif input % 5 == 0:
        response= "buzz"
    else:
        response= str(input)

    return f"-- {response} --"

def main():
    """
    The main function that runs the FizzBuzz game.

    This function prompts the user for a number, applies the FizzBuzz game logic to it,
    and prints the result to the standard output. If the user enters an invalid input,
    an error message is displayed. The function ends with a thank-you message.

    The game terminates after one round of play or when an error is encountered. 

    """
    show_output("Welcome to Fizzbuzz!")
    user_input = input("Enter a number to start playing : ")

    try: 
        input_num = process_input(user_input)
        game_output_str = apply_game_logic(input_num)
        show_output(game_output_str)
    except (ValueError, TypeError) as e:
        show_output(str(e))
    except Exception: 
        show_output("Something went wrong terribly bad.\
                    \n Try again or just back to studies")
    finally : 
        show_output("Thanks for playing fair.. Hope you had fun!")


if __name__ == "__main__": 
    main()