#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:29:17 2017

@author: Joseph O'Connor
UNI: jgo2115
"""
import random
import sys

GUESS_COUNT = ['first','second','third','fourth','fifth']

def invalidInput():
    print("Your input is invalid. Type only an integer in the inclusive range between 1 and 10 or 'quit' to stop the program.")
    return

def tryGuess():
    input_str = input("What's your {} guess? Type 'quit' to quit the program: ".format(GUESS_COUNT[i]))
    if 'quit' in input_str:
        sys.exit()
    else:
        try:
            guess_int = int(input_str)
            if guess_int < 1 or guess_int > 10:
                invalidInput()
                tryGuess()
                return
            difference = abs(random_int - int(input_str))
            if difference > 5:
                print("Not even close.")
            elif difference > 2:
                print("Close.")
            elif difference != 0:
                print("Almost there.")
            else:
                print("You guessed correctly! Congratulations, you won!")
                sys.exit()
        except ValueError:
            invalidInput()
            tryGuess()
    return
    

random_int = int(random.random() * 10) + 1
print("I'm thinking of an integer between 1 and 10 inclusively. You get five chances to guess the number.")
try:
    for i in range(0, 5): 
        tryGuess()
    print("Aww, you could not guess the integer in 5 guesses. Sorry, you lost the game.")
except SystemExit:
    print("Goodbye!")