#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practica 1 - Algoritmica y Complejidad
(updated 02-mar)
Coments:    Test para la practica 1.
@author:    Grupo E (Naiara Alonso, Pablo Goitia, Juan Romon)

"""

import P1_ALG
import time
from datetime import datetime
import random
import matplotlib.pyplot as plt


def test_radix_sort():
    print("\nTest 1:")
    to_sort = [10, 31, 16, 2, 22, 20]
    print("Input : " + str(to_sort))
    sorted_list = P1_ALG.radix_sort(to_sort, 2, 10)
    print("Output: " + str(sorted_list))
    
    print("\nTest 2:")
    to_sort = [6, 86, 81, 75, 49, 2]
    print("Input : " + str(to_sort))
    sorted_list = P1_ALG.radix_sort(to_sort, 2, 10)
    print("Output: " + str(sorted_list))
    
    print("\nTest 3:")
    to_sort = [76, 34, 0, 77, 12, 23]
    print("Input : " + str(to_sort))
    sorted_list = P1_ALG.radix_sort(to_sort, 2, 10)
    print("Output: " + str(sorted_list))
    
    print("\nTest 4:")
    to_sort = [50, 31, 26, 2, 20, 22]
    print("Input : " + str(to_sort))
    sorted_list = P1_ALG.radix_sort(to_sort, 2, 10)
    print("Output: " + str(sorted_list))

def test_registers():
    print("\nTest 1 (6 registers):")
    to_sort = [('AEU', 271), ('AAA', 143), ('EIA', 233), ('AIO', 145), ('AIO', 138)]
    print("Input : " + str(to_sort))
    start_time = time.time()
    sorted_list = P1_ALG.register_radix_sort(to_sort)
    stop_time = time.time()
    print("Output: " + str(sorted_list))
    print("Execution time: " + str(stop_time - start_time) + " seconds")
    
def graph_generator_elements():
    #Set initial parameters
    digit_number = 3
    element_number = 0
    step = 200 #200 recomended
    iter_number = 500 #500 recomended
    time_radix = [0] * iter_number
    time_sort = [0] * iter_number
    step_rec = []
    
    #Take runtime measurements and store them
    for n in range(iter_number):
        element_number += step
        step_rec.append(element_number)
        to_sort_radix = [0] * element_number
        
        for i in range(element_number):
            to_sort_radix[i] = random.randint(0, (10 ** digit_number) - 1)
            
        to_sort_sort = to_sort_radix[:]
            
        start_time = time.time()
        P1_ALG.radix_sort(to_sort_radix, digit_number, 10)
        stop_time = time.time()
        time_radix[n] = stop_time - start_time
        
        start_time = time.time()
        to_sort_sort.sort()
        stop_time = time.time()
        time_sort[n] = stop_time - start_time
    
    #Generate graph
    fig, ax = plt.subplots()
    plt.title("Time-element relation")
    plt.xlabel("Number of elements")
    plt.ylabel("Time (s)")
    ax.plot(step_rec, time_radix, color='blue', label="RadixSort")
    ax.plot(step_rec, time_sort, color='red', label="Python's sort()")
    ax.legend()
    #Datetime object that contais current date and time
    now = datetime.now()
    dt = now.strftime("%d-%m-%Y_%H-%M-%S")
    plt.savefig("element_results_%s.png" % dt, dpi = 150)
    
def graph_generator_digits():
    #Set initial parameters
    digit_number = 0
    element_number = 10
    step = 1 #1 recomended
    iter_number = 1000 #1000 recomended
    time_radix = [0] * iter_number
    time_sort = [0] * iter_number
    step_rec = []
    
    #Take runtime measurements and store them
    for n in range(iter_number):
        digit_number += step
        step_rec.append(digit_number)
        to_sort_radix = [0] * element_number
        
        for i in range(element_number):
            to_sort_radix[i] = random.randint(0, (10 ** digit_number) - 1)
            
        to_sort_sort = to_sort_radix[:]
            
        start_time = time.time()
        P1_ALG.radix_sort(to_sort_radix, digit_number, 10)
        stop_time = time.time()
        time_radix[n] = stop_time - start_time
        
        start_time = time.time()
        to_sort_sort.sort()
        stop_time = time.time()
        time_sort[n] = stop_time - start_time
    
    #Generate graph
    fig, ax = plt.subplots()
    plt.title("Time-digit relation")
    plt.xlabel("Number of digits per element")
    plt.ylabel("Time (s)")
    ax.plot(step_rec, time_radix, color='blue', label="RadixSort")
    ax.plot(step_rec, time_sort, color='red', label="Python's sort()")
    ax.legend()
    #Datetime object that contais current date and time
    now = datetime.now()
    dt = now.strftime("%d-%m-%Y_%H-%M-%S")
    plt.savefig("digit_results_%s.png" % dt, dpi = 150)

def main():
    print("Running program...")
    print("\nTESTING EXERCISE 1:")
    test_radix_sort()
    print("\nTESTING EXERCISE 2:")
    test_registers()
    print("\nTESTING EXERCISE 3:")
    print("Generating the graphics. This operation could take a few minutes.")
    graph_generator_elements()
    graph_generator_digits()
    print("[OK] Graphics should have been saved in the source folder.")

main()
