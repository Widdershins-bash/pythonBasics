import math

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resources_available (coffee):
    available = []
    required = []

    for ingredient in resources:
        available.append(resources[ingredient])

    for ingredient in MENU[coffee]['ingredients']:
        required.append(MENU[coffee]['ingredients'][ingredient])

    if available[0] > required[0] and available[1] > required[1] and available[2] > required[2]:
        return True
    else:
        return False

def print_report ():
    print("\nRemaining resources include:")
    for key in resources:
        print(f"{key}: {resources[key]}")

def receive_input ():
    print("\nACCESSING COFFEE MACHINE:")
    option_select = int(input("What can I help you with? (1: Check-Resources) or (2: Buy a cup of coffee): "))
    if option_select == 1:
        return 1
    elif option_select == 2:
        return 2
    else:
        print("Type a valid option")
        return 0

def buying_coffee ():
    print("\nThe menu is:")
    for key in MENU:
        print(f"{key}: ${MENU[key]['cost']}")

    coffee_select = ""
    valid_selection = False
    while not valid_selection:
        coffee_select = input("\nWhat would you like to buy: ").lower()
        if coffee_select in MENU:
            valid_selection = True

        else:
            print("Select a valid option:")
            valid_selection = False

    if resources_available(coffee_select):
        cost = MENU[coffee_select]['cost']
        payment = 0
        print("\nInsert coins:")

        print(f"costs: {math.floor(cost / .25)} quarters: ", end="")
        payment += float(input("insert quarters: ")) * 0.25

        print(f"now costs: {math.floor((cost - payment) / .10)} dimes: ", end="")
        payment += float(input("insert dimes: ")) * 0.10

        print(f"now costs: {math.floor((cost - payment) / .05)} nickels: ", end="")
        payment += float(input("insert nickels: ")) * 0.05

        print(f"now costs: {round((cost - payment) / .01)} pennies: ", end="")
        payment += float(input("insert pennies: ")) * 0.01

        if payment < cost:
            print("\nInsufficient funds...money refunded")
        elif payment > cost:
            print("\nOver-payed...money refunded")
        else:
            print(f"\nEnjoy your {coffee_select}!")

            resources["water"] -= MENU[coffee_select]["ingredients"]["water"]
            resources["milk"] -= MENU[coffee_select]["ingredients"]["milk"]
            resources["coffee"] -= MENU[coffee_select]["ingredients"]["coffee"]

    else:
        print("Insufficient resources: check report.")


POURING_COFFEE = "yes"

while POURING_COFFEE == "yes":
    selection = receive_input()
    if selection == 1:
        print_report()

    elif selection == 2:
        buying_coffee()

    POURING_COFFEE = ("Still using machine? (yes) (no): ")