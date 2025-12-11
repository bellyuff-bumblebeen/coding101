# initiates the rating sequence:

# (required before running):
feedback_list = []
firstname_cap = "MANUAL NAME"
lastname_cap = "MANUAL NAME"
rate = "unknown" # defined in parameters
rated = False # defined in parameters
rate_attempt = 0 # defined in parameters
rating_num = 0 # defined in parameters

def rate_sequence(rate="unknown", rated=False, rate_attempt=0, rating_num=0):
    print("\nWould you like to rate my services? (yes/no)")
    while rate.lower() != "yes" or "no":
        rate = input("> ")
        rate = rate.lower()

        # if you choose to rate:
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

        # if you choose not to rate:
        elif rate == "no":
            rating_num = 0  # to prevent an error in the feedback condition
            print(f"\nThank you for your time, {firstname_cap}.")
            # adds to running feedback list:
            feedback_list.append("~n/a")
            break
        else:
            print("\nPlease answer with yes/no")

# test:
rate_sequence()