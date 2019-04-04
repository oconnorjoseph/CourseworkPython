#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 15:25:28 2017

@author: Joseph O'Connor
UNI: jgo2115
"""

BAD_CHARS = [' ',',','s','e','c','o','n','d','s']

def invalidInput():
    print("Your input is invalid. Next time you run the program, type only a positive number of seconds in the inclusive range from 1 to 86400.")
    return

input_str = input("Type in a positive number of seconds (in the inclusive range from 1 to 86400): ")
if "-" in input_str:
    invalidInput()
else: 
    for c in BAD_CHARS:
        input_str = input_str.replace(c, '')  
    
    try:
        time_endings = ['s', 's', 's']
        seconds = float(input_str)
        if (seconds > 86400):
            invalidInput()
        else:
            hours = int(seconds / 3600)
            if hours == 1:
                time_endings[0] = ''
            seconds -= hours * 3600
            
            minutes = int(seconds / 60)
            if minutes == 1:
                time_endings[1] = ''
            seconds -= minutes * 60
            
            if seconds == 1:
                time_endings[2] = ''
            if seconds == int(seconds):
                seconds = int(seconds)
            else:
                seconds = round(seconds, 12)
                
            print("The corresponding time is {} hour{}, {} minute{}, and {} second{}.".format(hours, time_endings[0], minutes, time_endings[1], seconds, time_endings[2]))
    except ValueError:
        invalidInput()    
