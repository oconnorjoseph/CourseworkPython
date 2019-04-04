#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Joseph O'Connor
UNI: jgo2115
"""
import numpy as np
from matplotlib import pyplot as plt

def euclidean_distance(a,b):
    diff = a - b
    return np.sqrt(np.dot(diff, diff))

def load_data(csv_filename):
    """ 
    Returns a numpy ndarray in which each row repersents
    a wine and each column represents a measurement. There should be 11
    columns (the "quality" column cannot be used for classificaiton).
    """
    return np.genfromtxt(csv_filename, delimiter=';', skip_header=1, usecols=range(0, 11))

def split_data(dataset, ratio = 0.9):
    """
    Return a (train, test) tuple of numpy ndarrays. 
    The ratio parameter determines how much of the data should be used for 
    training. For example, 0.9 means that the training portion should contain
    90% of the data. You do not have to randomize the rows. Make sure that 
    there is no overlap. 
    """
    test_index_int = int(ratio * len(dataset))
    return dataset[:test_index_int], dataset[test_index_int:]

def compute_centroid(data):
    """
    Returns a 1D array (a vector), representing the centroid of the data
    set. 
    """
    return data.sum(0) / len(data)
    
def experiment(ww_train, rw_train, ww_test, rw_test):
    """
    Train a model on the training data by creating a centroid for each class.
    Then test the model on the test data. Prints the number of total 
    predictions and correct predictions. Returns the accuracy. 
    """
    ww_centroid = compute_centroid(ww_train)
    rw_centroid = compute_centroid(rw_train)
    
    correct_int, incorrect_int = 0, 0
    for datum in ww_test:
        if euclidean_distance(datum, ww_centroid) <= euclidean_distance(datum, rw_centroid):
            correct_int += 1
        else:
            incorrect_int += 1
    for datum in rw_test:
        if euclidean_distance(datum, rw_centroid) <= euclidean_distance(datum, ww_centroid):
            correct_int += 1
        else:
            incorrect_int += 1
    
    total_int = correct_int + incorrect_int
    accuracy_float = correct_int / total_int
    approx_str = " approximately"
    rounded_accuracy_float = round(accuracy_float, 6)
    if accuracy_float - rounded_accuracy_float <= 1e-10:
        approx_str = ""
        
    print("The model made {} predictions.".format(correct_int + incorrect_int))
    print("{} of those predictions were correct, and {} were incorrect.".format(correct_int, incorrect_int))
    print("Thus, the model has an accuracy of{} {:0.4f}%.".format(approx_str, accuracy_float * 100))        
    return accuracy_float
    
def learning_curve(ww_training, rw_training, ww_test, rw_test):
    """
    Perform a series of experiments to compute and plot a learning curve.
    """
    np.random.shuffle(ww_training)
    np.random.shuffle(rw_training)
    dif_int = len(ww_training) - len(rw_training)
    if dif_int < 0:
        dif_int = 0
    lower_size_int = len(ww_training) - dif_int
    accuracy_array = np.empty((lower_size_int, 2))
        
    for n_trial in range(1, lower_size_int + 1):
        accuracy_array[n_trial - 1] = [n_trial, 100 * experiment(ww_training[:n_trial], rw_training[:n_trial], ww_test, rw_test)]
    
    plt.title("Learning Curve")
    plt.xlabel("Number of Training Items")
    plt.ylabel("Accuracy (%)")
    plt.plot(accuracy_array[:, 0], accuracy_array[:, 1])    
    
def cross_validation(ww_data, rw_data, k):
    """
    Perform k-fold crossvalidation on the data and print the accuracy for each
    fold.
    """
    dif_int = len(ww_data) - len(rw_data)
    if dif_int < 0:
        dif_int = 0
    lower_size_int = len(ww_data) - dif_int
    
    partition_size = lower_size_int / k
    extra_ww_data, extra_rw_data = list(), list()
    truncated_partition_size = int(partition_size)
    if partition_size - truncated_partition_size > 1e10: 
        extra_ww_data = list(ww_data[truncated_partition_size * k:])
        extra_rw_data = list(rw_data[truncated_partition_size * k:])
    partition_size = truncated_partition_size
    accuracy_array = np.empty(k)
      
    for n_fold in range(0, k):
        ww_training_data = np.asarray(list(ww_data[0:n_fold * partition_size]) + list(ww_data[0:(n_fold + 1) * partition_size]) + extra_ww_data)
        rw_training_data = np.asarray(list(rw_data[0:n_fold * partition_size]) + list(rw_data[0:(n_fold + 1) * partition_size]) + extra_rw_data)
        
        ww_testing_data = ww_data[n_fold * partition_size: (n_fold + 1) * partition_size]
        rw_testing_data = rw_data[n_fold * partition_size: (n_fold + 1) * partition_size]
        
        accuracy_float = experiment(ww_training_data, rw_training_data, ww_testing_data, rw_testing_data)
            
        print("The accuracy of fold #{} is {}.".format(n_fold, accuracy_float))
        accuracy_array[n_fold] = accuracy_float
    
    return accuracy_array.sum() / k

    
if __name__ == "__main__": 
    x = np.array([[1,2,3,4,5], [2,3,4,5,6], [3,4,5,6,7]])
    print(x[[0,2]])
    
    ww_data = load_data('whitewine.csv')
    rw_data = load_data('redwine.csv')

    # Uncomment the following lines for step 2: 
    ww_train, ww_test = split_data(ww_data, 0.91)
    rw_train, rw_test = split_data(rw_data, 0.91)
    print(experiment(ww_train, rw_train, ww_test, rw_test))
    
    # Uncomment the following lines for step 3
    ww_train, ww_test = split_data(ww_data, 0.9)
    rw_train, rw_test = split_data(rw_data, 0.9)
    learning_curve(ww_train, rw_train, ww_test, rw_test)
    
    # Uncomment the following lines for step 4:
    k = 10
    acc = cross_validation(ww_data, rw_data, k)
    print("{}-fold cross-validation accuracy: {}".format(k,acc))
    