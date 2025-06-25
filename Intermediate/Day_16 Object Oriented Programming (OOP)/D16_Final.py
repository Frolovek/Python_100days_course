from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_continue = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while is_continue:
    request = input("What would you like? (espresso/latte/cappuccino):").lower()
    if request == "off":
        print("TEST turning off the machine")
        is_continue = False
    elif request == "report":
        print("TEST printing the report")
        coffee_maker.report()
        money_machine.report()
    elif request in menu.get_items():
        print("TEST Preparing")
        drink = menu.find_drink(request)
        if coffee_maker.is_resource_sufficient(drink):
            print("TEST Processing money")
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            else:
                is_continue = False
        else:
            is_continue = False
    else:
        is_continue = False




