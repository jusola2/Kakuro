#'''
#Created on Oct 4, 2017
#
#@author: Eduard, Juan
#'''

from random import randint, choices
from time import time

tablero = []
vector = []
consecutivosFilas = []
consecutivosColumnas = []
espacios = []

def kakuro(n):
    global tablero
    global espacios
    crearMatriz(n)
    valido = False
    while not valido:
        valido = validarEspacios(n)
    valores = None
    espacios=tablero
    reintentar=10
    while valores == None:
        valores = generarValores()
        reintentar-=1
        if reintentar==0:
            kakuro(n)
            return
    printMatriz(tablero)

def crearMatriz(n):
    global tablero
    global vector
    global consecutivosFilas
    global consecutivosColumnas
    global espacios
    tablero = []
    vector = []
    consecutivosFilas = []
    consecutivosColumnas = []
    espacios = []
    for i in range(0, n):
        vector = []
        for j in range(0, n):
            if i == 0 or j == 0:
                vector.append(0)
            else:
                vector.append(choices([0, 1],[0.05, 0.2])[0])
        tablero.append(vector)
##    while generarValores() == None:
##        crearMatriz(n)
##        return

def printMatriz(matriz):
    for n in range(0, len(matriz)):
        print(tablero[n])

def validarEspacios(n):
    global consecutivosFilas
    global consecutivosColumnas
    global tablero
    consecutivosFilas = espaciosFilas(tablero)
    consecutivosColumnas = espaciosColumnas(tablero)
    #Pone un espacio a la par del tablero en caso de estar solo
    for i in range(len(consecutivosFilas)):
        if consecutivosFilas[i][2]==1:
            for j in range(len(consecutivosColumnas)):
                if consecutivosFilas[i]==consecutivosColumnas[j]:
                    fila=consecutivosFilas[i][0]
                    columna=consecutivosFilas[i][1]
                    if (fila==1 or columna==1) and columna<n-1:
                        tablero[fila][columna+1]=1
                    else:
                        tablero[fila][columna-1]=1
                    return False
    #Revisa que no haya mas de 9 espacios seguidos horizontalmente
    for i in range(0, len(consecutivosFilas)):
        coord = consecutivosFilas[i]
        if coord[2]>9:
            tablero[coord[0]][coord[1]+randint(1, 9)]=0
            return False
    #Revisa que no haya mas de 9 espacios seguidos verticalmente
    for j in range(1, len(consecutivosColumnas)):
        coord = consecutivosColumnas[j]
        if coord[2]>9:
            tablero[coord[0]+randint(1, 9)][coord[1]]=0
            return False
    return True

# Revisa la fila en los espacios anteriores al numero que se desea insertar
def estaEnFila(fila, columna, n):
    global tablero
    while columna>0 and tablero[fila][columna]!=0:
        if tablero[fila][columna]==n:
            return True
        columna-=1
    return False

# Revisa la columna en los espacios anteriores al numero que se desea insertar
def estaEnColumna(fila, columna, n):
    global tablero
    while fila>0 and tablero[fila][columna]!=0:
        if tablero[fila][columna]==n:
            return True
        fila-=1
    return False

def espaciosFilas(pMatrix):
    #lista de tuplas (numeroFila,columna donde empieza el espacio ,cantidad de espacios)
    listaEspaciosHorizontales=[]
    contador=0
    for contador in range(len(pMatrix)):
        contadorTemp=0
        while contadorTemp < (len(pMatrix[contador])):
            if pMatrix[contador][contadorTemp]!=0:
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
                listaEspaciosHorizontales.append([contador,columnaInicio,num])
                        
            else:
                contadorTemp+=1
        contador+=1
    return listaEspaciosHorizontales

def espaciosColumnas(pMatrix):
    #lista de tuplas (numeroFila,columna donde empieza el espacio ,cantidad de espacios)
    listaEspaciosVerticales=[]
    contador=0
    for contador in range( len(pMatrix)):
        contadorTemp=0
        while contadorTemp < (len(pMatrix)):
            if pMatrix[contadorTemp][contador]!=0:
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
                listaEspaciosVerticales.append([filaInicio, contador, num])
            else:
                contadorTemp+=1
        contador+=1
    return listaEspaciosVerticales

def generarValores():
    global tablero
    global espacios
    tablero=espacios
    tamano = len(tablero)
    for i in range(tamano):
        for j in range(tamano):
            if tablero[i][j]!=0:
                n = randint(1, 9)
                maximasIteraciones=15
                while estaEnFila(i, j, n) or estaEnColumna(i, j, n):
                    n = randint(1, 9)
                    maximasIteraciones-=1
                    if maximasIteraciones==0:
                        return None
                tablero[i][j] = n
    return tablero

##kakuro(10)
##kakuro(11)
##kakuro(12)
##kakuro(13)
##kakuro(14)
##kakuro(15)
##kakuro(16)
##kakuro(17)
##kakuro(18)
##kakuro(19)
##kakuro(20)
