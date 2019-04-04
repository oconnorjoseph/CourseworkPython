#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:00:18 2017

@author: Joseph O'Connor
UNI: jgo2115
"""

def invalidInput():
    print("Your input is invalid. Next time you run the program, type only a positive integer.")
    return

input_str = input("Type in a positive integer: ")
if "-" in input_str:
    invalidInput()
else: 
    try:
        num = int(input_str)
        if num == 0:
            invalidInput()
        else:         
            print("The following integers are the consecutive sums for all positive integers up to and then finally including {}:".format(num))
            for i in range(1, num + 1):
                partial_summation = 0
                for j in range(1, i + 1):
                    partial_summation += j
                print(str(partial_summation))
    except ValueError:
        invalidInput()    

