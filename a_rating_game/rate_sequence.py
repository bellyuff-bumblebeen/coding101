# initiates the rating sequence:

# (required before running):
if __name__ == "__main__":
    feedback_list = []
    firstname = "MANUAL NAME"  # techincally, never uses your last name


def rate_sequence(firstname):
    print("\nWould you like to rate my services? (yes/no)")
    rate = "unknown"
    while rate.lower() != "yes" or "no":  # until a valid answer is inputted
        rate = input("> ")
        rate = rate.lower()

        # if you choose to rate:
        if rate == "yes":
            attempt = 0
            rated = False
            while not rated:
                # aquires a rating:
                rating = 0
                while rating == 0:
                    if attempt == 0:
                        print("\nType in your rating here (1-10)")
                        rating_str = input("> ")
                    else:
                        rating_str = input("> ")

                    # prevents ValueError:
                    try:
                        rating = int(rating_str)
                        if int(rating_str) == 0:  # prevents loop glitch
                            print("\nPlease enter an integer rating from 1-10:")
                            attempt += 1  # this is important to prevent the glitch
                    except ValueError:
                        attempt += 1
                        print("\nPlease enter an integer rating from 1-10:")
                rating = int(rating_str)

            # interprets rating:

# 0-5:
                if (0 < rating <= 5):
                    # has an underscore just to prevent confusion between the variable inside and outside of the function:
                    feedback_ = ""
                    rated = True
                    print("\nWe are always looking to improve.\nType feedback here:")
                    feedback_ = input("> ")
                    if feedback_ == "":
                        feedback_ = "~blank feedback"
                    else:
                        # just here for readability, shows that feedback remains the same:
                        feedback_ = feedback_
                    print(
                        f"\nFeedback sent.\nThank you, {firstname}, for your response.")

# 6-9:
                elif (9 >= rating > 5):
                    rated = True
                    print(
                        f"\nRating sent.\nThank you for using our services, {firstname}!")
                    feedback_ = "~n/a"

# 10:
                elif rating == 10:
                    rated = True
                    print(
                        f"Wow! 10/10! Thank for your rating, {firstname}!")
                    # adds to running feedback list:
                    feedback_ = "~n/a"

# invalid number:
                else:
                    print("\nPlease enter an integer rating from 1-10:")
                    attempt += 1
                    rating = 0
            break

        # if you choose not to rate:
        elif rate == "no":
            rating = 0  # rating is set to zero at deafault
            # number of attempts needs to be set to 0 (since return includes this value):
            attempt = 0
            print(f"\nThank you for your time, {firstname}.")
            # adds to running feedback list:
            feedback_ = "~n/a"
            break  # prevents any bugs
        else:
            print("\nPlease answer with yes/no")
    return feedback_, attempt


# test:
if __name__ == "__main__":
    feedback, rate_attempts = rate_sequence(firstname)
    print("\nfeedback:")
    print(feedback)
    print("\nattempts:")
    print(rate_attempts)
