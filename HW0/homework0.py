t# -*- coding: utf-8 -*-
"""
Spyder Editor

By Joseph O'Connor
"""

# Informs user about nursery rhyme & prints nursery rhyme
urprint("Here's a nursery rhyme this program will solve:")
print("As I was going to St. Ives, I met a man with seven wives. Every wife had seven sacks, and every sack had seven cats, every cat had seven kittens. Kittens, cats, sacks, and wives, how many were going to St. Ives? \n")

# Calculates the number of people and things going to St. Ives
count = 1
for i in range(5):
    count += 7**i

# Prints the total number of people and things who are going to St. Ives
print("The total number of people and things going to St. Ives is {}.".format(count))
