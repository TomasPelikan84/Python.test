import random
import os
from data import MENU
from data import resources

espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappucino_price = MENU["cappuccino"]["cost"]

def report(data):
    print(f"Voda: {data ['water']}")
    print(f"Milk: {data ['milk']}")
    print(f"Coffee: {data ['coffee']}")



# drink_user = input("Co by jste si dal? (espresso, latte, cappuccino): ")

resources_2 = resources

# odecet surovin
def cal_ingredience(name_of_drink):

    resources_2["water"] = resources_2["water"] - MENU[name_of_drink]["ingredients"]["water"]
    resources_2["milk"] = resources_2["milk"] - MENU[name_of_drink]["ingredients"]["milk"]
    resources_2["coffee"] = resources_2["coffee"] - MENU[name_of_drink]["ingredients"]["coffee"]
    print(f"Zbyle ingredience: {resources_2}")


def control_ingredience(name_of_drink, resources_2):
    if resources_2["water"] < MENU[name_of_drink]["ingredients"]["water"]:
        print("Neni dostatek ingredienci na Vas napoj.")
        return False
    elif resources_2["milk"] < MENU[name_of_drink]["ingredients"]["milk"]:
        print("Neni dostatek ingredienci na Vas napoj.")
        return False
    elif resources_2["coffee"] < MENU[name_of_drink]["ingredients"]["coffee"]:
        print("Neni dostatek ingredienci na Vas napoj.")
        return False
    else: 
        print("Na Vas napoj mame dost ingredienci.")
        return True
    
def coin_machine(drink_user):
    print("Prosim, vlozte mince 1, 2, 5, 10, 20, 50")
    coin_1 = int(input("Kolik 1 Kc chcete vlozit? "))
    coin_2 = int(input("Kolik 2 Kc chcete vlozit? ")) * 2
    coin_5 = int(input("Kolik 5 Kc chcete vlozit? ")) * 5
    coin_10 = int(input("Kolik 10 Kc chcete vlozit? ")) * 10
    coin_20 = int(input("Kolik 20 Kc chcete vlozit? ")) * 20
    coin_50 = int(input("Kolik 50 Kc chcete vlozit? ")) * 50
    sum = coin_1 + coin_2 + coin_5 + coin_10 + coin_20 + coin_50
    print(f"Celkem jste vlozili: {sum} Kc")
    print(f"Cena {drink_user} je: {MENU[drink_user]['cost']} Kc") 
    if sum > MENU["latte"]["cost"]:
        return_coin = sum - MENU["latte"]["cost"]
        print(f"Penize na zpet: {return_coin} Kc")
    print("Napoj se pripravuje.")    

def fill_in_ingredience():
    return resources

rest_of_ingredience = fill_in_ingredience() 

lets_continue = True

# cely program
while lets_continue == True:

    drink_user = input("Co by jste si dal? (espresso, latte, cappuccino): ")

    if drink_user == "report":
        report(resources_2)
        
    elif drink_user == "espresso":    
        #control_ingredience(drink_user, resources_2)
        lets_continue = control_ingredience(drink_user, resources_2)
        if lets_continue == False:
            break
        cal_ingredience(drink_user)
        coin_machine(drink_user) 

    elif drink_user == "latte":    
        #control_ingredience(drink_user, resources_2)
        lets_continue = control_ingredience(drink_user, resources_2)
        if lets_continue == False:
            break
        cal_ingredience(drink_user)
        coin_machine(drink_user)

    elif drink_user == "cappuccino":    
        #control_ingredience(drink_user, resources_2)
        lets_continue = control_ingredience(drink_user, resources_2)
        if lets_continue == False:
            break
        cal_ingredience(drink_user)
        coin_machine(drink_user)
    
    # lets_continue = control_ingredience(drink_user, resources_2)

    #if lets_continue == False:
     #   break

    

     

    # print(rest_of_ingredience)




#new_resources = {
#    "water": new_res_water,
#    "milk": new_res_milk,
 #   "coffee": new_res_coffee
#}
#print(new_resources)

#print(f"Zbyle ingredience: {resources_2}")










