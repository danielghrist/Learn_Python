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

currency_type = {
        "quarters": .25,
        "dimes": .1,
        "nickels": .05,
        "pennies": .01
    }


# Prints a report showing the remaining resources and the current money
def print_report(current_resources, current_money):
    for ingredient in current_resources:
        print(f"{ingredient.capitalize()}: {current_resources[ingredient]} ml")

    print(f"Money: ${round(current_money, 2):.2f}")


# Get ingredients for certain coffee type
def get_ingredients(coffee_type):
    """Takes in a coffee type and returns the ingredients from the MENU dictionary\n
    Return: Ingredients Dictionary"""
    global MENU
    return MENU[coffee_type]["ingredients"]


# Checks if the remaining resources are sufficient to make the coffee selected
def resources_sufficient(current_resources, ingredients_needed):
    """

    :param current_resources: dictionary
    :param ingredients_needed: dictionary
    :return: boolean
    """
    for ingredient in ingredients_needed:
        if current_resources[ingredient] < ingredients_needed[ingredient]:
            print(f"Sorry, you do not have enough {ingredient}")
            return False
        else:
            return True


# Prompt user to insert coins, calculates and returns the total entered
def get_coins(currency):
    """
    Asks the user for different denomination coins and amounts
    :return: Total Money Received as a float"""

    money_received = 0
    print("Please insert coins.")
    for denomination in currency:
        money_received += (int(input(f"How many {denomination}?: "))) * currency[denomination]
    return money_received


# Process the user's payment by checking if it covers the cost
# then returning the total money to be added to the machine's bank
def process_payment(payment, coffee_cost):
    if payment < coffee_cost:
        print(f"Sorry, the cost was ${coffee_cost:.2f}.  You only paid ${payment:.2f}. Not enough money. Money refunded.")
        return 0
    elif payment > coffee_cost:
        change = payment - coffee_cost
        print(f"The cost was only ${coffee_cost:.2f}.  Here is your change ${change:.2f}.")
        return payment - change
    else:
        return payment


# Subtract the ingredients used from the resources dictionary dispense coffee
def make_coffee(ingredients, current_resources, coffee_type):
    for ingredient in ingredients:
        current_resources[ingredient] -= ingredients[ingredient]

    print(f"Here is your {coffee_type} ☕.  Enjoy!")
    return current_resources


# def run_machine(current_resources, total_money, currency):
#     global MENU
total_money = 0
continue_ordering = True

while continue_ordering:
    # Get user choice of coffee
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # Turn off the machine if user enters "off"
    if user_choice == "off":
        print("Machine turned off.")
        continue_ordering = False
    elif user_choice == "report":
        print_report(resources, total_money)
    else:
        # Get ingredients for the type of coffee the user selected
        needed_ingredients = get_ingredients(user_choice)
        cost = MENU[user_choice]["cost"]
        # Check to see if the current resources in the machine are sufficient to make the desired user coffee choice
        has_resources = resources_sufficient(resources, needed_ingredients)

        if has_resources is True:
            user_payment = get_coins(currency_type)
            paid_amount = process_payment(user_payment, cost)
            if paid_amount != 0:
                total_money += paid_amount
                resources = make_coffee(needed_ingredients, resources, user_choice)
            else:
                continue_ordering = False
        else:
            continue_ordering = False


# run_machine(resources, 0, currency_type)
