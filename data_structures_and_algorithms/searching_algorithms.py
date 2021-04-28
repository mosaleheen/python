#!/usr/bin/env python
# -*-coding: utf-8 -*-

# searching_algorithms
#Mohammad Saleheen
#CREATED: 04-20-2021
class Search:
    '''An object that includes different searching algorithms'''
    def __init__(self, array, element):
        self.array = array
        self.low = 0
        self.high = len(self.array) - 1
        self.element = element
        
    # linear search algorithm
    def linear_search(self):
        for index, item in enumerate(self.array):
            if item == self.element:
                return index
        return -1

    # binary search algorithm with loop
    def binary_search_loop(self):
        while self.high >= self.low:
            mid = (self.high + self.low) // 2
            if self.array[mid] == self.element:
                return mid
            elif self.array[mid] > self.element:
                self.high = mid - 1
            else:
                self.low = mid + 1
        return -1

    # binary search with recursion
    def binary_search_recursive(self):
        if self.high >= self.low:
            mid = (self.high + self.low) // 2
            if self.array[mid] == self.element:
                return mid
            elif self.array[mid] > self.element:
                self.high = mid - 1
                return binary_search_recursive(self)
            else:
                self.low = mid + 1 
                return binary_search_recursive(self)
        else:
            return -1

    def interpolation_search(self):
        while self.high >= self.low:
            if self.high == self.low:
                return self.low
            # this is my modified interpolation search
            pos = self.low + ((self.element - self.array[self.low]) * (self.high - self.low)) // (self.array[self.high] - self.array[self.low])
            if self.array[pos] == self.element:
                return pos
            elif self.array[pos] > self.element:
                self.high = pos - 1
            else:
                self.low = pos + 1
        return -1



