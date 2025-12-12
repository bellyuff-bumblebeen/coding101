import determining_name
import determining_status1
import determining_status2
import rate_sequence
import update_conditions

# saves across games:
running = True
name_list = []
feedback_list = []
condition_list = []
responses = 0

# start game:
while running:
    if responses > 0:
        print("\n" * 32)

# name:
    firstname_result, lastname_result = determining_name.determine_name()
    # adds to running name list
    name_list.append(f"{firstname_result} {lastname_result}")

# good/bad day:
    has_privilages = True
    pstatus = determining_status1.determine_status1(
        firstname_result, lastname_result)

# if bad, quote?:
    if pstatus == "bad":
        determining_status2.determine_status2()

# ADD A CONTINUE SCREEN BEFORE RATING

# rate:
    feedback, rate_attempts = rate_sequence.rate_sequence(firstname_result)
    feedback_list.append(f"{feedback}")

# condition updates:
    condition_messages = []
    condition_defs = []
    total_conditions = update_conditions.update_conditions(
        rate_attempts, pstatus, feedback, condition_messages, condition_defs)

# print conditions:
    break
