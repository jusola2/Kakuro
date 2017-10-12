#'''
#Created on Oct 4, 2017
#
#@author: Eduard
#'''

from random import randint
from time import time

tablero = []
vector = []

def crearMatriz(n):
    for i in range(0, n):
        vector = []
        for j in range(0, n):
            if i == 0 or j == 0 or i == n-1 or j == n-1:
                vector.append(0)
            else:
                vector.append(randint(0, 1))
        tablero.append(vector)
    validarMatriz(n)
    for k in range(0, n):
        print(tablero[k])
    print(espaciosFilas(tablero))
    print(espaciosVerticales(tablero))

def validarMatriz(n):
    for i in range(2, n-1):
        for j in range(1, n-1):
            if tablero[i][j-1] == 1 and tablero[i-1][j-1] == 0:
                tablero[i][j] = 1

def espaciosFilas(pMatrix):
    start_time = time()
    #lista de tuplas (numeroFila,columna donde empieza el espacio ,cantidad de espacios)
    listaEspaciosHorizontales=[]
    contador=0
    for contador in range( len(pMatrix)):
        contadorTemp=0
        while contadorTemp < (len(pMatrix[contador])):
            if pMatrix[contador][contadorTemp]==1:
                columnaInicio=contadorTemp
                num=1
                termino=True
                contadorTemp+=1
                while termino:
                    if (contadorTemp<len(pMatrix[contador])and pMatrix[contador][contadorTemp]==1):
                        num+=1
                        contadorTemp+=1
                    else:
                        termino=False
                        contadorTemp+=1
                if(num>1):
                    listaEspaciosHorizontales.append((contador,columnaInicio,num))
                        
            else:
                contadorTemp+=1
        contador+=1
    elapsed_time = time() - start_time
    print("Duro en mili",elapsed_time)
    return listaEspaciosHorizontales

def espaciosVerticales(pMatrix):
    start_time = time()
    #lista de tuplas (numeroFila,columna donde empieza el espacio ,cantidad de espacios)
    listaEspaciosVerticales=[]
    contador=0
    for contador in range( len(pMatrix)):
        contadorTemp=0
        while contadorTemp < (len(pMatrix)):
            if pMatrix[contadorTemp][contador]==1:
                filaInicio=contadorTemp
                num=1
                termino=True
                contadorTemp+=1
                while termino:
                    if (contadorTemp<len(pMatrix)and pMatrix[contadorTemp][contador]==1):
                        num+=1
                        contadorTemp+=1
                    else:
                        termino=False
                        contadorTemp+=1
                if(num>1):
                    listaEspaciosVerticales.append((filaInicio, contador, num))
                        
            else:
                contadorTemp+=1
        contador+=1
    elapsed_time = time() - start_time
    print("Duro en mili",elapsed_time)
    return listaEspaciosVerticales

crearMatriz(10)
