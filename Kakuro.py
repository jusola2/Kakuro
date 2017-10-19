#'''
#Created on Oct 4, 2017
#
#@author: Eduard, Juan
#'''

from random import randint, choices
from time import time
import pygame
import easygui

#variables
tamanios = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
seleccion = 0
tablero = []
vector = []
consecutivosFilas = []
consecutivosColumnas = []
espacios = []
sumas = []

#inicializar componentes
pygame.init()
pygame.font.init()
comic = pygame.font.SysFont('comicsansms', 12)
numbers = pygame.font.SysFont('comicsansms', 10)

#Colores
BLACK=(0,0,0)
WHITE=(255,255,255)

def mainWindow():
    global seleccion
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Kakuro')
    clock = pygame.time.Clock()
    #Imagen de fondo
    bg = pygame.image.load('background.jpg')
    screen.blit(bg, (0,0))
    title = pygame.image.load('title.png')
    screen.blit(title, (280,20))
    #Texto bajo el titulo
##    texto = comic.render('Elija el tamaño del tablero', True, BLACK)
##    screen.blit(texto, (215,88))
    n=int(easygui.choicebox(title='Kakuro',
                            msg='Elija el tamaño del kakuro',
                            choices=tamanios))
    kakuro(n)
    dibujarTablero(screen, n)
    #Para cerrar la ventana
    cerrar = False
    while not cerrar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cerrar = True
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    #quit()

def dibujarTablero(screen, n):
    global tablero
    global sumas
    MARGIN = 2
    WIDTH = 35
    HEIGHT = 25
    pygame.draw.rect(screen,
                      BLACK,
                      [(400-((MARGIN + WIDTH)*n)//2)-MARGIN,
                      100,
                      ((MARGIN + WIDTH)*n)+MARGIN,
                      ((MARGIN + HEIGHT)*n)+MARGIN])
    for row in range(n):
        for column in range(n):
            color = BLACK
            if tablero[row][column]!=0:
                color = WHITE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + 400-((MARGIN + WIDTH)*n)//2,
                              (MARGIN + HEIGHT) * row + MARGIN + 100,
                              WIDTH,
                              HEIGHT])

    for i in range(len(sumas)):
        if sumas[i][4]==1:
            x=(MARGIN + WIDTH) * (sumas[i][1]-1) + 400-((MARGIN + WIDTH)*n)//2
            y=(MARGIN + HEIGHT) * sumas[i][0] + MARGIN + 100
            pygame.draw.line(screen, WHITE, (x, y), (x+WIDTH, y+HEIGHT), MARGIN)
            texto = numbers.render(str(sumas[i][3]), True, WHITE)
            x+=WIDTH-10
            screen.blit(texto, (x,y))
        else:
            x=(MARGIN + WIDTH) * sumas[i][1] + 400-((MARGIN + WIDTH)*n)//2
            y=(MARGIN + HEIGHT) * (sumas[i][0]-1) + MARGIN + 100
            pygame.draw.line(screen, WHITE, (x, y), (x+WIDTH, y+HEIGHT), MARGIN)
            texto = numbers.render(str(sumas[i][3]), True, WHITE)
            y+=HEIGHT-10
            screen.blit(texto, (x,y))
            
    escribirSolucion(screen, tablero, MARGIN, WIDTH, HEIGHT, n)

def escribirSolucion(screen, matriz, MARGIN, WIDTH, HEIGHT, n):
    for i in range(1,len(matriz)):
        for j in range(1,len(matriz)):
            if matriz[i][j]!=0:
                x=(MARGIN + WIDTH) * j + 400-((MARGIN + WIDTH)*n)//2
                x+=10
                y=(MARGIN + HEIGHT) * i + MARGIN + 100
                y+=2
                texto = comic.render(str(matriz[i][j]), True, BLACK)
                screen.blit(texto, (x,y))
    

def kakuro(n):
    global tablero
    global espacios
    global sumas
    crearMatriz(n)
    valido = False
    while not valido:
        valido = validarEspacios(n)
    valores = None
    reintentar=10
    while valores == None:
        valores = generarValores()
        reintentar-=1
        if reintentar==0:
            kakuro(n)
            return
    sumas = calcularSumas(tablero)
##    tablero = reiniciarCeldas(tablero)
    printMatriz(tablero)

def crearMatriz(n):
    global tablero
    global espacios
    tablero = []
    vector = []
    espacios = []
    for i in range(0, n):
        vector = []
        for j in range(0, n):
            if i == 0 or j == 0:
                vector.append(0)
            else:
                vector.append(choices([0, 1],[0.05, 0.2])[0])
        tablero.append(vector)

def printMatriz(matriz):
    for n in range(0, len(matriz)):
        print(matriz[n])

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

# Calcula las sumas de las celdas del tablero
def calcularSumas(matriz):
    global consecutivosFilas
    global consecutivosColumnas
    values=[]
    #Revisa los espacios horizontales
    for i in range(len(consecutivosFilas)):
        vector = consecutivosFilas[i]
        if vector[2]>1:
            n = getSumaHorizontal(vector, matriz)
            vector.append(n)
            vector.append(1)
            values.append(vector)
    #Revisa los espacios verticales
    for i in range(len(consecutivosColumnas)):
        vector = consecutivosColumnas[i]
        if vector[2]>1:
            n = getSumaVertical(vector, matriz)
            vector.append(n)
            vector.append(2)
            values.append(vector)
    values.sort()
    return values

# Obtiene la suma del vector desde un punto dado horizontalmente
def getSumaHorizontal(coord, matriz):
    vector=[]
    for j in range(coord[1], coord[1]+coord[2]):
        vector.append(matriz[coord[0]][j])
    return sum(vector)

# Obtiene la suma del vector desde un punto dado verticalmente
def getSumaVertical(coord, matriz):
    vector=[]
    for i in range(coord[0], coord[0]+coord[2]):
        vector.append(matriz[i][coord[1]])
    return sum(vector)                        

def reiniciarCeldas(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j]!=0:
                matriz[i][j]=1
    return matriz

mainWindow()
