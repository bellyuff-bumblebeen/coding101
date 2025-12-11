# status determining (1):
    
# (required before running):
good_bad = "unknown"
firstname_cap = "MANUAL"
lastname_cap = "NAME"

def determine_status1(firstname_cap, lastname_cap):
    print(f"Hello {firstname_cap} {lastname_cap}")
    print("\nHow are you doing? (good/bad)")
    while good_bad == "unknown":
        pstatus = input("> ")
        pstatus = pstatus.lower()
        if pstatus == "good":
            print("\nNice to hear that!\nHave a great day!")
            break
        elif pstatus == "bad":
            print("\nSorry to hear that...")
            break
        elif pstatus == "good/bad":
            print("\nHow, funny.\nYou've lost your privilages.")
            has_privilages = False
            break
        else:
            print("\nPlease answer with good/bad.")  # prevents error

determine_status1(firstname_cap, lastname_cap)