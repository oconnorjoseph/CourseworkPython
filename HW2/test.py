#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20   15:15:39 2017
ENGIE 1006
"""
TOLERANCE =  0.1
n = 81
guess = 2
print(guess)
while abs(guess*guess - n)   >  TOLERANCE:
    quotient =  n  / guess
    guess =  (quotient +  guess) /  2
    print(guess)
print("The square root of ", n," is   ",guess)