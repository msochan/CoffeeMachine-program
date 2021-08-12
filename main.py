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

money_inside_machine = 0


def print_report():
    print("Resources available:")
    print(f" Water: {resources['water']}ml")
    print(f" Milk: {resources['milk']}ml")
    print(f" Coffee: {resources['coffee']}g")
    print(f" Money: ${money_inside_machine}")


def check_resources(coffee_ingredients):
    for ingredient in coffee_ingredients:
        if coffee_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    print("Please insert coins")
    quarters = float(input("How many quarters: "))
    dimes = float(input("How many dimes: "))
    nickles = float(input("How many nickles: "))
    pennies = float(input("How many pennies: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def check_transaction(inserted_money, coffee_cost):
    global money_inside_machine
    if inserted_money < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif inserted_money == coffee_cost:
        money_inside_machine += inserted_money
        return True
    else:
        money_inside_machine += coffee_cost
        change = round(inserted_money - coffee_cost, 2)
        print(f"Here is ${change} dollars in change.")
        return True


def make_coffee(coffee_type):
    if check_resources(MENU[coffee_type]["ingredients"]):
        inserted_money = process_coins()
        if check_transaction(inserted_money, MENU[coffee_type]["cost"]):
            for key in MENU[coffee_type]["ingredients"]:
                resources[key] -= MENU[coffee_type]["ingredients"][key]
            print(f"Here is your {coffee_type}. Enjoy!")


def game_loop():
    is_continue = True
    while is_continue:
        choose = (input("What would you like? (espresso/latte/cappuccino): ")).lower()
        if choose == "off":
            is_continue = False
            print("Machine turning off...")
        elif choose == "report":
            print_report()
        elif choose == "espresso":
            make_coffee(choose)
        elif choose == "latte":
            make_coffee(choose)
        elif choose == "cappuccino":
            make_coffee(choose)


game_loop()
