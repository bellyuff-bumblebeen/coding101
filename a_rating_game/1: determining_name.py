# name determining:

# (required before running)
name_list = []

def determine_name():
    print("What is your first name?")
    firstname = input("> ")
    print("What is your last name?")
    lastname = input("> ")
    firstname_cap = firstname.capitalize()
    lastname_cap = lastname.capitalize()
    # adds to running name list
    name_list.append(f"{firstname_cap} {lastname_cap}")

determine_name()