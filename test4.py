# Calculator
import os
def sum(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiple(n1, n2):
    return n1 * n2
def division (n1, n2):
    return n1 / n2

symbols = {
    "+": sum,
    "-": subtract,
    "*": multiple,
    "/": division
}

def calculator():
    num1 = float(input("Zadej prvni cislo: "))
    lets_continue = "yes"
    while lets_continue == "yes":
        for key in symbols:
            print(key)
        operation = input("Zvolte jednu z operaci vyse: ")
        num2 = float(input("Zadejte dalsi cislo: "))

        calc_operation = symbols[operation]
        result = calc_operation(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        lets_continue = input("Napiste 'yes' pokud chcete pokracovat, napiste 'no' pokud chcete skoncit. ")
        if lets_continue == "yes":
            num1 = result
        else:
            os.system('cls')
            calculator()

calculator()

    
        



















