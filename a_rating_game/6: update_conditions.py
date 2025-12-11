# update conditions (if met):

# (required before running):
rate_attempt = 2 # change to test other outcomes
pstatus = "good/bad" # change to test other outcomes
rating_num = 2 # change to test other outcomes
feedback = "" # change to test other outcomes
condition_messages = []
condition_defs = []

def update_conditions():
    conditions = 0

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

# test:
update_conditions()
print("\nmessages:")
for message in condition_messages:
    print(message)
print("\ndefinitions:")
for definition in condition_defs:
    print(definition)
