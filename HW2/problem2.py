# In the worst case, the number of character comparisons required by 
# find(s, substring) is equivalent to len(s)- len(substring).

# find_multi(s, substring) needs to make more character comparisons than 
# find(s, substring) in all but the worst case for find(s, substring). In the 
# worst case for find(s, substring), find_multi(s, substring) needs to make the 
# same amount of character comparisons as find(s, substring).

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 01:57:28 2017

@author: Joseph O'Connor
UNI: jgo2115
"""


def find(s, substring):
    max_index = len(s) - len(substring)
    
    if len(substring) == 0:
        return -1
    
    for index in range(0, max_index + 1):
        if substring == s[index:index + len(substring)]:
            return index
    return -1

def find_multi(s, substring):
    max_index = len(s) - len(substring)
    found_indexes = []
    
    if len(substring) == 0:
        return -1
    
    for index in range(0, max_index + 1):
        if substring == s[index:index + len(substring)]:
            found_indexes.append(index)
    return found_indexes