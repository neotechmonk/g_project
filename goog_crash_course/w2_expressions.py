f_name = "Pontius"
l_name = "Pilate"

# Logic
full_name = f_name + " " + l_name

# define the function
def get_full_name(first_name: str, last_name: str) -> str:
    full_name = first_name + " " + last_name
    return full_name


def print_name(name: str) -> None:
    with open("names.txt", "a") as file:
        file.write(name + "\n")
    print(name)


print(full_name)
print("================================")

# usage of the function
result = get_full_name("Joe", "Mafia")
print_name(result)
