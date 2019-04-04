#/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: Joseph O'Connor
UNI: jgo2115
"""
import random

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
        print("Your input is invalid. Please only type one of the following: {}.".format(formatStringList("or", acceptable_input)))
        
    print("Could not get a correct response after 10 attempts.")
    raise SystemExit

class Card(object): 
    SUITS = ['♠','♣','♦','♥']
    RANKS = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    
    def __init__(self, suit, rank):
        if suit not in self.SUITS:
            raise ValueError("suit argument for Card object must be one of the following: {}.".format(formatStringList("or", self.SUITS)))
        if rank not in self.RANKS:
            raise ValueError("rank argument for Card object must be one of the following: {}.".format(formatStringList("or", self.RANKS)))
        self.suit = suit
        self.rank = rank           

    def __str__(self):
        return self.suit + self.rank

    def value(self, total):
        if self.rank == self.RANKS[12]:
            if total > 10:
                return 1
            else:
                return 11
        if self.rank in self.RANKS[:9]:
            return int(self.rank)
        return 10
    
deck = None
current_card = None
player_total = 0
dealer_total = 0

def make_deck():
    deck_list = []
    for suit in Card.SUITS:
        for rank in Card.RANKS:
            deck_list.append(Card(suit, rank))
    
    random.shuffle(deck_list)
    return deck_list 

def deal_player_and_continue():
    global current_card
    current_card = deck.pop()
    global player_total
    player_total += current_card.value(player_total)
    print("You have been delt {}.".format(current_card))
    print("Your total is now {}.".format(player_total))
    if player_total > 21:
        print("Sorry, you lost.")
        return False
    elif player_total == 21:
        print("Congratulations, you won!")
        return False
    else:
        input_str = input_with_verification("Do you want another card? Type 'yes' for another card or 'no' to stay, or type 'quit' to quit:\n", 'yes', 'no')
        if input_str == "yes":
            return deal_player_and_continue()
        return True

def deal_dealer_and_continue():
    current_card = deck.pop()
    global dealer_total
    dealer_total += current_card.value(dealer_total)
    print("Dealer has been delt {}.".format(current_card))
    print("Dealer's total is now {}.".format(dealer_total))
    if dealer_total > 21:
        print("Congratulations, you won!")
        return False
    elif dealer_total == 21:
        print("Sorry, you lost.")
        return False
    elif dealer_total > 16:
        return True
    return deal_dealer_and_continue()

def main():
    global deck
    deck = make_deck()
    if deal_player_and_continue():  
        print("Now its the dealer's turn.")
        if deal_dealer_and_continue():
            if player_total > dealer_total:
                print("Congratulations, you won!")
            elif player_total < dealer_total:
                print("Sorry, you lost.")
            else:
                print("Game is a push. Nobody wins.")
        
if __name__ == "__main__":
    main()
