# status determining (1):

# (required before running):
if __name__ == "__main__":
    firstname = "MANUAL NAME"
    lastname = "MANUAL NAME"


def determine_status1(firstname, lastname):
    print(f"\nHello {firstname} {lastname}")
    print("How are you doing? (good/bad)")
    good_bad = "unknown"
    while good_bad == "unknown":
        status = input("> ")
        status = status.lower()
        if status == "good":
            print("\nNice to hear that!\nHave a great day!")
            break
        elif status == "bad":
            print("\nSorry to hear that...")
            break
        elif status == "good/bad":
            print("\nHow, funny.\nYou've lost your privilages.")
            has_privilages = False
            break
        else:
            print("\nPlease answer with good/bad.")  # prevents error
    return status


# test:
if __name__ == "__main__":
    pstatus = determine_status1(firstname, lastname)
    print("\nstatus:")
    print(pstatus)
