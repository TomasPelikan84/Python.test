import random
import os
from data import MENU
from data import resources

#3 === zakladni nastaveni===

espresso_price = MENU['espresso']['cost']
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]


# === funkce ===
def report(data):
    print(f"Voda: {data ['water']}")
    print(f"Milk: {data ['milk']}")
    print(f"Coffee: {data ['coffee']}")

def coins():
    print("Prosim vlozte mince 1, 2, 5, 10, 20, 50. ")
    kc1 = int(input("Kolik 1 Kc chcete vlozit/: "))
    kc2 = int(input("Kolik 2 Kc chcete vlozit/: ")) * 2
    kc5 = int(input("Kolik 5 Kc chcete vlozit/: ")) * 5
    kc10 = int(input("Kolik 10 Kc chcete vlozit/: ")) * 10
    kc20 = int(input("Kolik 20 Kc chcete vlozit/: ")) * 20
    kc50 = int(input("Kolik 50 Kc chcete vlozit/: ")) * 50
    suma = kc1 + kc2 + kc5 + kc10 + kc20 + kc50
    print(f"Celkem jste vlozili {suma} Kc.")
    return suma

def calculate_change(user_sum_coins, price):
    refund = user_sum_coins - price
    if refund >= 0:
        print("Napoj se pripravuje.")
        if refund > 0:
            print(f"Zde jsou penize zpet: {refund} Kc")
    else:
        print(f"Nevhodili jste dostatek penez, jeste je potreba vlozit {price - user_sum_coins}")

def fill_in_ingredience():
    return resources

def consumption_ingredience(name_of_drink, ingredience):
    ingredience["water"] = ingredience["water"] - MENU[name_of_drink]["ingredients"]["water"]
    ingredience["milk"] = ingredience["milk"] - MENU[name_of_drink]["ingredients"]["milk"]
    ingredience["coffee"] = ingredience["coffee"] - MENU[name_of_drink]["ingredients"]["coffee"]
    print(f"Zbyle ingredience {ingredience}")


def calculate_ingredience(drink_name):
    if drink_name == "espresso":
        consumption_ingredience(drink_name, rest_of_ingredience)

    elif drink_name == "latte":
        consumption_ingredience(drink_name, rest_of_ingredience)

    elif drink_name == "cappuccino":
        consumption_ingredience(drink_name, rest_of_ingredience)

def ingredience_checker(in_water, in_milk, in_coffee):
    if in_water <= 0:
        print("Nemate dost ingredienci na tento napoj.")
        return False
    elif in_milk <= 0:
        print("nemate dost ingredienci na tento napoj.")
        return False
    elif in_coffee <= 0:
        print("nemate dost ingredienci na tento napoj.")
        return False
    else:
        print("Na Vas napoj mate dost ingredienci.")
        return True

rest_of_ingredience = fill_in_ingredience()
# === Kod automatu === 
lets_continue = True

while lets_continue == True:
    user_choice = input("Co by jste si dal(a)? (espresso, latte, cappuccino): ")

    calculate_ingredience(user_choice)

    if user_choice != "report":
        lets_continue = ingredience_checker(rest_of_ingredience["water"], rest_of_ingredience["milk"], rest_of_ingredience["coffee"])


    if lets_continue == False:
        break

    if user_choice == "report":
        report(rest_of_ingredience)
  
    if user_choice == "espresso":
        sum = coins()
        print(f"Cena espressa je {espresso_price} Kc.")
        calculate_change(sum, espresso_price)

    elif user_choice == "latte":
        sum = coins()
        print(f"Cena latte je {latte_price} Kc.")
        calculate_change(sum, latte_price)

    elif user_choice == "cappuccino":
        sum = coins()
        print(f"Cena cappuccina je {cappuccino_price} Kc.")
        calculate_change(sum, cappuccino_price)










