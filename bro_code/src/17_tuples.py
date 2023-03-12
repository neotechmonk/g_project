"""
    Similar to Lists but
    -- immutable
    --  ordered

    - Can have duplicates
    - Different to named tuples



    Functions
        count => of some value appearing
        index ==> index of occurence of a value
"""

pet_dog_1 = ("Dog", "Jimmy", "male")
pet_dog_2 = ("Dog", "Leah", "female")
pet_rabbit = ("Rabbit", "Oreo", "male")
pet_parrot = ("Indian ring neck", "Stef", "female")


pets = [pet_dog_1,pet_dog_2, pet_rabbit, pet_parrot]



# Iterate over the employees and print their information
for pet in pets:
    type, name, gender = pet
    print(f"Name: {name}, Type: {type}, Gender: {gender}")

