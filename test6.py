import random
import math

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(text, shift):
    encode_text = ""
    for one in text:
        if one != " ":
            index = alphabet.index(one)
            new_index = index + shift
            encode_text = encode_text + alphabet[new_index]
        else:
            encode_text = encode_text + " "

    print(f"Zakodovany text je: {encode_text}")

def decode(text, shift):
    decode_text = ""
    for one in text:
        if one != " ":
            index = alphabet.index(one)
            new_index = index - shift
            decode_text = decode_text + alphabet[new_index]
        else:
            decode_text = decode_text + " "

    print(f"Odkodovany text je: {decode_text}")

def cipher(direction, text, shift):
    end_text = ""
    for one in text:
        if one != " ":
            index = alphabet.index(one)
            if direction == "encode":
                new_index = index + shift
                end_text = end_text + alphabet[new_index]
            elif direction == "decode":
                new_index = index - shift
                end_text = end_text + alphabet[new_index]
        else:
            end_text = end_text + " "
    print(f"Zakodovany text je: {end_text}")
    # lets_continue = input("Zadejte 'ano' jestli chcete pokracovat, nebo 'ne' jestli chcete program ukoncit.\n")


lets_continue = "ano"

while lets_continue == "ano":
    direction = input("Zadejte 'encode' jestli chcete zakodovat text, nebo 'decode' jestli chcete odkodovat text.\n")
    text = input("Zadejte text pro kodovani nebo odkodovani:\n")
    shift = int(input("Zadejte delku posunu:\n"))

    cipher(direction, text, shift)
    lets_continue = input("Zadejte 'ano' jestli chcete pokracovat, nebo 'ne' jestli chcete program ukoncit.\n")

    #elif direction == "decode":
      #  decode(text, shift)
      #  lets_continue = input("Zadejte 'ano' jestli chcete pokracovat, nebo 'ne' jestli chcete program ukoncit.\n")







    


