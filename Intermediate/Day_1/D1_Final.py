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
    "money": 0
}




def report_summary(available_resources):
    print(f"Water: {available_resources['water']}ml")
    print(f"Milk: {available_resources['milk']}ml")
    print(f"Coffee: {available_resources['coffee']}g")
    print(f"Money: {available_resources['money']}$")




def is_resources_sufficient(menu, coffee_request, available_resources):
    """Check if coffee machine has enough resources"""

    print("TEST in def checking resources")
    if (available_resources["water"] - menu[coffee_request]["ingredients"]["water"]) < 0:
        print("Sorry, not enough water")
        return False
    elif (available_resources["coffee"] - menu[coffee_request]["ingredients"]["coffee"]) < 0:
        print("Sorry, not enough coffee")
        return False
    elif coffee_request != "espresso":
        if (available_resources["milk"] - menu[coffee_request]["ingredients"]["milk"]) < 0:
            print("Sorry, not enough milk")
            return False
        else:
            print("TEST enough resources")
            return True
    else:
        print("TEST enough resources")
        return True




def process_coins():
    """Process inserted coins"""

    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    money_sum = 0.01 * pennies + 0.05 * nickles + 0.1 * dimes + 0.25 * quarters

    print(f"You inserted {money_sum}$")
    return money_sum




def is_transaction_successful(menu, coffee_request, inserted_money):
    """Check if user inserted enough money"""

    if (inserted_money - menu[coffee_request]["cost"]) < 0:
        print("Sorry, not enough money. Money refunded")
        return False
    elif (inserted_money - menu[coffee_request]["cost"]) > 0:
        in_change = inserted_money - menu[coffee_request]["cost"]
        print(f"Here is {round(in_change,2)}$ in change.")
        return True
    else:
        print("TEST enough money")
        return True



def finally_coffee(menu, coffee_request, available_resources):
    """Making coffee"""

    available_resources["money"] = available_resources["money"] + menu[coffee_request]["cost"]
    available_resources["water"] = available_resources["water"] - menu[coffee_request]["ingredients"]["water"]
    available_resources["coffee"] = available_resources["coffee"] - menu[coffee_request]["ingredients"]["coffee"]

    if coffee_request != "espresso":
        available_resources["milk"] = available_resources["milk"] - menu[coffee_request]["ingredients"]["milk"]

    print(f"Here is your {coffee_request}. Enjoy!")
    print(f"TEST {available_resources}")
    return available_resources


is_continue = True

while is_continue:
    request = input("What would you like? (espresso/latte/cappuccino):").lower()

    if request == "off":
        print("TEST turning off the machine")
        is_continue = False
    elif request == "report":
        print("TEST printing the report")
        report_summary(resources)
    elif request in ("espresso", "latte", "cappuccino"):
        print("TEST Preparing")
        if is_resources_sufficient(MENU, request, resources):
            user_money = process_coins()
            if is_transaction_successful(MENU, request, user_money):
                resources = finally_coffee(MENU, request, resources)
            else:
                is_continue = False
        else:
            is_continue = False
    else:
        is_continue = False

