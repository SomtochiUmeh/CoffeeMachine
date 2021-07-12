
menu = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
            'milk': 0
        },
        'cost': 1.5
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24
        },
        'cost': 2.5
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24
        },
        'cost': 3.0
    }
}
resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}

water, coffee, milk = resources['water'], resources['coffee'], resources['milk']
money = resources['money']

# TODO 1: 'what would you like? (espresso/latte/cappuccino):'
# check user input to see what to do next
# the prompt should show every time action has completed


def request():
    return input('What would you like? (espresso/latte/cappuccino): ').lower()


# TODO 2: 'turn off the coffee machine by entering 'off' to the prompt'

# while True:
#     if request == 'off':
#         break
    # continue with the rest of the program


# TODO 3: print report when user enters report to the prompt; water, milk, coffee, money

def report():
    print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: {money}")


# TODO 4: Check if resources are sufficient
# when user chooses a drink, check if the resources are enough to make that drink
# 'sorry, there is not enough {resource}'

# req_water, req_milk = menu[request()]['ingredients']['water'], menu[request()]['ingredients']['milk']
# req_coffee, req_cost = menu[request()]['ingredients']['coffee'], menu[request()]['cost']


def sufficient():
    if req_milk > milk:
        print("Sorry, there's not enough milk")
        return False
    if req_water > water:
        print('Sorry, there\'s not enough water')
        return False
    if req_coffee > coffee:
        print('Sorry, there\'s not enough coffee')
        return False
    return True


# TODO 5: process coins
# if there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins
# quarter, dimes, nickels and pennies and calculate the monetary value of the coins inserted

def coins(quart, dim, nick, pen):
    return quart*0.25 + dim*0.1 + nick*0.05 + pen*0.01


# TODO 6: Check if the transaction was successful
# insufficient funds: refund the money; 'Sorry that's not enough money. Money refunded.'
# if enough money is inserted, the cost gets added as money to the resources and the resources are updated
# if the user inserted too much money, the machine should offer change to 2d.p

def transaction(paid, needed):
    if paid < needed:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if paid > needed:
            change = paid - needed
            print(f'Your {requests} costs {needed}; you paid {paid:.2f}; your change is {change:.2f}.')
        global money
        money += needed
        return True


# TODO 7: Make coffee
# ingredients to make the drink are deducted from the resources

def make_coffee():
    global milk
    milk -= req_milk
    global coffee
    coffee -= req_coffee
    global water
    water -= req_water


# once all the resources have been deducted, tell the user 'here's your latte, enjoy
# print('Here\'s your latte, enjoy.')

if __name__ == '__main__':

    while True:

        requests = request()

        if requests == 'off':

            break

        if requests == 'report':

            report()

        else:

            req_water, req_milk = menu[requests]['ingredients']['water'], menu[requests]['ingredients']['milk']
            req_coffee, req_cost = menu[requests]['ingredients']['coffee'], menu[requests]['cost']

            if sufficient():

                quarters = int(input('How many quarters: '))
                dimes = int(input('How many dimes: '))
                nickels = int(input('How many nickels: '))
                pennies = int(input('How many pennies: '))

                if transaction(coins(quarters, dimes, nickels, pennies), req_cost):

                    make_coffee()
                    print('Here\'s your latte, enjoy.')
