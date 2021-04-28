#!/usr/bin/env python
# -*-coding: utf-8 -*-

#main.py
#Mohammad Saleheen
#CREATED: 04-20-2021
import timeit, random, searching_algorithms

# initialize a sorted list and pick a random element
number_of_elements = int(input('Enter the number of array elements: '))
initial_list = random.sample(range(10*number_of_elements), number_of_elements)
initial_list.sort()
element = random.choice(initial_list)

#print(initial_list)
algo = searching_algorithms.Search(initial_list, element)

print('Index of element {} using linear search: {}'.format(element, algo.linear_search()))
print('Index of element {} using binary search (loop): {}'.format(element, algo.binary_search_loop()))
print('Index of element {} using binary search (recursive): {}'.format(element, algo.binary_search_recursive()))
print('Index of element {} using interpolation search: {}'.format(element, algo.interpolation_search()))
