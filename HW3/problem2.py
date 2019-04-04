#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Joseph O'Connor
UNI: jgo2115
"""
import string
c
def read_markets(filename):
    """
    Read in the farmers market data from the file named filename and return 
    a tuple of two objects:
    1) A dictionary mapping zip codes to lists of farmers market tuples.
    2) A dictionary mapping towns to sets of zip codes.
    """
    if not issubclass(type(filename), type("")):
        raise TypeError("Argument filename for function read_markets must be a string")
      
    market_entries = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            market_entries.append(tuple(line.split('#')[:-2]))
    
    zip_markets_dict = dict()
    town_zips_dict = dict()                             
    if len(market_entries) == 0:
        return zip_markets_dict, town_zips_dict

    for entry in market_entries:
        if entry[4] != "" and set(string.digits) >= set(entry[4]):
            entry_zip_int = int(entry[4])
            if entry_zip_int in zip_markets_dict.keys():
                zip_markets_dict[entry_zip_int].append(entry)        
            else:
                zip_markets_dict[entry_zip_int] = [entry,]
            
            if entry[3] in town_zips_dict.keys():
                town_zips_dict[entry[3]] |= set((entry_zip_int, ))
            else:
                town_zips_dict[entry[3]] = set((entry_zip_int,))
        
    print(zip_markets_dict)
    print(town_zips_dict)
    return zip_markets_dict, town_zips_dict

def print_market(market):
    """
    Returns a human-readable string representing the farmers market tuple
    passed to the market parameter.
    """
    if not issubclass(type(market), tuple):
        raise TypeError("Argument market for function print_market must be a tuple")
    if len(market) != 5:
        raise IndexError("Argument market for function print_market must be a tuple of size 5")
    return "\n{}\n{}\n{}, {} {}".format(market[1],market[2],market[3],market[0],market[4])

if __name__ == "__main__":
    FILENAME = "markets.txt"

    try: 
        zip_to_market, town_to_zips = read_markets(FILENAME)
        
        continue_bool = True
        while continue_bool:
            user_input = input("Please enter a zip code or town name, or type 'quit' to quit:\n").strip().lower()
            if user_input == "quit":
                continue_bool = False
            elif user_input == "":
                print("Invalid input.")
            else:
                zips_set = {}
                if 4 <= len(user_input) <= 5 and user_input.isdigit():
                    zip_input_int = int(user_input)
                    if zip_input_int in zip_to_market.keys():
                        zips_set = {zip_input_int}
                else:
                    for town_key in town_to_zips:
                        if user_input == town_key.lower():
                            zips_set = town_to_zips[town_key]
      
                if len(zips_set) == 0:
                    print("Not found.\n")
                else:
                    for zip_int in zips_set:
                        for market in zip_to_market[zip_int]:
                            print(print_market(market))
    except (FileNotFoundError, IOError): 
        print("Error reading {}".format(FILENAME))
