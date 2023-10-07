import math
import random
import os

def sum(num1, num2):
    return num1 + num2

def subt(num1, num2):
    return num1 - num2

def multipl(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

operation = {
    "+": sum,
    "-": subt,
    "*": multipl,
    "/": division
}

def calculator():
    lets_continue = "ano"
    num1 = float(input("Jake je prvni cislo? "))
    while lets_continue == "ano":
        
        for key in operation:
            print(key)

        user_char = input("Zvolte jednu z operaci vyse: ")
        num2 = float(input("Zadejte dalsi cislo? "))

        calc_function = operation[user_char]
        result = calc_function(num1, num2)
        print(f"{num1} {user_char} {num2} = {result}")
        lets_continue = input("Zadejte 'ano' pokud chcete pokracovat, nebo 'ne' jestli chcete novou kalkulaci: ")
        if lets_continue == "ano":
            num1 = result
        else:
            os.system('cls')
            calculator()

calculator()

























