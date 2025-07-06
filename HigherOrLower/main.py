import random
import art
from game_data import data

def select_contestants ():
    contestant_one = data[random.randint(0, len(data) - 1)]
    contestant_two = data[random.randint(0, len(data) - 1)]
    while contestant_two == contestant_one:
        contestant_two = data[random.randint(0, len(data) - 1)]

    one_description = f"a: {contestant_one['name']}, a {contestant_one['description']} from {contestant_one['country']}"
    two_description = f"b: {contestant_two['name']}, a {contestant_two['description']} from {contestant_two['country']}"

    return contestant_one["follower_count"], contestant_two["follower_count"], one_description, two_description


def game ():
    print(CONTESTANTS[2])
    print(art.vs)
    print(CONTESTANTS[3])
    if CONTESTANTS[0] > CONTESTANTS[1]:
        winner = CONTESTANTS[0]
    else:
        winner = CONTESTANTS[1]

    player_selection = input("\nWho has more followers? (a) (b): ")

    if player_selection == "a" and winner == CONTESTANTS[0]:
        return True
    elif player_selection == "b" and winner == CONTESTANTS[1]:
        return True
    else:
        return False


REPLAY = "yes"

while REPLAY == "yes":
    SCORE = 0
    print(art.logo + "\n")
    CONTESTANTS = select_contestants()
    while game():
        SCORE += 1
        print(f"Correct, your score is up to: {SCORE}" + "\n\n\n\n")
        CONTESTANTS = select_contestants()

    print(f"Incorrect, your final score was: {SCORE}")

    REPLAY = input("Play again? (yes) (no): ")
    if REPLAY == "yes":
        print("\n" * 20)