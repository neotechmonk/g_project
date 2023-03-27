"""
    2023.03.25

    ## Scope
    - Write a program
    - That takes numbers as user input
    - Prints out
        1. Fizz if number is divisible by 3
        2. Buzz if number is divisible by 5
        3. Fizzbuzz if number is divisible by 3 and 5
        4. Just the number otherwise
"""

def show_output(msg : str)-> None:
    print(msg)

def process_input(input :str)-> float:
    """
        Validate input and return an integer
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