#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 01:57:38 2017

@author: Joseph O'Connor
UNI: jgo2115
"""

def invalidInput():
    print("Your input is invalid. Next time you run the program, type only a positive integer height.")

user_input = input ("Type a whole number for the height of your desired Pascal's triangle, or type 'quit' to quit: ")

if "quit" in user_input:
    print("Goodbye!")
elif '-' in user_input:
    invalidInput()
else:
    height = 0
    try:    
        height = int(user_input)
    except ValueError:
        invalidInput()
        
    if height != 0:
        triangle = [[1]]
        width = height * 4
        
        for row in range(1, height):
            triangle.append([1])
            for col in range(1, row):
                summ = triangle[row - 1][col - 1] + triangle[row - 1][col]
                triangle[row].append(summ)
            triangle[row].append(1)
        
        
        for row in range(0, height):
            line = ""
            for col_data in triangle[row]:
                line += str(col_data)
                if col_data > 99:
                    line += " "
                elif col_data > 9:
                    line += "  "
                else:
                    line += "   "
            print(line.center(width, " "))