# status determining (2 -- if bad):

# (required before running):
if __name__ == "__main__":
    pstatus = "bad"  # not actually required, but this doesn't initiate this if pstatus is not bad


def determine_status2():
    print("Would you like to hear an inspiring quote? (yes/no)")
    status = ""
    while status == "":
        status = input("> ")
        status = status.lower()
        if status == "yes":
            # FINISH THIS MESSAGE (ADD A DICTIONARY)
            print("\n\"Be happy!\"")
        elif status == "no":
            print("\nWell, hope you feel better!")
        else:
            print("\nPlease answer with yes/no")
            status = ""


# test:
if __name__ == "__main__":
    determine_status2()
