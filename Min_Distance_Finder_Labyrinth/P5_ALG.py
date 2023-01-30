#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practica 5 - Algoritmica y Complejidad
(updated 14-may)
Coments:    Revisado.
@author:    Grupo E (Naiara Alonso, Pablo Goitia, Juan Romon)

"""
import sys
from queue import PriorityQueue

# Movimientos (ctes)
DERECHA = 0
ABAJO = 1
IZQUIERDA = 2
ARRIBA = 3
NUM_MOVIMIENTOS = 4

# Posiciones (ctes)
CAMINO = 0
MURO = -1
SALIDA = -2

def laberinto_va(L, x, y):
    if r_laberinto_va(L, x, y, 1):
        return L
    return None

def r_laberinto_va(L, x, y, p): #p es el contenido de la casilla
    L[y][x] = p
    for i in range(NUM_MOVIMIENTOS):
        x1, y1 = mover(x, y, i)
        if es_factible(L, x1 , y1):
            if L[y1][x1] == SALIDA:
                return True
            if r_laberinto_va(L, x1, y1, p + 1):
                return True
    return False

def laberinto_rp(L, x, y):
    xFin, yFin = coord_salida(L)
    Lmejor = None
    Pmejor = sys.maxsize
    C = PriorityQueue()
    C.put((1, (L, x, y))) # Encola con prioridad
    while not C.empty(): # Mientras la cola no este vacia
        p , (L, x, y) = C.get() # Desencola prioritario
        L[y][x] = p
        for i in range (NUM_MOVIMIENTOS):
            x2, y2 = mover(x, y, i)
            ct = cota(L, x, y, xFin, yFin)
            if es_factible(L, x2, y2) and ct + p < Pmejor:
                if L[y2][x2] == SALIDA:
                    if p < Pmejor:
                        Lmejor = L
                        Pmejor = p
                else :
                    C.put((p + 1, (L, x2, y2))) # Encola con prioridad
    return Lmejor

def mover(x, y, i):
    if (i == DERECHA):
        return [x + 1, y]
    if (i == ABAJO):
        return [x, y + 1]
    if (i == IZQUIERDA):
        return [x - 1, y]
    if (i == ARRIBA):
        return [x, y - 1]

def es_factible(L, x, y):
    f = len(L); c = len(L[0])
    if y < 0 or y > f - 1 or x < 0 or x > c - 1:
        return False
    if L[y][x] == MURO or L[y][x] > 0:
        # mayor que cero implica ya visitado
        return False
    return True

def cota(L, xIni, yIni, xFin, yFin):
    #determinamos la cota minima -- manhattan distance
    return abs((xFin-xIni)+(yFin-yIni))

def coord_salida(L):
    f = len(L); c = len(L[0])
    for i in range(f):
        if L[i][0] == SALIDA:
            return (i, 0)
    for i in range(f):
        if L[i][c - 1] == SALIDA:
            return (i, f - 1)
    for j in range(c):
        if L[0][j] == SALIDA:
            return (0, j)
    for j in range(c):
        if L[f - 1][j] == SALIDA:
            return (c - 1, j)