#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practica 1 - Algoritmica y Complejidad
(updated 03-mar)
Coments:    Apartado 3 terminado.
@author:    Grupo E (Naiara Alonso, Pablo Goitia, Juan Romon)

"""

def radix_sort(to_sort, digit_size, base):
    '''"Radix sort" algorithm based on base sorting.'''
    queue = [[] for q in range(base)]
    
    for i in range(digit_size):
        for j in range(len(to_sort)):
            d = (to_sort[j] // (base ** i)) % base
            queue[d].append(to_sort[j])
        
        #Save the numbers in the list, in reverse order.
        '''In this way, we improve the execution times in terms of
        the number of elements, saving the time it takes to extract
        the first element of a list (reordering time).'''
        j = len(to_sort)
        for d in range(base - 1, -1, -1):
            while (len(queue[d]) != 0):
                j -= 1
                to_sort[j] = queue[d].pop()
                
    return to_sort

def register_radix_sort(to_sort):
    #Convert the register into a numerical value
    value_dict = dict(zip('AEIOU', [1, 2, 3, 4, 5]))
    equivalent_list = []
    
    for i in range(len(to_sort)):
        eq_number = ''
        for j in (to_sort[i][0]):
            eq_number += str(value_dict.get(j))
        equivalent_list.append(int(eq_number + str(to_sort[i][1])))
    
    #Execute the sorting algorithm "RadixSort"
    equivalent_list = radix_sort(equivalent_list, 6, 10)
    
    #Convert the numerical value into a register again
    number_dict = dict(zip('12345',['A','E','I','O','U']))
    
    for i in range(len(equivalent_list)):
        #Create temporary register that will be added to the returned list
        tmp_register = []
        e1 = equivalent_list[i] // 1000
        e2 = equivalent_list[i] - (e1 * 1000)
    
        tmp_register.append(e1)
        tmp_register.append(e2)
        
        equivalent_list[i] = tmp_register
        
        vowels = ''
        nums = str(equivalent_list[i][0])
        for num in nums:
            vowels += number_dict.get(num)
        equivalent_list[i][0] = vowels
    
    return equivalent_list