from dictionary import MENU, resources

money = 30


def price(qn, dn, nn, pn):
    q = 0.25
    d = 0.1
    n = 0.05
    p = 0.01
    total = q * qn + d * dn + n * nn + p * pn
    return total


def check_resources(coffe):
    if coffe not in MENU:
        print("Invalid coffee type. Please choose a valid option.")
        return 0

    ingredients = MENU[coffe]['ingredients']

    if ingredients['water'] >= resources["water"]:
        print("Sorry, there is not enough water.")
        return 0
    if 'milk' in ingredients and ingredients['milk'] >= resources["milk"]:
        print("Sorry, there is not enough milk.")
        return
    if ingredients['coffee'] >= resources["coffee"]:
        print("Sorry, there is not enough coffee.")
        return 0
    else:
        resources["water"] -= ingredients["water"]
        if 'milk' in ingredients:
            resources["milk"] -= ingredients["milk"]
        resources["coffee"] -= ingredients["coffee"]
        return 1


def do_coffe():
    global money
    coffe_type = input("What would you like to ?(espresso/latte/cappuccino)")
    if coffe_type == "off":
        return 0
    if coffe_type == "report":
        print(f"money:{money}")
        for ing in resources:
            print(f"{ing}:{resources[ing]}")
    if coffe_type in MENU:
        if check_resources(coffe_type):
            print(f"{coffe_type}:${MENU[coffe_type]['cost']} ")
            quarters = int(input("How many quarters ?"))
            dimes = int(input("How many dimes ?"))
            nickles = int(input("How many nickles ? "))
            pennies = int(input("How many pennies ? "))
            total = price(quarters, dimes, nickles, pennies)

            if total >= MENU[coffe_type]["cost"]:
                refund = total-MENU[coffe_type]["cost"]
                if money >= refund:
                    print(f"Here is ${round(refund,2)} in change")
                    print(f"Here is your {coffe_type} ☕ Enjoy !")
                    money -= refund
                    money += MENU[coffe_type]["cost"]
                elif money <= refund:
                    print("There is not enough refund in machine.")
            else:
                print("Sorry that's not enough money. Money refunded.")
    do_coffe()


do_coffe()



