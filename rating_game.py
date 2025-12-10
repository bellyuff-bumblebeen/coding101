running = True
responses = 0

while running:
    # name
    good_bad = "unknown"
    # rating
    rate = "unknown"
    rated = False
    rate_attempt = 0
    rating = 0
    rating_num = 0
    # restart
    again = ""
    # feedback
    feedback = ""
    feedback_list = []
    # special coniditions
    conditions = 0
    total_conditions = 0
    condition_messages = []
    condition_defs = []
    go_on = "blank"
    chose_number = False
    go_on2 = "blank"

# separation (if second or more time)
    if responses > 0:
        print("\n" * 27)

# determine name:
    print("What is your first name?")
    firstname = input("> ")
    print("What is your last name?")
    lastname = input("> ")
    firstname_cap = firstname.capitalize()
    lastname_cap = lastname.capitalize()

# determine status:
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
            break
        else:
            print("\nPlease answer with good/bad.")  # prevents error

    new_pstatus = ""
# answer based on status
    if pstatus == "bad":
        print("Would you like to hear an inspiring quote? (yes/no)")
        while new_pstatus == "":
            new_pstatus = input("> ")
            new_pstatus = new_pstatus.lower()
            if new_pstatus == "yes":
                print("\n\"Be happy!\"") #FINISH THIS MESSAGE
            elif new_pstatus == "no":
                print("\nWell, hope you feel better!")
            else:
                new_pstatus = ""
        


# rate? (yes/no)
    print("\nWould you like to rate my services? (yes/no)")
    while rate.lower() != "yes" or "no":
        rate = input("> ")
        rate = rate.lower()

        if rate == "yes":
            while not rated:
                while rating_num == 0:
                    if rate_attempt == 0:
                        print("\nType in your rating here (1-10)")
                        rating = input("> ")
                    elif rate_attempt > 0:
                        rating = input("> ")
                        
                    # prevents ValueError:
                    try:
                        rating_num = int(rating)
                        if int(rating) == 0: # prevents loop glitch
                            print("\nPlease enter an integer rating from 1-10:")
                            rate_attempt += 1 # this is important to prevent the glitch
                    except ValueError:
                        rate_attempt += 1
                        print("\nPlease enter an integer rating from 1-10:")
                rating_num = int(rating)
    
                # interprets input
                if (0 < rating_num <= 5):
                    rated = True
                    print("\nWe are always looking to improve.\nType feedback here:")
                    feedback = input("> ")
                    print(
                        f"\nFeedback sent.\nThank you, {firstname_cap}, for your response.")
                    break
                    responses += 1
                elif (9 >= rating_num > 5):
                    rated = True
                    print(f"\nRating sent.\nThank you for using our services, {firstname_cap}!")
                elif rating_num == 10:
                    rated = True
                    print(f"Wow! 10/10! Thank for your rating, {firstname_cap}!")
                else:
                    print("\nPlease enter an integer rating from 1-10:")
                    rate_attempt += 1
                    rating_num = 0
            break
        elif rate == "no":
            rating_num = 0  # to prevent an error in the feedback condition
            print(f"\nThank you for your time, {firstname_cap}.\nGoodbye.")
            break
        else:
            print("\nPlease answer with yes/no")

# conditions: (count)
    if rate_attempt > 3:
        conditions += 1
        condition_messages.append("\"rating should not have been that difficult...\"")
        condition_defs.append("--You entered an invalid rating over 3 times")
    elif rate_attempt >= 1:
        conditions += 1
        condition_messages.append("\"get better at following instructions\"")
        condition_defs.append("--You entered an invalid rating at least 1 time")
    if pstatus == "good/bad":
        conditions += 1
        condition_messages.append("\"okay, smart one...(it wasn't funny)\"")
        condition_defs.append("--You entered 'good/bad' when we asked you to answer with good/bad")
    if (0 < rating_num <= 5) and feedback == "":
        conditions += 1
        condition_messages.append("\"thanks for that advice...\"")
        condition_defs.append("--You sumbitted blank feedback")

# conditions: (print)
    print(f"\n\n\n\n\nYou met {conditions} conditions:")
    for item in range(conditions):
        print(f"{item + 1}) {condition_messages[item]}")

# wait to continue, number for definition
    if conditions > 0:
        print("\nEnter a number to see corrosponding condition definition")
    while go_on != "" or chose_number:
        print("(press enter to continue)")
        go_on = input("> ")
        try:
            go_on = int(go_on)
            try:
                if go_on > 0:
                    print(f"\n{condition_defs[go_on - 1]}")
                    chose_number = True #allows loop to stop
                else:
                    print("\nInvalid number")
            except IndexError:
                if conditions > 0:
                    print("\nInvalid number")
        except ValueError:
            if go_on == "":
                break
            else:
                print("\nInvalid number")

# again?
    print("\n\n\nWould you like use our services again? (yes/no)")
    while again == "":
        again = input("> ")
        again = again.lower()
        if again == "yes":
            responses += 1
            break
        elif again == "no":
            running = False
            print(f"\nThank you, have a good day, {firstname_cap}!")
        else:
            print("\nPlease answer with yes/no")
            again = ""