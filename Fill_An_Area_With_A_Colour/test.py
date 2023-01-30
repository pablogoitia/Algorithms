#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practica 2 - Algoritmica y Complejidad
(updated 20-mar)
Coments:    Test para la practica 2.
@author:    Grupo E (Naiara Alonso, Pablo Goitia, Juan Romon)

"""

import P2_ALG
import time
from datetime import datetime
import matplotlib.pyplot as plt


def test_rellenar(input_map, x, y, c):
    print("INPUT:")
    for i in range(len(input_map)):
        print(input_map[i])
    output_map = P2_ALG.rellenar(input_map, x, y, c)
    print("OUTPUT:")
    for i in range(len(output_map)):
        print(input_map[i])
    
def graph_generator_matrix1():
    # Generate matrix and set default colored fields
    min_size = 5
    max_size = 500
    step = 20
    step_rec = []
    time_rellena = []
    
    for i in range(min_size, max_size + 1, step):
        step_rec.append(i)
        matrix = [[0 for x in range(i)] for y in range(i)]
        for j in range(i):
            matrix[j][j] = 1
            
        start_time = time.time()
        P2_ALG.rellenar(matrix, 0, i - 1, 1)
        stop_time = time.time()
        time_rellena.append(stop_time - start_time)
    
    #Generate graph
    fig, ax = plt.subplots()
    plt.title("Time-size relation (diagonal)")
    plt.xlabel("Matrix size")
    plt.ylabel("Time (s)")
    ax.plot(step_rec, time_rellena, color='blue', label="rellena()")
    ax.legend()
    #Datetime object that contais current date and time
    now = datetime.now()
    dt = now.strftime("%d-%m-%Y_%H-%M-%S")
    plt.savefig("results_%s.png" % dt, dpi = 150)
    
def graph_generator_matrix2():
    # Generate matrix and set default colored fields
    min_size = 5
    max_size = 1000
    step = 20
    step_rec = []
    time_rellena = []
    
    for i in range(min_size, max_size + 1, step):
        step_rec.append(i)
        matrix = [[0 for x in range(i)] for y in range(i)]
        for j in range(i):
            matrix[j][i - 2] = 1
            
        start_time = time.time()
        P2_ALG.rellenar(matrix, 0, i - 1, 1)
        stop_time = time.time()
        time_rellena.append(stop_time - start_time)
    
    
    #Generate graph
    fig, ax = plt.subplots()
    plt.title("Time-size relation (column)")
    plt.xlabel("Matrix size")
    plt.ylabel("Time (s)")
    ax.plot(step_rec, time_rellena, color='blue', label="rellena()")
    ax.legend()
    #Datetime object that contais current date and time
    now = datetime.now()
    dt = now.strftime("%d-%m-%Y_%H-%M-%S")
    plt.savefig("results_%s.png" % dt, dpi = 150)

def main():
    print("Running program...")
    print("\nTESTING EXERCISE 2:")
    input_map = [[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    test_rellenar(input_map, 2, 2, 1)
    input_map = [[0,1,1,1,1],[1,0,1,1,1],[1,1,0,1,1],[1,1,1,0,1]]
    test_rellenar(input_map, 1, 0, 0)
    input_map = [[0,0,0],[0,0,0],[0,0,0]]
    test_rellenar(input_map, 0, 0, 1)
    print("\nTESTING EXERCISE 3:")
    print("Generating the graphics. This operation could take a few minutes.")
    print("Note: it works better on Linux.")
    #graph_generator_matrix1()
    #graph_generator_matrix2()
    print("[OK] Graphics should have been saved in the source folder.")

main()
