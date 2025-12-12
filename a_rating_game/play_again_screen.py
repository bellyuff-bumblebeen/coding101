# screen to play again (or enter special access):

# (required before running):
if __name__ == "__main__":
    firstname_cap = "MANUAL NAME"
    name_list = ["placeholder name 1",
                 "placerholder name 2", "placeholder name 3"]
    feedback_list = ["great game!", "excellent game!", "exceptional game!"]
    condition_list = ["0", "1", "2"]

    print("\n\n\nWould you like use our services again? (yes/no)")  # for test


def play_again_screen(again=""):
    while again == "":
        again = input("> ")
        again = again.lower()
        if again == "yes":
            responses += 1
            break
        elif again == "no":
            running = False
            print(f"\nThank you, and have a good day, {firstname_cap}!")

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
                        stat_type = "stalled"  # to initate a stall
                    print("\n\n\n\n\n\n")

                    # starts a "stall"
                    while stat_type == "stalled":           # MAKE THIS INTO A FUNCTION
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
                            # ADD AN AVERAGE DISPLAY TOO
                            f"{name}: {condition_list[name_list.index(name)]}")
                        stat_type = "stalled"  # to initiate a stall
                    print("\n\n\n\n\n\n")

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


# test:
if __name__ == "__main__":
    play_again_screen()
