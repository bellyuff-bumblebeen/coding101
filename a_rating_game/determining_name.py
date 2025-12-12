# name determining:

# (required before running)
# nothing

def determine_name():
    print("What is your first name?")
    firstname = input("> ")
    print("What is your last name?")
    lastname = input("> ")
    firstname_cap = firstname.capitalize()
    lastname_cap = lastname.capitalize()
    return firstname_cap, lastname_cap


# test:
if __name__ == "__main__":
    firstname_result, lastname_result = determine_name()

    print("\nName:")
    print(f"{firstname_result} {lastname_result}")
