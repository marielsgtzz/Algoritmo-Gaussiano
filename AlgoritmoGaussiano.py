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

#Regresa el renglón de la matriz que representa la fila principal y el pivote. Regresa -1, -1 si es una matriz de ceros
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

#Hacer ceros los elementos abajo de un uno principal 
def cerosDebajoPivote(m,n,l):
    for i in range(l+1,len(m)): #Recorre las columnas de la matriz empezando abajo del 1 principal
        mAux = m
        if m[i][n] != 0:
            multi = m[i][n] * -1
            print("\nMultiplicamos R"+str(l+1)+" por "+str(multi)+"\n")
            for j in range(0,len(mAux[i])):
                mAux[l][j] = m[l][j]*multi
            imprimirMatriz(mAux)
            for j in range(0,len(mAux[i])):
                m[i][j]+= mAux[l][j]
            print("\nSumamos R"+str(l+1)+" con R"+str(i+1)+" para tener cero abajo del 1 principal\n")
            for j in range(0,len(mAux[i])):
                m[l][j] = m[l][j]/multi
            imprimirMatriz(m) #Regresa al renglón principal a su estado antes de miltiplicarlo por el pivote
    return m
  
    
#Para hacer la matriz una matriz escalonada
def algoGaussiano(m):
    #Imprime la matriz como se recibió
    imprimirMatriz(m)
    
    for l in range(0,len(m)): #l = el renglón principal en el que estamos
        
    
        #Encuentra la fila que tenga el primer (comparando columnas de izq a der) elemento diferente a cero y da el valor de dicho elemento
        mAux = m[l:]
        filaPrin = filaPrincipal(mAux)
        filaP = filaPrin[0] + l
        pivote = filaPrin[1]
        
        if pivote != -1:
            print("\nLa fila principal es la "+str(filaP+1)+". R"+str(filaP+1)+"<-->R"+str(l+1)+"\n")
            #Se mueve ese renglón a R1
            m[l], m[filaP] = m[filaP], m[l]
            imprimirMatriz(m)
            
            #Dividir el renglón principal por el valor del pivote para hacer al pivote 1
            for cantVar in range(0,len(m[0])):
                if m[l][cantVar] != 0:
                    m[l][cantVar] = round(m[l][cantVar]/pivote, 2)
            print("\nSe divide R"+str(l+1)+" entre "+str(pivote)+" para hacer al pivote 1\n")
            imprimirMatriz(m)
            n = 0 #en qué columna está el primer 1 principal
            while m[l][n] == 0:
                 n += 1    
            m = cerosDebajoPivote(m, n, l)
            
        if filaP == -1:
            print("\nMatriz de ceros\n")
            break
        
    
    print("\nLa matriz ya está escalonada.\n")
    return
           

    
#definir matriz
matriz1 = [[4,-1,-1,2],
          [3,-3,2,16],
          [2,-1,1,9]]

matriz2 = [[0,1,-5,8],
          [2,1,-1,4],
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

algoGaussiano(matriz5)











