#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practica 4 - Algoritmica y Complejidad
(updated 16-abr)
Coments:    Revisado.
@author:    Grupo E (Naiara Alonso, Pablo Goitia, Juan Romon)

"""

g_table = []

def change(currency, amount, mode = 0):
    """
    Uses diferent change methods

    Parameters
    ----------
    currency : array
        value of coins on determinated monetary system.
    amount : int
        amount of money to give change.
    mode : int
        0 (default):
            bottom up algorithm.
        1:
            top down algorithm.
        2:
            voracious algorithm.
            
    Returns
    -------
    change : array
        number of coins of each value.

    """
    # User error management
    if (amount < 0):
        return -1
    
    # Algorithm selection
    if (mode == 0):
        table = build_table_bottom_up(currency, amount)
    elif (mode == 1):
        build_table_top_down(currency, amount)
        table = g_table
    elif (mode == 2):
        return voracious(currency, amount)
    else:
        return -1
    
    #debug_print_table(table)
    
    change = [0] * len(currency)
    
    if (amount == 0):
        return change
    
    # Common path for bottom-up and top-down
    i = len(currency) - 1
    while (i >= 0 and amount > 0):
        if (i == 0):
            change[i] += amount
            amount = 0
        if (table[i][amount] == table[i - 1][amount]):
            i -= 1
        else:
            amount -= currency[i]
            change[i] += 1
            
    return change

def build_table_bottom_up(currency, amount):
    """
    Bottom up algorithm to create table

    Parameters
    ----------
    currency : array
        value of coins on determinated monetary system.
    amount : int
        amount of money to give change.

    Returns
    -------
    table : matrix
        table with minimun coins for each value.
    """
    # Table initialization
    table = [[0 for x in range(amount + 1)] for y in range(len(currency))]
    
    # Filling the table
    # Base case: Coin with value '1'
    for i in range(amount + 1):
        table[0][i] = i
    
    for i in range(1, len(currency)):
        coin = currency[i]
        for j in range(amount + 1):
            # Other base case: 
            if coin == j:
                table[i][j] = 1
            # If not the above base cases
            elif coin > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = min(table[i - 1][j], 1 + table[i][j - coin])
    
    return table

def build_table_top_down(currency, amount):
    """
    Top down algorithm to create table

    Parameters
    ----------
    currency : array
        value of coins on determinated monetary system.
    amount : int
        amount of money to give change.

    Returns
    -------
    None.

    """
    # Table initialization
    global g_table #declaration avoids "unused variable" warnings
    g_table = [[0 for x in range(amount + 1)] for y in range(len(currency))]
    
    # Filling the table (recursive calls)
    build_table_top_down_rec(currency, amount, len(currency) - 1)

def build_table_top_down_rec(currency, amount, index):
    """
    Top down: recursive calls. Fills the fields of a table declared as 
    a global variable.

    Parameters
    ----------
    currency : array
        value of coins on determinated monetary system.
    amount : int
        amount of money to give change.
    index : int
        index of the next coin to evaluate.

    Returns
    -------
    new table field: int

    """
    
    if g_table[index][amount] == 0: #The value hasn't been calculated yet
        coin = currency[index]
        
        # Base cases
        if index == 0: #Equivalent to "coin == 1"
            g_table[index][amount] = amount
        elif coin == amount:
            g_table[index][amount] = 1
        
        # If not the above base cases
        elif (index > 0):
            if coin > amount:
                g_table[index][amount] = build_table_top_down_rec(currency, amount, index - 1)
            else:
                g_table[index][amount] = min(build_table_top_down_rec(currency, amount, index - 1), 
                                         1 + build_table_top_down_rec(currency, amount - coin, index))
    
    return g_table[index][amount]

def voracious(currency, amount):
    """
    Calculate the change based on the highest possible coins.

    Parameters
    ----------
    currency : array
        value of coins on determinated monetary system.
    amount : int
        amount of money to give change.

    Returns
    -------
    change : array
        number of coins of each value.

    """

    i = len(currency) - 1 #Counter that points to the last element of the array
    change = [0] * len(currency)
    
    if (amount == 0):
        return change

    while (amount > 0):
        if (amount >= currency[i]):
            change[i] += 1
            amount -= currency[i]
        else:
            i -= 1

    return change

def debug_print_table(table):
    """
    Prints the table. Debugging function.

    Parameters
    ----------
    table : matrix
        table to print.

    Returns
    -------
    None.

    """
    for i in range(len(table)):
        for j in range(len(table[0])):
            print(table[i][j], end="   ")
        print("\n")