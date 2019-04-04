#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 01:57:08 2017

@author: Joseph O'Connor
UNI: jgo2115
"""

VOWELS = "aeiou"
running = True
user_word = ""

def piggy(word):
    accumulated_consonants = ""
    
    for char in word:
        if char in VOWELS:
            if len(accumulated_consonants) == 0:
                word += "y"
            else:
                word = word[len(accumulated_consonants):] + accumulated_consonants
            break
        else:
            accumulated_consonants += char
            
    word += "ay"
    return word

while running:
    user_word = input ("Type a word to translate it to pig latin or type '.' to quit: ")
    
    if user_word == ".":
        print ("Oodbyegay!")
        break
    print ("The pig latin translation of '{}' is '{}'.".format(user_word, piggy(user_word)))