running = True
name_list = []
feedback_list = []
condition_list = []
responses = 0

# special access notes:

# at play again screen, input "stats" to enter special access:
# ---input "player_conditions" to access feedback
# ---input "player_feedback" to access feedback
# ---input "exit" to go back to play again screen

# at "<stall>" screen:
# ---press enter to go back to special access screen
# ---input "exit" to go back to play again screen (in progress)
# ---if you input anything else, the stall continues

while running:

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
    # adds to running name list
    name_list.append(f"{firstname_cap} {lastname_cap}")

# status resets:
    good_bad = "unknown"
    has_privilages = True
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
            has_privilages = False
            break
        else:
            print("\nPlease answer with good/bad.")  # prevents error

# new status resets:
    new_pstatus = ""
# answer based on status
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


# rate resets:
    rate = "unknown"
    rated = False
    rate_attempt = 0
    rating = 0
    rating_num = 0
# rate?
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
                        if int(rating) == 0:  # prevents loop glitch
                            print("\nPlease enter an integer rating from 1-10:")
                            rate_attempt += 1  # this is important to prevent the glitch
                    except ValueError:
                        rate_attempt += 1
                        print("\nPlease enter an integer rating from 1-10:")
                rating_num = int(rating)

            # interprets input:
                # feedback resets:
                feedback = ""
                # feedback:
                if (0 < rating_num <= 5):
                    rated = True
                    print("\nWe are always looking to improve.\nType feedback here:")
                    feedback = input("> ")
                    if feedback != "":
                        # adds to running feedback list:
                        feedback_list.append(f"{feedback}")
                    else:
                        # adds to running feedback list:
                        feedback_list.append("~blank feedback")
                    print(
                        f"\nFeedback sent.\nThank you, {firstname_cap}, for your response.")
                    break
                    responses += 1
                elif (9 >= rating_num > 5):
                    rated = True
                    print(
                        f"\nRating sent.\nThank you for using our services, {firstname_cap}!")
                    # adds to running feedback list:
                    feedback_list.append("~n/a")
                elif rating_num == 10:
                    rated = True
                    print(
                        f"Wow! 10/10! Thank for your rating, {firstname_cap}!")
                    # adds to running feedback list:
                    feedback_list.append("~n/a")
                else:
                    print("\nPlease enter an integer rating from 1-10:")
                    rate_attempt += 1
                    rating_num = 0
            break
        elif rate == "no":
            rating_num = 0  # to prevent an error in the feedback condition
            print(f"\nThank you for your time, {firstname_cap}.\nGoodbye.")
            # adds to running feedback list:
            feedback_list.append("~n/a")
            break
        else:
            print("\nPlease answer with yes/no")

# ADD GAME OVER SCREEN AND CONTINUE PROMPT

# condition resets:
    conditions = 0
    condition_messages = []
    condition_defs = []
    go_on = "blank"  # this is "blank" because enter lets the player continue
    chose_number = False
# conditions: (count)
    if rate_attempt > 3:
        conditions += 1
        condition_messages.append(
            "\"rating should not have been that difficult...\"")
        condition_defs.append("--You entered an invalid rating over 3 times")
    elif rate_attempt >= 1:
        conditions += 1
        condition_messages.append("\"get better at following instructions\"")
        condition_defs.append(
            "--You entered an invalid rating at least 1 time")
    if pstatus == "good/bad":
        conditions += 1
        condition_messages.append("\"okay, smart one...(it wasn't funny)\"")
        condition_defs.append(
            "--You entered 'good/bad' when we asked you to answer with good/bad")
    if (0 < rating_num <= 5) and feedback == "":
        conditions += 1
        condition_messages.append("\"thanks for that advice...\"")
        condition_defs.append("--You sumbitted blank feedback")

# conditions: (print)
    print(f"\n\n\n\n\nYou met {conditions} condition(s):")
    # adds to running condition list:
    condition_list.append(f"{conditions}")
    for item in range(conditions):
        print(f"{item + 1}) {condition_messages[item]}")

# wait to continue, number for definition
    if conditions > 0:
        print("\nEnter a number to see corrosponding condition definition")
        while go_on != "" or not chose_number:
            print("(press enter to continue)")
            go_on = input("> ")
            try:
                go_on = int(go_on)
                if conditions >= go_on > 0:
                    print(f"\n{condition_defs[go_on - 1]}")
                    chose_number = True  # allows loop to stop
                else:
                    if conditions > 1:
                        message = f"try a number in range 1-{conditions}"
                    elif conditions == 1:
                        message = "your only choice is 1"
                    print(f"\nInvalid number. ({message})")
            except ValueError:
                if go_on == "":
                    break
                else:
                    print("\nPlease enter a number.")

# again resets:
    again = ""
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

# input "stats" to view gathered information
        elif again == "stats":
            # reset stat type:
            stat_type = "blank"  # set to blank because 'stat_type' is reused

            print("\n\n\n\n\n\n<statistics accessed>")
            print("<input statistic type>")
            while stat_type == "blank":
                stat_type = input("> ")
                stat_type = stat_type.lower()
            # if feeback stats:
                if stat_type == "player_feedback":
                    print("\n\n\n\n\n\n<feedback gathered>\n")
                    for name in name_list:
                        # given the name, finds the corrosponding feedback to print:
                        print(
                            f"{name}: {feedback_list[name_list.index(name)]}")
                        print("\n\n\n\n\n\n")
                        stat_type = "stalled"  # to initate a stall

                    # starts a "stall"
                    while stat_type == "stalled":  # ADD AN EXIT OPTION TO GO STRAIGHT BACK TO NEW GAME?
                        print("<stall>")
                        stat_type = input("> ")
                        stat_type = stat_type.lower()
                        # if you input enter, you exit the stall, back to stat type input
                        if stat_type == "":
                            print("<stall exited>")
                            stat_type = "exited stall"  # sends you to an "if" below
                        # if you input enter, it sends you down to the exit "if" below
                        elif stat_type == "exit":
                            break
                        # if you don't input enter, you stay in the stall:
                        else:
                            stat_type = "stalled"

            # if condition stats:
                elif stat_type == "player_conditions":
                    print("\n\n\n\n\n\n\n<conditions gathered>\n")
                    for name in name_list:
                        # given the name, finds the corrosponding conditions to print:
                        print(
                            f"{name}: {condition_list[name_list.index(name)]}")
                        print("\n\n\n\n\n\n")
                        stat_type = "stalled"  # to initiate a stall

                    # starts a "stall"
                    while stat_type == "stalled":
                        print("<stall>")
                        stat_type = input("> ")
                        stat_type = stat_type.lower()
                        # if you input enter, you exit the stall, back to stat type input:
                        if stat_type == "":
                            print("<stall exited>")
                            stat_type = "exited stall"  # sends you to an "if" below
                        # if you input exit, it sends you down to the exit "if" below
                        elif stat_type == "exit":
                            break
                        # if you don't input enter, you stay in the stall:
                        else:
                            stat_type = "stalled"

            # if exit: (this is if and not elif, because if you come from a stall, you also exit)
                if stat_type == "exit":
                    again = ""
                    print(
                        f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWould you like to use our services again? (yes/no)")
                    break

            # if you exit a stall, you are sent here: (this is if for the same reason as above)
                if stat_type == "exited stall":
                    print("<input statistic type>")
                    stat_type = "blank"  # allows stat type loop to continue
            # if your input is invalid:
                else:
                    print("\n<cannot accept that input>")
                    stat_type = "blank"

        else:
            print("\nPlease answer with yes/no")
            again = ""
