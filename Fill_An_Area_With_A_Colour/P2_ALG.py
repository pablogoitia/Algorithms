#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practica 2 - Algoritmica y Complejidad
(updated 14-mar)
Coments:    Algoritmo rellenar.
@author:    Grupo E (Naiara Alonso, Pablo Goitia, Juan Romon)

"""

def rellenar(matrix, x, y, c):
    filas = len(matrix) - 1 
    columnas = len(matrix[0]) - 1 
    bolsa = []
    bolsa.append([x,y])
    while (len(bolsa) != 0):
        v = bolsa.pop()
        xcord = v[0]
        ycord = v[1]
        if (matrix[xcord][ycord] != c):
            'Coloreamos la casilla'
            matrix[xcord][ycord] = c
            'Introducimos en la volda las casillas adyacentes no coloreadas'
            'CASILLA DE ENCIMA'
            xAd = xcord 
            yAd = ycord - 1
            if ((yAd >= 0) and (matrix[xAd][yAd]  != c)):
                bolsa.append([xAd, yAd])
            'CASILLA DE LA DERECHA'
            xAd = xcord + 1
            yAd = ycord  
            if ((xAd <= filas) and (matrix[xAd][yAd]  != c)):
                 bolsa.append([xAd, yAd])
            'CASILLA DE DEBAJO'
            xAd = xcord 
            yAd = ycord + 1
            if ((yAd <= columnas) and (matrix[xAd][yAd]  != c)):
                bolsa.append([xAd, yAd])
            'CASILLA DE LA DERECHA'
            xAd = xcord - 1
            yAd = ycord  
            if ((xAd >= 0 )and (matrix[xAd][yAd]  != c)):
                bolsa.append([xAd, yAd])

    return matrix