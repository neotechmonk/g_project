"""
Handy string methods

    string.find
    string.capitalize
    string.upper
    string.lower
    string.isdigit
    string.isalpha
    string.count
    string.replace
"""


from string import Template

#Helper function
def pprint(template: str, *args):
    print(template.format(*args))

string = "donkey k0ng"
pprint("Original string {}", string)


pprint("Length of the string =>  {}", len(string))


pprint("{} has 0 instead of o at =>  {}", string,  string.find('0'))

new_string = string.replace("0","o")

pprint("{} <= replace'd =>   {}", new_string,  string)
pprint("{} capitalised =>   {}", new_string,  new_string.capitalize())
pprint("{} upper cased =>   {}", new_string,  new_string.upper())
pprint("{} lower cased =>   {}", new_string,  new_string.lower())
pprint("{} isdigit=>   {}", new_string,  new_string.isdigit())
pprint("{} is isnumeric=>   {}", new_string,  new_string.isnumeric())
pprint("{} is isalpha (a-z, A-Z),=>   {}", new_string,  new_string.isalpha())
pprint("{} is isalnum (a-z, A-Z, 0-9),)=>   {}", new_string,  new_string.isalnum())
pprint("{} is isascii (a-z, A-Z, 0-9, + symbols),)=>   {}", new_string,  new_string.isascii())
pprint("More than one {}=> {}", new_string,  ("\n\t"+new_string)*3)



# string.find()
# string.capitalize
# string.upper
# string.lower
# string.isdigit
# string.isalpha
# string.count
# string.replace

