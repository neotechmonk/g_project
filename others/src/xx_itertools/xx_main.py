
def iterate_countries_with_while () -> None: 
    countries = ("United Kingdom",
             "United States", 
             "Germany",
             "France","Italy ")

    country_iter = iter(countries) #Gets an iterator. Doesnt iterator yet 

    # Its possible to get mulitple interacotrs on the same iterable 
    # Allows for the same iteration sequence to be run at different locations of the code
    # country_iter_copy = iter(countries) 

    while True : 
        try: 
            print(next(country_iter))        
        except StopIteration : 
            break


def iterate_countries_file() -> None: 
    with open ("countries.txt") as f : 
        for line in iter(f.readline,""):
            print(line, end = "")
 
if __name__ == "__main__":
    # iterate_countries_with_while()
    iterate_countries_file()


