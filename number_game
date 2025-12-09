import random
game_on = True
new_game = True
first_game = True
try_counter = 0
try_cap = 8
player_literal = ""
player_number = ""
player_wins = 0
averager = []


while game_on:
    if new_game:
        n = random.randint(1, 100)
#changes the prompt if its not your first time
    if first_game:
        message = """guess a number from 1-100:
> """
    else:
        message = "> "

#player guesses:
    player_literal = (input(message))
    player_number = int(player_literal)

#if value is lower than the number
    if player_number < n: 
        message = """higher...
try again..."""
        print(message)
        first_game = False
        try_counter += 1
        new_game = False

#if value if higher than the number
    elif player_number > n: 
        message = """lower...
try again..."""
        print(message)
        first_game = False
        try_counter += 1
        new_game = False

#if player runs out of tries (7)
    if try_counter == try_cap:
        averager.append(try_cap)
        message = """out of tries! sorry!
play again (yes/no)?
> """
        player_number = input(message)
        if player_number.lower() == "yes":
            message = """
new number generated..."""
            print(message)
            player_number = ""
            first_game = False
            new_game = True
            try_counter = 0
        elif player_number.lower() == "no":
            game_on = False


#if value is correct
    elif player_number == n:
        if try_counter > 0:
            message = "correct! you win!"
            print(message)
        elif try_counter == 0:
            message = "wow! first try! you win!"
            print(message)
        player_wins += 1
        averager.append(try_counter)
        try_counter = 0

#asks player to play again
        message = """would you like to play again (yes/no)?
> """
        player_number = input(message)
        if player_number.lower() == "yes":
            message = """
new number generated..."""
            print(message)
            player_number = ""
            first_game = False
            new_game = True

        elif player_number.lower() == "no":
            game_on = False

#if value is invalid
    if player_number == ValueError:
        message = "must be a number from 1-100"
        print(message)
        first_game = False
        new_game = False


final_avg = sum(averager) / len(averager)
message = """
game ended."""
print(message)
print(f"average # of tries: {final_avg} / {try_cap}")
print(f"total wins: {player_wins} / {len(averager)}")