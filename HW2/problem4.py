#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 01:57:46 2017

@author: Joseph O'Connor
UNI: jgo2115
"""

def formatStringList(conjunction, *strings):
    elements_formatted = "{}".format(strings).replace("(","").replace(")", "").replace("[", "").replace("]", "")
    elements_formatted = elements_formatted[:len(elements_formatted) - 1]
    
    if "'," in elements_formatted:
        last_comma_index = elements_formatted.rindex("',")
        elements_formatted = "".join([elements_formatted[:last_comma_index], " ", conjunction, elements_formatted[last_comma_index + 2:]])
    
    return elements_formatted.replace("'","")
    

def input_with_verification(prompt, *acceptable_input):
    for attempt in range(0, 11):
        user_input = input(prompt).lower()
        
        if user_input == "quit":
            raise SystemExit 
        for acceptable in acceptable_input:
            if user_input == acceptable:
                return user_input
        print("Your input is invalid. Please only type one of the following: " + formatStringList("or", acceptable_input))
        
    print("Could not get a correct response after 10 attempts.")
    raise SystemExit

def toppings():
    return input_with_verification("Add a topping: pepperoni, mushrooms, spinach, or say 'done'\n", "pepperoni", "mushrooms", "spinach", "done")
    
def pizza():
    size_choice = input_with_verification("Small, medium, or large?\n", "small", "medium", "large") 
    topping_choices = []
    
    for topping_index in range(0, 3):
        topping = toppings()
        if topping == "done":
            break;
        topping_choices.append(topping)
    
    if len(topping_choices) == 0:
        topping_choices.append("no toppings")
    else:
        topping_choices.sort()
    return "{} pizza with {}".format(size_choice, formatStringList("and", topping_choices))
  
def dressing():
    return input_with_verification("Please choose a dressing: vinaigrette, ranch, blue cheese, or lemon\n", "vinaigrette", "ranch", "blue cheese", "lemon") 
    
def salad():
    salad_choice = input_with_verification("Would you like a garden salad or greek salad?\n", "garden", "greek") 
    
    return "{} salad with {} dressing".format(salad_choice, dressing()) 
    
def select_meal():
    meal = []
    meal_formatted = ""
    order_choice = input_with_verification("Hello, would you like a pizza or salad? Type 'quit' at any time to quit:\n", "pizza", "salad")
    
    while True:
        if order_choice == "pizza":
            meal.append(pizza())  
        elif order_choice == "salad":
            meal.append(salad())
        else:
            print("Your order has been placed. Goodbye.")
            return meal_formatted
        
        condensed_meal = []
        indexes_to_skip = []
        
        for index in range(0, len(meal)):
            if index not in indexes_to_skip:
                prefix = 1
                meal_at_index = meal[index]
                
                for further_index in range(index + 1, len(meal)):
                    if meal_at_index == meal[further_index]:
                        prefix += 1
                        indexes_to_skip.append(further_index)
                if prefix > 1:
                    meal_at_index = meal_at_index.replace("pizza", "pizzas").replace("salad", "salads")
                condensed_meal.append("{} {}".format(str(prefix), meal_at_index))
                
        meal_formatted = "You ordered {}. {}".format(formatStringList("and", condensed_meal), "Place another order or say 'done'.")
        print(meal_formatted)
        
        order_choice = input_with_verification("Hello, would you like a pizza or salad? Type 'quit' at any time to quit or 'done' to finish your order:\n", "pizza", "salad", "done") 
    
try:
    select_meal()
except SystemExit:
    print("Goodbye!")
    
    
