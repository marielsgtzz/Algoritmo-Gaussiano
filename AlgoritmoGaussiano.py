#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 14:44:02 2022

@author: marielsgtzz
"""
import numpy as np

#Imprime la representación gráfica de una matriz
def imprimirMatriz(m):
    a = np.array(m)
    for line in a:
        print ('  '.join(map(str, line)))

#Convierte un sistema de ecuaciones a una matriz mediante inputs del usuario
def sistemaMatriz():
    cantVar = int(input("Cuántas variables tiene el sistema de ecuaciones?"))
    cantEc = int(input("Cuántas ecuaciones (renglones) tiene el sistema de ecuaciones?")) 
    matriz = []
    for j in range(0,cantEc):
        ec = []
        for i in range(0,cantVar):
            elem = int(input("Cuál es el coeficiente de la variable "+str(i+1)+", de la ecuación "+str(j+1)+"?"))
            ec.append(elem)
        res = int(input("Cuál es el resultado de la ecuación "+str(j+1)+"?"))
        ec.append(res)
        matriz.append(ec)
    return matriz

#Para hacer la matriz una matriz escalonada
def algoGaussiano(m):
    #Imprime la matriz como se recibió
    imprimirMatriz(m)
    
    #Encontrar la fila que tenga el primer (comparando columnas de izq a der) elemento diferente a cero
    filaPrin = filaPrincipal(m)
    filaP = filaPrin[0]
    pivote = filaPrin[1]
    print(filaP,pivote)
    print("\nLa fila principal es la "+str(filaP+1)+". R"+str(filaP+1)+"<-->R1\n")
    
    if filaP == -1:
        return "Matriz de ceros" 
    
    #Se mueve ese renglón a R1
    m[0], m[filaP] = m[filaP], m[0]
    imprimirMatriz(m)
    
    #Dividir el renglón principal por el valor del pivote para hacer al pivote 1
    for cantVar in range(0,len(m[0])):
        if cantVar != 0:
           m[0][cantVar] = round(m[0][cantVar]/pivote, 2)
    print("\nSe divide R1 entre "+str(pivote)+" para hacer al pivote 1\n")
    imprimirMatriz(m)
           
           
    pass

#Pasos:
     
#Regresa el renglón de la matriz que representa la fila principal. Regresa -1 si es una matriz de ceros
def filaPrincipal(m):
    var = 0 #columnas
    while var < len(m[0])-1:
        ec = 0 #renglones
        while ec < len(m) and m[ec][var]==0:
            ec += 1
        
        if ec == len(m) and m[ec-1][var]==0:
            var += 1
        elif m[ec][var]!=0:
            return [ec,m[ec][var]]
    return [-1 ,-1]   

    
#definir matriz
matriz1 = [[1,-1,-1,2],
          [3,-3,2,16],
          [2,-1,1,9]]

matriz2 = [[0,1,-5,8],
          [1,1,-1,4],
          [2,1,3,0]]

matriz3 = [[0,0,0,8],
          [0,0,0,4],
          [0,0,1,0]]

matriz4 = [[0,0,0,8],
          [0,3,0,7],
          [0,0,1,5]]

matriz5 = [[0,0,0,0],
          [0,0,0,4],
          [0,0,0,0]]

#print(matriz4[1]/3)
algoGaussiano(matriz4)


