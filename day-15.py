def resource_enough(drink, reso):
    for ing, amt in drink['ingredients'].items():
        if amt > reso[ing]:
            print(f"Sorry there is not enough {ing}")
            return False
    return True


def enough_coins(drink):
    total = int(input("how many quarters?:\t")) * 0.25
    total += int(input("how many dimes?:\t")) * 0.1
    total += int(input("how many nickles?:\t")) * 0.05
    total += int(input("how many pennies?:\t")) * 0.01
    cost = drink['cost']

    if cost > total:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
        total -= cost
        print(f"Here's a ${total:.2f} change.")
        return True

def process_drink(drink, reso):
    for ing, amt in drink['ingredients'].items():
        reso[ing] -= amt
    return reso


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0
still_on = True

while still_on:

    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == 'off':
        still_on = False

    elif user_choice == 'report':
        for key, value in resources.items():
            print(f"{key.capitalize()}: {value}")
        print(f"Profit: {profit}")

    elif user_choice in MENU:
        drink = MENU[user_choice]

        if resource_enough(drink, resources):
            print("Insert coins to proceed:")

            if enough_coins(drink):
                resources = process_drink(drink, resources)
                profit += drink['cost']
                print(f"Here's your {user_choice}, enjoy!")
