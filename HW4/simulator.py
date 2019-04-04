#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Joseph O'Connor
UNI: jgo2115
"""
import random
import math
from matplotlib import pyplot as plt

def normpdf(x, mean, sd):
    """
    Return the value of the normal distribution 
    with the specified mean and standard deviation (sd) at
    position x.
    You do not have to understand how this function works exactly. 
    """
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def pdeath(x, mean, sd):
    start = x-0.5
    end = x+0.5
    step =0.01    
    integral = 0.0
    while start<=end:
        integral += step * (normpdf(start,mean,sd) + normpdf(start+step,mean,sd)) / 2
        start += step            
    return integral    
    
recovery_time = 4 # recovery time in time-steps
virality = 0.9    # probability that a neighbor cell is infected in 
                  # each time step 
death_mean = 4    # time step where probability of dying is highest (first step = 1)
death_sd = 1      # standard deviation of probability of dying in steps                                           

class Cell(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y 
        self.state = 'S' # can be 'S' (susceptible), 'R' (resistant = dead), or 
                         # 'I' (infected)
        self.counter = 0
        self.to_infect_bool = False
        
    def infect(self):
        self.state = 'I'
        self.to_infect_bool = False
        self.counter = recovery_time
        
    def recover(self):
        self.state = 'S'
    
    def process(self, adjacent_cells):
        if self.state != 'I':
            return
        
        self.counter -= 1
        if self.counter == 0:
                self.recover()
        elif random.random() < pdeath(recovery_time - self.counter, death_mean, death_sd):
                self.state = 'R'
        else:
            for adjacent_cell in adjacent_cells:
                if adjacent_cell.state == 'S' and random.random() <= virality:
                    adjacent_cell.to_infect_bool = True     

    def process_to_infect(self):
        if self.to_infect_bool:
            self.infect()
        
        
class Map(object):
    STATE_TO_COLOR_MAP = {'S': (0.0, 1.0, 0.0), 'R': (0.5, 0.5, 0.5), 'I': (1.0, 0.0, 0.0)}
    ADJACENT_ADJUSTS = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    
    def __init__(self):
        self.height = 150
        self.width = 150           
        self.cells = {}

    def add_cell(self, cell):
        self.cells[cell.x, cell.y] = cell
        
    def display(self): 
        pixel_table = []
        for y in range(self.height):
            pixel_table.append([])
            for x in range(self.width):
                coordinate_cell = self.cells.get((x, y))
                if coordinate_cell != None:
                    pixel_table[y].append(self.STATE_TO_COLOR_MAP[coordinate_cell.state])
                else:
                    pixel_table[y].append((0.0, 0.0, 0.0))
        
        plt.imshow(pixel_table)
    
    def adjacent_cells(self, x, y):
        adjacent_cells_list = []
        for adjust_tuple in self.ADJACENT_ADJUSTS:
            cell = self.cells.get((x + adjust_tuple[0], y + adjust_tuple[1]))
            if cell != None:
                adjacent_cells_list.append(cell)              
                
        return adjacent_cells_list
    
    def time_step(self):
        infected_cells_list = [cell for cell in self.cells.values() if cell.state == 'I']
        for cell in infected_cells_list:
            cell.process(self.adjacent_cells(cell.x, cell.y))
            
        for cell in self.cells.values():
            cell.process_to_infect()
            
        self.display()
      
def read_map(filename):
    """
    From a file in comma-separated value (.csv) format, creates a map specified 
    by a grid of pixels where each pixel represents a small, populated area of 
    individuals.
    The .csv file must contain a list of (y, x) values, where y is the y-value
    of the pixel and x is the x-value of the pixel. Do NOT list the .csv data
    in (x, y) order, and do NOT include (y, x) values for unpopulated pixels.
    """
    m = Map()
    
    cells_list = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                cell_y, cell_x = line.split(',')
                cells_list.append(Cell(int(cell_x), int(cell_y)))
    except ValueError:
        raise ValueError("file named '{}' from which to create map is not in comma-separated value format".format(filename))
    
    for cell in cells_list:
        m.add_cell(cell)
    
    return m
