
def greetings(name="noble stranger"):
    if not isinstance(name, str):
        print("Error! It was not a name.")
        return

    print(f"Hello, {name}.")

greetings("Alexandra")
greetings("Wil")
greetings()
greetings(42) 







    
        
