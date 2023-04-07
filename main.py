from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
drink_maker = CoffeeMaker()
money = MoneyMachine()
machine_on = True
user_request = input(f"What would you like? {menu.get_items()} ").lower()
#
while machine_on:
    if user_request == 'report':
        drink_maker.report()
        money.report()

    elif user_request == 'off':
        machine_on = False

    else:
        drink = menu.find_drink(user_request)
        sufficient = drink_maker.is_resource_sufficient(drink)
        if sufficient:
            transaction = money.make_payment(drink.cost)

            if transaction:
                drink_maker.make_coffee(drink)
                