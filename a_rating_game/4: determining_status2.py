# status determining (2 -- if bad):

# (required before running):
pstatus = "bad"
new_pstatus = ""

def determine_status2(pstatus, new_pstatus):
    if pstatus == "bad":
        print("Would you like to hear an inspiring quote? (yes/no)")
        while new_pstatus == "":
            new_pstatus = input("> ")
            new_pstatus = new_pstatus.lower()
            if new_pstatus == "yes":
                # FINISH THIS MESSAGE (ADD A DICTIONARY)
                print("\n\"Be happy!\"")
            elif new_pstatus == "no":
                print("\nWell, hope you feel better!")
            else:
                print("\nPlease answer with yes/no")
                new_pstatus = ""
            
determine_status2(pstatus, new_pstatus)
