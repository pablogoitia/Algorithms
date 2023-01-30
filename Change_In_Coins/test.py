#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practica 4 - Algoritmica y Complejidad
(updated 17-abr)
Coments:    Test para la practica 4.
@author:    Grupo E (Naiara Alonso, Pablo Goitia, Juan Romon)

"""
import P4_ALG
import time
from datetime import datetime
import matplotlib.pyplot as plt
import sys

# Divisas (ctes)
OLD_ENGLISH = [1, 4, 6, 12, 24, 30]
EURO = [1, 2, 5, 10, 20, 50]

# Otras constantes
MAX_AMOUNT = 500

class txtcolors:
    """ Color list for console output. """
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
    
def test(amount, currency, output = False):
    """
    Verifies if the change of a determined amount of a monetary system is
    correct.
    Arguments:
        amount: amount of money to give change
        currency: value of coins on determinated monetary system
        output: True to print results (default: False)
    Returns:
        None.
    """
    correct = False
    cambio1 = P4_ALG.change(currency, amount)
    cambio2 = P4_ALG.change(currency, amount, 1)
    cambio3 = P4_ALG.change(currency, amount, 2)
    if output: print("Bottom-Up: " + str(cambio1) + "\nTop-Down:  " + 
                     str(cambio2) + "\nVoracious: " + str(cambio3))
    
    if cambio1 == cambio2 and comprobar_suma(cambio1, cambio2, cambio3, currency):
        if output: print(txtcolors.OKGREEN + "[OK]\n" + txtcolors.ENDC)
        correct = True
    else:
        if output: print(txtcolors.FAIL + "[FAIL]\n" + txtcolors.ENDC) 
    return correct
    
def random_test(max_amount, currency):
    """
    Checks if the algorithms work correctly for a set of values.
    Arguments:
        max_amount: maximum amount of money to give change
        currency: value of coins on determinated monetary system
    Returns:
        Number of failures.
    """
    failures = 0
    for amount in range(max_amount):
        if not (test(amount, currency)):
            failures += 1
            
    return failures
    
def comprobar_suma(cambio1, cambio2, cambio3, currency):
    """
    Check that the total sum is the same for all three change return
    algorithms.
    Arguments:
        cambio1: results from bottom-up.
        cambio2: results from top-down.
        cambio3: results from voracious
        sistema_monetario: value of coins on determinated monetary system
    Returns:
        boolean: True if the sum is correct, False otherwise.
    """
    suma1 = 0
    suma2 = 0
    suma3 = 0
    for i in range(len(currency)):
        moneda = currency[i]
        suma1 += cambio1[i] * moneda
        suma2 += cambio2[i] * moneda
        suma3 += cambio3[i] * moneda
    if suma1 == suma2 == suma3:
        return True
    return False

def graphics(currency, currency_name):
    """ Generates the graph of execution times. """
    
    min_amount = 1
    max_amount = 4000
    step = 50
    step_rec = []
    time_bottom_up = []
    time_top_down = []
    time_voracious = []
    
    for i in range(min_amount, max_amount + 1, step):
        #print(f'Executing step #{i}')
        step_rec.append(i)
        
        start_time = time.time()
        P4_ALG.change(currency, i)
        time_bottom_up.append(time.time() - start_time)
        
        start_time = time.time()
        P4_ALG.change(currency, i, 1)
        time_top_down.append(time.time() - start_time)
        
        start_time = time.time()
        P4_ALG.change(currency, i, 2)
        time_voracious.append(time.time() - start_time)
        
    #Generate graph
    fig, ax = plt.subplots()
    plt.title(f'Time-amount relation ({currency_name})')
    plt.xlabel("Amount")
    plt.ylabel("Time (s)")
    ax.plot(step_rec, time_bottom_up, color='red', label="bottom_up()")
    ax.plot(step_rec, time_top_down, color='blue', label="top_down()")
    ax.plot(step_rec, time_voracious, color='green', label="voracious()")
    ax.legend()
    #Datetime object that contais current date and time
    now = datetime.now()
    dt = now.strftime("%d-%m-%Y_%H-%M-%S")
    plt.savefig(f'results_{currency_name}_{dt}.png', dpi = 150)

def main():
    """
    Main to execute the program

    Returns
    -------
    None.

    """
    print(txtcolors.HEADER + "Running program...\n" + txtcolors.ENDC)
    limit = sys.getrecursionlimit()
    sys.setrecursionlimit(30000) # Ajusta temporalmente el limite de recursion
    
    # Test basicos
    print(txtcolors.UNDERLINE + "TEST 1:" + txtcolors.ENDC)
    test(8, OLD_ENGLISH, 1)
    print(txtcolors.UNDERLINE + "TEST 2:" + txtcolors.ENDC)
    test(51, EURO, 1)
    
    # Random test
    print(txtcolors.UNDERLINE + "RANDOM TEST (old english):" + txtcolors.ENDC)
    print(f'{txtcolors.OKCYAN}Fallos: {random_test(MAX_AMOUNT, OLD_ENGLISH)}' +
          f' / {MAX_AMOUNT}{txtcolors.ENDC}')
    print(txtcolors.UNDERLINE + "RANDOM TEST (euro):" + txtcolors.ENDC)
    print(f'{txtcolors.OKCYAN}Fallos: {random_test(MAX_AMOUNT, EURO)}' +
          f' / {MAX_AMOUNT}{txtcolors.ENDC}')
    
    # Generacion de grafica en funcion de los valores de "cambio"
    print("\nGenerando graficas...")
    graphics(OLD_ENGLISH, "old english")
    graphics(EURO, "euro")
    print(txtcolors.OKCYAN + "Las graficas deberian haberse guardado en el " +
          "directorio." + txtcolors.ENDC)
        
    print("\nPuedes (des)habilitar la impresion de tablas (des)comentando en" + 
          " 'change' la funcion 'debug_print_table'.")
    
    sys.setrecursionlimit(limit) # Restablece el limite de recursion del motor

main()
    