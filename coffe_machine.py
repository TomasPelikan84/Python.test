import random
import os
from data import MENU
from data import resources

espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappucino_price = MENU["cappuccino"]["cost"]

drink_user = input("Co by jste si dal? (espresso, latte, cappuccino): ")

resources_2  = resources

#if drink_user == "report":
 #   print(resources)


# odecet surovin

esp_water = MENU["espresso"]["ingredients"]["water"]
esp_milk = MENU["espresso"]["ingredients"]["milk"]
esp_coffee = MENU["espresso"]["ingredients"]["coffee"]

latte_water = MENU["latte"]["ingredients"]["water"]
latte_milk = MENU["latte"]["ingredients"]["milk"]
latte_coffee = MENU["latte"]["ingredients"]["coffee"]

cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]

resources_water = resources_2["water"]
resources_milk = resources_2["milk"]
resources_coffee = resources_2["coffee"]

if drink_user == "espresso":
    new_res_water = resources_water - esp_water
    new_res_milk = resources_milk - esp_milk
    new_res_coffee = resources_coffee - esp_coffee

new_resources = {
    "water": new_res_water,
    "milk": new_res_milk,
    "coffee": new_res_coffee
}
print(new_resources)

#print(f"Zbyle ingredience: {resources_2}")










