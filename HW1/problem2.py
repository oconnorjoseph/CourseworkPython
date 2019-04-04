#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:29:31 2017

@author: Joseph O'Connor
UNI: jgo2115
"""

BAD_CHARACTERS = [' ',',','y','e','a','r','s']
CURRENT_POPULATION = 307357870
SEC_PER_YEAR = 60 * 60 * 24 * 365
SEC_PER_BIRTH = 7
SEC_PER_DEATH = 13
SEC_PER_IMMIGRANT = 35

def invalidInput():
    print("Your input is invalid. Next time you run the program, type only a positive number of years.")
    return

input_str = input("Type in a positive number of years into the future: ")
if "-" in input_str:
    invalidInput()
else: 
    for c in BAD_CHARACTERS:
        input_str = input_str.replace(c, '')  
    
    try:
        years = float(input_str)
        if (years == int(years)):
            years = int(years)
        seconds = years * SEC_PER_YEAR
        population_growth = int(seconds / SEC_PER_BIRTH) - int(seconds / SEC_PER_DEATH) + int(seconds / SEC_PER_IMMIGRANT)
        
        print("The estimated population after {} years will be {} people.".format(years, CURRENT_POPULATION + population_growth))    
    except ValueError:
        invalidInput()    
