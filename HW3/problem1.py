#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Joseph O'Connor
UNI: jgo2115
"""

from collections  import defaultdict
import string

def compare(item1, item2):
    item1[0] - item2[0]
    

def count_ngrams(file_name, n=2):
    """
    This function reads an input file and returns a dictionary of n-gram counts.
    file_name is a string, n is an integer.
    The result dictionary maps n-grams to their frequency (i.e. the count of 
    how often that n-gram appears). 
    Each n-gram key is a tuple and the count is an int.
    """
    if not issubclass(type(file_name), type("")):
        raise TypeError("Argument file_name for function count_ngrams must be a string")
    if not issubclass(type(n), int):
        raise TypeError("Argument n for function count_ngrams must be an integer")
    if n < 1:
        raise ValueError("Argument n for function count_ngrams must be greater than 0")
    
    ngram_count_dict = defaultdict(int)
    file_string = ""
    with open(file_name, 'r') as file:
        file_string = file.read().replace('\n', " ").replace('\r', " ")
    if file_string == "":
        return ngram_count_dict

    for bad_char in string.whitespace.replace(" ","") + string.punctuation:
        file_string = file_string.replace(bad_char, "")
    file_words = [word for word in file_string.lower().strip().split() if word != ""]
        
    if n > len(file_words):
        return ngram_count_dict
    
    ngrams_list = []
    for index in range(len(file_words) + 1 - n):
        ngrams_list.append(tuple(file_words[index:index + n]))
    
    for ngram_tuple in ngrams_list:
        ngram_count_dict[ngram_tuple] += 1
    return ngram_count_dict    
    
def single_occurences(ngram_count_dict):
    """
    This functions takes in a dictionary (in the format produces by
    count_ngrams) and returns a list of all ngrans with only 1 occurence.
    That is, this function should return a list of all n-grams with a count
    of 1.
    """
    if not issubclass(type(ngram_count_dict), dict):
        raise TypeError("Argument ngram_count_dict for function single_occurences must be a dictionary")
        
    single_occurances_list = []
    for key, value in ngram_count_dict.items():
        if value == 1:
            single_occurances_list.append(key)
    
    return single_occurances_list

def most_frequent(ngram_count_dict, num = 5):
    """
    This function takes in two parameters:
        ngram_count_dict is a dictionary of ngram counts.
        num denotes the number of n-grams to return.
    This function returns a list of the num n-grams with the highest
    occurence in the file. For example if num=10, the method should
    return the 10 most frequent ngrams in a list.
    """
    if not issubclass(type(ngram_count_dict), dict):
        raise TypeError("Argument ngram_count_dict for function most_frequent must be a dictionary")
    if not issubclass(type(num), int):
        raise TypeError("Argument num for function most_frequent must be an integer")
    if num < 0:
        raise ValueError("Argument n for function count_ngrams must be greater than or equal to 0")
    most_frequent_ngrams_list = []
    if num == 0 or len(ngram_count_dict) == 0:
        return most_frequent_ngrams_list
        
    count_ngram_list = [(value, key) for key, value in ngram_count_dict.items()]
    count_ngram_list.sort(key=lambda item: item[0])
    
    list_len = len(count_ngram_list)
    for index in range(list_len - num, list_len):
        most_frequent_ngrams_list.append(count_ngram_list[index][1])
    most_frequent_ngrams_list.reverse()
    return most_frequent_ngrams_list