# stall initiation:

# (required before running)
stat_type = "stalled"

def stall_initiate(stat_type):
    while stat_type == "stalled": 
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

stall_initiate(stat_type)