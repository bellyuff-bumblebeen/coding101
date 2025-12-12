# update conditions (if met):

# (required before running):
if __name__ == "__main__":
    condition_messages = []
    condition_defs = []

    # these are all specific to certain conditions CHANGE THESE TO TEST OTHER OUTCOMES:
    # (indef, meaning in definition to distinguish from outside varibales:)
    rate_attempts = 2
    pstatus = "good/bad"
    rating_num = 2
    feedback = ""


def update_conditions(rate_attempts_indef, pstatus_indef, feedback_indef, condition_message_list, condition_defs_indef):
    total_conditions_indef = 0

    if rate_attempts_indef > 3:
        total_conditions_indef += 1
        condition_message_list.append(
            "\"rating should not have been that difficult...\"")
        condition_defs_indef.append(
            "--You entered an invalid rating over 3 times")
    elif rate_attempts_indef >= 1:
        total_conditions_indef += 1
        condition_message_list.append(
            "\"get better at following instructions\"")
        condition_defs_indef.append(
            "--You entered an invalid rating at least 1 time")
    if pstatus_indef == "good/bad":
        total_conditions_indef += 1
        condition_message_list.append(
            "\"okay, smart one...(it wasn't funny)\"")
        condition_defs_indef.append(
            "--You entered 'good/bad' when we asked you to answer with good/bad")
    if feedback_indef == "":
        total_conditions_indef += 1
        condition_message_list.append("\"thanks for that advice...\"")
        condition_defs_indef.append("--You sumbitted blank feedback")
    return total_conditions_indef


# test:
if __name__ == "__main__":
    total_conditions = update_conditions(
        rate_attempts, pstatus, feedback, condition_messages, condition_defs)
    print("\nmessages:")
    for message in condition_messages:
        print(message)
    print("\ndefinitions:")
    for definition in condition_defs:
        print(definition)
    print("\ntotal conditions met:")
    print(total_conditions)
