# screen to view coniditons (if any met):

# (required before running):
if __name__ == "__main__":
    # not an empty string because entering allows player to continue (defined in parameters)
    go_on = "blank"
    conditions = 2  # set to one to allow the screen to appear
    # set placeholders equal to the number of conditions
    condition_defs = ["def_placeholder 1", "def_placeholder 2"]

    chose_number = False  # defined in parameters


def condition_screen(go_on="blank", chose_number=False):
    if conditions > 0:
        print("\nEnter a number to see corrosponding condition definition")
        while go_on != "" or go_on == "not_a_number" or not chose_number:
            if go_on == "not_a_number":
                print("(or press enter to continue)")
            else:
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
                    # makes this print this message (OR press enter to continue)
                    go_on = "not_a_number"


# test:
if __name__ == "__main__":
    condition_screen()

# just testing something really quick...
