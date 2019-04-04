#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:18:19 2017

@author: Joseph O'Connor
UNI: jgo2115
"""

import random
import math

POSSIBLE_MOVES_STR = ["rock", "paper", "scissors"]

while True:
    player_move_str = "".join(input("Rock, paper, or scissors? Type 'quit' if you would like to quit: ").split())
    if player_move_str == 'quit':
        break;
    computer_move = int(random.random() * 3)
    player_move = 3
    
    for i in range(3):
        if (player_move_str == POSSIBLE_MOVES_STR[i]):
            player_move = i
            break;
            
    if player_move == 3:
        print ("Type only 'rock', 'paper', or 'scissors' as a move, or 'quit' to quit the program.") 
    else:
        print ("You chose " + player_move_str + ".")
        print ("The computer chose... " + POSSIBLE_MOVES_STR[computer_move] + "!")
        difference = computer_move - player_move
        if difference % 3 == 1:
            print ("You lost! Aww.")
        elif difference == 0:
            print ("It's a draw!")
        else:
            print ("You win! Woo-hoo!")