import random
import time
from art import logo

loop = "yes"
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suits = ["spades", "hearts", "clubs", "diamonds"]
card_pairs = {11:"ace", 2:"two", 3:"three", 4:"four",
              5:"five", 6:"six", 7:"seven", 8:"eight",
              9:"nine", 10:["ten", "jack", "queen", "king"]
}

def deal_cards ():
    string_hand = []
    int_hand = []
    for i in range(2):
        card_picker = cards[random.randint(0, 9)]
        int_hand.append(card_picker)
        if card_picker == 10:
            picked_card = card_pairs[card_picker][random.randint(0, 3)]
            string_hand.append(f"{picked_card} of {suits[random.randint(0, 3)]}".title())
        else:
            picked_card = card_pairs[card_picker]
            string_hand.append(f"{picked_card} of {suits[random.randint(0, 3)]}".title())

    return string_hand, int_hand

#I may or may not add a split feature later
def display_hand(hit_split, who):
    if hit_split == "hit":
        new_card = hit()
        who[0].append(new_card[0])
        who[1].append(new_card[1])
        if who == players_cards:
            print("\nyour hand is now: ", end = "")
        else:
            print("\nThe dealers hand is now: ", end = "")

        for card in who[0]:
            if card == who[0][-1]:
                print(f"and {card}. ", end = "")
            else:
                print(card + ", ", end = "")

        print(f"Adding up to: {sum(who[1])}")

def hit ():
    card_picker = cards[random.randint(0, 9)]
    added_value = card_picker
    if card_picker == 10:
        picked_card = card_pairs[card_picker][random.randint(0, 3)]
        added_card = f"{picked_card} of {suits[random.randint(0, 3)]}".title()
    else:
        picked_card = card_pairs[card_picker]
        added_card = f"{picked_card} of {suits[random.randint(0, 3)]}".title()

    return added_card, added_value

def play_again():
    gameplay_loop = input("play again? (yes) (no): ")
    if gameplay_loop == "yes":
        print("\n" * 20)
    else:
        print("\nThanks for playing!")
        quit()

    return gameplay_loop


#gameplay loop
while loop == "yes":
    print(logo)

    player_decision = ""
    #Lists with 2 lists inside: one for the card names, and the other for there value
    dealers_cards = deal_cards()
    players_cards = deal_cards()

    print(f"\nYou've been dealt a {players_cards[0][0]} and a {players_cards[0][1]}. Adding up to: {sum(players_cards[1])}")

    while player_decision != "check":
        print(f"dealers first card is: {dealers_cards[0][0]} ({dealers_cards[1][0]})")
        if sum(players_cards[1]) == 21:
            player_decision = "check"

        elif sum(players_cards[1]) < 21:
            player_decision = input("hit or check: ")
            if player_decision != "check":
                display_hand(player_decision, players_cards)

        else:
            if 11 in players_cards[1]:
                for number in range(len(players_cards[1])):
                    if players_cards[1][number] == 11:
                        players_cards[1][number] = 1
                        print(f"an ace was changed to 1. Your new sum is: {sum(players_cards[1])}")
                        break

            else:
                print("You Busted!")
                player_decision = "check"

    if not sum(players_cards[1]) == 21:
        if sum(players_cards[1]) < 21:
            print("\nmoving onto dealer...")
            time.sleep(2)
            print(f"\nThe dealers hand is {dealers_cards[0][0]} and a {dealers_cards[0][1]}. Adding up to: {sum(dealers_cards[1])}")

            while sum(dealers_cards[1]) < sum(players_cards[1]):
                time.sleep(1)
                display_hand("hit", dealers_cards)

                if sum(dealers_cards[1]) > 21:
                    if 11 in dealers_cards[1]:
                        for number in range(len(dealers_cards[1])):
                            if dealers_cards[1][number] == 11:
                                dealers_cards[1][number] = 1
                                print(f"a dealers ace was changed to 1. There new sum is: {sum(dealers_cards[1])}")
                                break

                    else:
                        print("Dealer Busted. You Win!")
                        loop = play_again()

            if sum(dealers_cards[1]) > sum(players_cards[1]) and sum(dealers_cards[1]) <= 21:
                print("dealer wins!")
                loop = play_again()

        else:
            #player busted
            loop = play_again()

    else:
        print("You got BLACKJACK! You Win!")
        loop = play_again()

