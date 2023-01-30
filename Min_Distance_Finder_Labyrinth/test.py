#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practica 5 - Algoritmica y Complejidad
(updated 14-may)
Coments:    Test para la practica 5.
@author:    Grupo E (Naiara Alonso, Pablo Goitia, Juan Romon)

"""
import P5_ALG
import random
import time
from datetime import datetime
import matplotlib.pyplot as plt

# Posiciones (ctes)
CAMINO = 0
MURO = -1
SALIDA = -2
    
def main():
    print(txtcolors.HEADER + "Running program...\n" + txtcolors.ENDC)
    print(txtcolors.UNDERLINE + "Probando caso del enunciado...\n" 
          + txtcolors.ENDC)
    print("VUELTA ATRÁS:")
    prueba_enunciado(0)
    print("RAMIFICACIÓN Y PODA:")
    prueba_enunciado(1)
    
    print(txtcolors.UNDERLINE + "Probando caso aleatorio...\n"
          + txtcolors.ENDC)
    print("VUELTA ATRÁS:")
    prueba_aleatorio(0)
    print("RAMIFICACIÓN Y PODA:")
    prueba_aleatorio(1)
    
    print(txtcolors.UNDERLINE + "Generando gráfica...\n"
          + txtcolors.ENDC)
    genera_grafica()
    print("La gráfica debería estar en el directorio de origen.")

class txtcolors:
    """ Color list for console output. """
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'
    
def prueba_enunciado(rp = False):
    f = 5; c = 10
    inicio_x = 1; inicio_y = 3
    salida_x = 1; salida_y = 9
    
    L = [[CAMINO for i in range(c)] for j in range(f)]
    for i in range(f):
        if i == 0 or i == f - 1:
            for j in range(c):
                L[i][j] = MURO
        else:
            L[i][0] = MURO
            L[i][c - 1] = MURO
    for i in range(f):
        if i == 0 or i == f - 1:
            for j in range(c):
                L[i][j] = MURO
        else:
            L[i][0] = MURO
            L[i][c - 1] = MURO
    
    for j in range(2, c - 2, 1):
        L[2][j] = MURO
    L[1][3] = MURO
    L[salida_x][salida_y] = SALIDA
    
    print(txtcolors.OKCYAN + "Input:" + txtcolors.ENDC)
    print_laberinto(L, f, c)
    
    if rp:
        L = P5_ALG.laberinto_rp(L, inicio_x, inicio_y)
    else:
        L = P5_ALG.laberinto_va(L, inicio_x, inicio_y)
    
    print(txtcolors.OKCYAN + "Output:" + txtcolors.ENDC)
    print_laberinto(L, f, c)

def laberinto_grafica(order):
    ini_x = ini_y = order // 2
    L = [[MURO for i in range(order)] for j in range(order)]
    
    for i in range(1, order - 1):
        L[i][ini_y] = CAMINO
        
    for j in range(1, order - 1):
        L[ini_x][j] = CAMINO
    
    L[ini_x][order - 1] = SALIDA
    
    return L, ini_x, ini_y

def crea_laberintos (f, c):
    L = [[None for i in range(c)] for j in range(f)]
    
    max_muros = (f * c) * 0.5
    muros_actuales = 0
    
    for i in range(f):
        for j in range(c):
            if i == 0 or i == f - 1 or j == 0 or j == c - 1:
                L[i][j] = MURO
                muros_actuales += 1
            elif (muros_actuales > max_muros):
                L[i][j] = CAMINO
            else:  
                casilla = random.randint(MURO, CAMINO)
                L[i][j] = casilla
                if (casilla == MURO):
                    muros_actuales += 1
    # Despues de generar el laberinto, colocamos una salida 
    aleatorio = random.randint(1,4)
    if  aleatorio == 1: #la salida esta en la parte de arriba
        posAleatoria = random.randint(1, c - 2)
        L[0][posAleatoria] = SALIDA
    elif aleatorio == 2: #la salida esta en la parte de abajo
        posAleatoria = random.randint(1, c - 2)
        L[f - 1][posAleatoria] = SALIDA
    elif aleatorio == 3: #la salida esta en la parte de la izquierda
        posAleatoria = random.randint(1, f - 2)
        L[posAleatoria][0] = SALIDA
    elif aleatorio == 4: #la salida esta en la parte de la derecha
        posAleatoria = random.randint(1, f - 2)
        L[posAleatoria][c - 1] = SALIDA
    return L

def pos_inicio(L):
    f = len(L); c = len(L[0])
    determinado = False
    x = y = 0
    while determinado == False:
        x = random.randint(1, c - 1)
        y = random.randint(1, f - 1)
        if L[y][x] == CAMINO:
            determinado = True
    return x,y

def prueba_aleatorio(rp = False):
    labret = None
    
    while labret == None:
        f = random.randint(6,9)
        c = random.randint(5,10)
    
        L = crea_laberintos(f, c)
        xIni, yIni = pos_inicio(L)
        if rp:
            labret = P5_ALG.laberinto_rp(L, xIni, yIni)
        else:
            labret = P5_ALG.laberinto_va(L, xIni, yIni)
        
    print("Filas -> " + str(f) + " | Columnas -> " + str(c))
    print(txtcolors.OKCYAN + "Output:" + txtcolors.ENDC)
    print_laberinto(labret, f, c)
    
def genera_grafica():
    """ Generates the graph of execution times. """
    min_order = 10
    max_order = 5000
    step = 100
    step_rec = []
    time_va = []
    time_rp = []
    
    for i in range(min_order, max_order + min_order + 1, step):
        step_rec.append(i)
        
        L, ini_x, ini_y = laberinto_grafica(i)
        L2, ini_x, ini_y = laberinto_grafica(i)
        
        start_time = time.time()
        P5_ALG.laberinto_va(L, ini_x, ini_y)
        time_va.append(time.time() - start_time)
        
        start_time = time.time()
        P5_ALG.laberinto_rp(L2, ini_x, ini_y)
        time_rp.append(time.time() - start_time)
        
    #Generate graph
    fig, ax = plt.subplots()
    plt.title("Time-order relation")
    plt.xlabel("Amount")
    plt.ylabel("Time (s)")
    ax.plot(step_rec, time_va, color='red', label="laberinto_va()")
    ax.plot(step_rec, time_rp, color='blue', label="laberinto_rp()")
    ax.legend()
    #Datetime object that contais current date and time
    now = datetime.now()
    dt = now.strftime("%d-%m-%Y_%H-%M-%S")
    plt.savefig(f'results_{dt}.png', dpi = 150)
    
    
def print_laberinto(L, f, c):
    for i in range(f):
        for j in range(c):
            if (L[i][j] == MURO):
                print("X", end="  ")
            elif (L[i][j] == CAMINO):
                print("-", end="  ")
            elif (L[i][j] == SALIDA):
                print("#", end="  ")
            elif (L[i][j] > 0):
                print(L[i][j], end="  ")
        print()
    print()

main()