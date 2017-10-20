import threading
import logging
import time
from time import time
from random import shuffle
import random
#el original esta en immagen en la fuente de los archivos 
#kakuro de prueba kaku=[[0,0,0,0,0,0,0],
#                       [0,0,1,1,0,0,0],
#                       [0,0,1,1,1,1,0],
#                       [0,1,1,0,1,1,0],
#                       [0,1,1,1,1,0,0],
#                       [0,0,0,1,1,0,0],
#                       [0,0,0,0,0,0,0]]

filas=[(1, 2, 2,16,1), (2, 2, 4,23,1), (3, 1, 2,16,1), (3, 4, 2,14,1), (4, 1, 4,29,1), (5, 3, 2,17,1)]
columnas=[(3, 1, 2,16,2), (1, 2, 4,27,2), (1, 3, 2,17,2), (4, 3, 2,16,2), (2, 4, 4,26,2), (2, 5, 2,13,2)]

listaDeCampos=[(1, 2, 2,16,1),(3, 1, 2,16,2),(2, 2, 4,23,1),(1, 2, 4,27,2),(3, 1, 2,16,1),(1, 3, 2,17,2)

                ,(3, 4, 2,14,1),(4, 3, 2,16,2),(4, 1, 4,29,1),(2, 4, 4,26,2),(5, 3, 2,17,1),(2, 5, 2,13,2)]
def obtenerPosibilidades(goalValue, emptyCells):
    #Me va a retornar una lista con las posibles combinaciones de numeros. Se deberá después permutar
    #Hay 3-45 posibilidades en el goal value
    #Hay 2-9 posibilidades de celdas
    posibilities = {
         3: { 2: [[1,2]]},
         4: { 2: [[1,3]]},
         5: { 2: [[1,4],[2,3]]},
         6: { 2: [[1,5],[2,4]], 3: [[1,2,3]]},
         7: { 2: [[1,6],[2,5],[3,4]], 3: [[1,2,4]]},
         8: { 2: [[1,7],[2,6],[3,5]], 3: [[1,3,4],[1,2,5]]},
         9: { 2: [[1,8],[2,7],[3,6],[4,5]], 3: [[2,3,4],[1,3,5],[1,2,6]]},
        10: { 2: [[1,9],[2,8],[3,7],[4,6]], 3: [[2,3,5],[1,4,5],[1,3,6],[1,2,7]], 4: [[1,2,3,4]]},
        11: { 2: [[2,9],[3,8],[4,7],[5,6]], 3: [[2,4,5],[2,3,6],[1,4,6],[1,3,7],[1,2,8]], 4: [[1,2,3,5]]},
        12: { 2: [[3,9],[4,8],[5,7]], 3: [[3,4,5],[2,4,6],[2,3,7],[1,5,6],[1,4,7],[1,3,8],[1,2,9]], 4: [[1,2,3,6],[1,2,4,5]]},
        13: { 2: [[4,9],[5,8],[6,7]], 3: [[3,4,6],[2,5,6],[2,4,7],[2,3,8],[1,5,7],[1,4,8],[1,3,9]], 4: [[1,2,3,7],[1,2,4,6],[1,3,4,5]]},
        14: { 2: [[5,9],[6,8]], 3: [[3,5,6],[3,4,7],[2,5,7],[2,4,8],[2,3,9],[1,6,7],[1,5,8],[1,4,9]], 4: [[1,2,3,8],[1,2,4,7],[1,2,5,6],[1,3,4,6],[2,3,4,5]]},
        15: { 2: [[6,9],[7,8]], 3: [[4,5,6],[3,5,7],[3,4,8],[2,6,7],[2,5,8],[2,4,9],[1,6,8],[1,5,9]], 4: [[1,2,3,9],[1,2,4,8],[1,2,5,7],[1,3,4,7],[1,3,5,6],[2,3,4,6]], 5: [[1,2,3,4,5]]},
        16: { 2: [[7,9]], 3: [[4,5,7],[3,6,7],[3,5,8],[3,4,9],[2,6,8],[2,5,9],[1,7,8],[1,6,9]], 4: [[1,2,4,9],[1,2,5,8],[1,2,6,7],[1,3,4,8],[1,3,5,7],[1,4,5,6],[2,3,4,7],[2,3,5,6]], 5: [[1,2,3,4,6]]},
        17: { 2: [[8, 9]], 3: [[1, 7, 9], [2, 6, 9], [3, 5, 9], [2, 7, 8], [3, 6, 8], [4, 5, 8], [4, 6, 7]], 4: [[1, 2, 5, 9], [1, 3, 4, 9], [1, 2, 6, 8], [1, 3, 5, 8], [2, 3, 4, 8], [1, 3, 6, 7], [1, 4, 5, 7], [2, 3, 5, 7], [2, 4, 5, 6]], 5: [[1, 2, 3, 4, 7], [1, 2, 3, 5, 6]]},
        18: { 3: [[1, 8, 9], [2, 7, 9], [3, 6, 9], [4, 5, 9], [3, 7, 8], [4, 6, 8], [5, 6, 7]], 4: [[1, 2, 6, 9], [1, 3, 5, 9], [2, 3, 4, 9], [1, 2, 7, 8], [1, 3, 6, 8], [1, 4, 5, 8], [2, 3, 5, 8], [1, 4, 6, 7], [2, 3, 6, 7], [2, 4, 5, 7], [3, 4, 5, 6]], 5: [[1, 2, 3, 4, 8], [1, 2, 3, 5, 7], [1, 2, 4, 5, 6]]},
        19: { 3: [[2, 8, 9], [3, 7, 9], [4, 6, 9], [4, 7, 8], [5, 6, 8]], 4: [[1, 2, 7, 9], [1, 3, 6, 9], [1, 4, 5, 9], [2, 3, 5, 9], [1, 3, 7, 8], [1, 4, 6, 8], [2, 3, 6, 8], [2, 4, 5, 8], [1, 5, 6, 7], [2, 4, 6, 7], [3, 4, 5, 7]], 5: [[1, 2, 3, 4, 9], [1, 2, 3, 5, 8], [1, 2, 3, 6, 7], [1, 2, 4, 5, 7], [1, 3, 4, 5, 6]]},
        20: { 3: [[3, 8, 9], [4, 7, 9], [5, 6, 9], [5, 7, 8]], 4: [[1, 2, 8, 9], [1, 3, 7, 9], [1, 4, 6, 9], [2, 3, 6, 9], [2, 4, 5, 9], [1, 4, 7, 8], [2, 3, 7, 8], [1, 5, 6, 8], [2, 4, 6, 8], [3, 4, 5, 8], [2, 5, 6, 7], [3, 4, 6, 7]], 5: [[1, 2, 3, 5, 9], [1, 2, 3, 6, 8], [1, 2, 4, 5, 8], [1, 2, 4, 6, 7], [1, 3, 4, 5, 7], [2, 3, 4, 5, 6]]},
        21: { 3: [[4, 8, 9], [5, 7, 9], [6, 7, 8]], 4: [[1, 3, 8, 9], [1, 4, 7, 9], [2, 3, 7, 9], [1, 5, 6, 9], [2, 4, 6, 9], [3, 4, 5, 9], [1, 5, 7, 8], [2, 4, 7, 8], [2, 5, 6, 8], [3, 4, 6, 8], [3, 5, 6, 7]], 5: [[1, 2, 3, 6, 9], [1, 2, 4, 5, 9], [1, 2, 3, 7, 8], [1, 2, 4, 6, 8], [1, 3, 4, 5, 8], [1, 2, 5, 6, 7], [1, 3, 4, 6, 7], [2, 3, 4, 5, 7]], 6: [[1, 2, 3, 4, 5, 6]]},
        22: { 3: [[5, 8, 9], [6, 7, 9]], 4: [[1, 4, 8, 9], [2, 3, 8, 9], [1, 5, 7, 9], [2, 4, 7, 9], [2, 5, 6, 9], [3, 4, 6, 9], [1, 6, 7, 8], [2, 5, 7, 8], [3, 4, 7, 8], [3, 5, 6, 8], [4, 5, 6, 7]], 5: [[1, 2, 3, 7, 9], [1, 2, 4, 6, 9], [1, 3, 4, 5, 9], [1, 2, 4, 7, 8], [1, 2, 5, 6, 8], [1, 3, 4, 6, 8], [2, 3, 4, 5, 8], [1, 3, 5, 6, 7], [2, 3, 4, 6, 7]], 6: [[1, 2, 3, 4, 5, 7]]},
        23: { 3: [[6, 8, 9]], 4: [[1, 5, 8, 9], [2, 4, 8, 9], [1, 6, 7, 9], [2, 5, 7, 9], [3, 4, 7, 9], [3, 5, 6, 9], [2, 6, 7, 8], [3, 5, 7, 8], [4, 5, 6, 8]], 5: [[1, 2, 3, 8, 9], [1, 2, 4, 7, 9], [1, 2, 5, 6, 9], [1, 3, 4, 6, 9], [2, 3, 4, 5, 9], [1, 2, 5, 7, 8], [1, 3, 4, 7, 8], [1, 3, 5, 6, 8], [2, 3, 4, 6, 8], [1, 4, 5, 6, 7], [2, 3, 5, 6, 7]], 6: [[1, 2, 3, 4, 5, 8], [1, 2, 3, 4, 6, 7]]},
        24: { 3: [[7, 8, 9]], 4: [[1, 6, 8, 9], [2, 5, 8, 9], [3, 4, 8, 9], [2, 6, 7, 9], [3, 5, 7, 9], [4, 5, 6, 9], [3, 6, 7, 8], [4, 5, 7, 8]], 5: [[1, 2, 4, 8, 9], [1, 2, 5, 7, 9], [1, 3, 4, 7, 9], [1, 3, 5, 6, 9], [2, 3, 4, 6, 9], [1, 2, 6, 7, 8], [1, 3, 5, 7, 8], [2, 3, 4, 7, 8], [1, 4, 5, 6, 8], [2, 3, 5, 6, 8], [2, 4, 5, 6, 7]], 6: [[1, 2, 3, 4, 5, 9], [1, 2, 3, 4, 6, 8], [1, 2, 3, 5, 6, 7]]},
        25: { 4: [[1, 3, 8, 9], [1, 4, 7, 9], [2, 3, 7, 9], [1, 5, 6, 9], [2, 4, 6, 9], [3, 4, 5, 9], [1, 5, 7, 8], [2, 4, 7, 8], [2, 5, 6, 8], [3, 4, 6, 8], [3, 5, 6, 7]], 5: [[1, 2, 3, 6, 9], [1, 2, 4, 5, 9], [1, 2, 3, 7, 8], [1, 2, 4, 6, 8], [1, 3, 4, 5, 8], [1, 2, 5, 6, 7], [1, 3, 4, 6, 7], [2, 3, 4, 5, 7]], 6: [[1, 2, 3, 4, 5, 6]]},
        26: { 4: [[2, 7, 8, 9], [3, 6, 8, 9], [4, 5, 8, 9], [4, 6, 7, 9], [5, 6, 7, 8]], 5: [[1, 2, 6, 8, 9], [1, 3, 5, 8, 9], [2, 3, 4, 8, 9], [1, 3, 6, 7, 9], [1, 4, 5, 7, 9], [2, 3, 5, 7, 9], [2, 4, 5, 6, 9], [1, 4, 6, 7, 8], [2, 3, 6, 7, 8], [2, 4, 5, 7, 8], [3, 4, 5, 6, 8]], 6: [[1, 2, 3, 4, 7, 9], [1, 2, 3, 5, 6, 9], [1, 2, 3, 5, 7, 8], [1, 2, 4, 5, 6, 8], [1, 3, 4, 5, 6, 7]], 7: [[]], 8: [[]], 9: [[]]},
        27: { 4: [[3, 7, 8, 9], [4, 6, 8, 9], [5, 6, 7, 9]], 5: [[1, 2, 7, 8, 9], [1, 3, 6, 8, 9], [1, 4, 5, 8, 9], [2, 3, 5, 8, 9], [1, 4, 6, 7, 9], [2, 3, 6, 7, 9], [2, 4, 5, 7, 9], [3, 4, 5, 6, 9], [1, 5, 6, 7, 8], [2, 4, 6, 7, 8], [3, 4, 5, 7, 8]], 6: [[1, 2, 3, 4, 8, 9], [1, 2, 3, 5, 7, 9], [1, 2, 4, 5, 6, 9], [1, 2, 3, 6, 7, 8], [1, 2, 4, 5, 7, 8], [1, 3, 4, 5, 6, 8], [2, 3, 4, 5, 6, 7]]},
        28: { 4: [[4, 7, 8, 9], [5, 6, 8, 9]], 5: [[1, 3, 7, 8, 9], [1, 4, 6, 8, 9], [2, 3, 6, 8, 9], [2, 4, 5, 8, 9], [1, 5, 6, 7, 9], [2, 4, 6, 7, 9], [3, 4, 5, 7, 9], [2, 5, 6, 7, 8], [3, 4, 6, 7, 8]], 6: [[1, 2, 3, 5, 8, 9], [1, 2, 3, 6, 7, 9], [1, 2, 4, 5, 7, 9], [1, 3, 4, 5, 6, 9], [1, 2, 4, 6, 7, 8], [1, 3, 4, 5, 7, 8], [2, 3, 4, 5, 6, 8]], 7: [[1, 2, 3, 4, 5, 6, 7]]},
        29: { 4: [[5, 7, 8, 9]], 5: [[1, 4, 7, 8, 9], [2, 3, 7, 8, 9], [1, 5, 6, 8, 9], [2, 4, 6, 8, 9], [3, 4, 5, 8, 9], [2, 5, 6, 7, 9], [3, 4, 6, 7, 9], [3, 5, 6, 7, 8]], 6: [[1, 2, 3, 6, 8, 9], [1, 2, 4, 5, 8, 9], [1, 2, 4, 6, 7, 9], [1, 3, 4, 5, 7, 9], [2, 3, 4, 5, 6, 9], [1, 2, 5, 6, 7, 8], [1, 3, 4, 6, 7, 8], [2, 3, 4, 5, 7, 8]], 7: [[1, 2, 3, 4, 5, 6, 8]]},
        30: { 4: [[6, 7, 8, 9]], 5: [[1, 5, 7, 8, 9], [2, 4, 7, 8, 9], [2, 5, 6, 8, 9], [3, 4, 6, 8, 9], [3, 5, 6, 7, 9], [4, 5, 6, 7, 8]], 6: [[1, 2, 3, 7, 8, 9], [1, 2, 4, 6, 8, 9], [1, 3, 4, 5, 8, 9], [1, 2, 5, 6, 7, 9], [1, 3, 4, 6, 7, 9], [2, 3, 4, 5, 7, 9], [1, 3, 5, 6, 7, 8], [2, 3, 4, 6, 7, 8]], 7: [[1, 2, 3, 4, 5, 6, 9], [1, 2, 3, 4, 5, 7, 8]]},
        31: { 5: [[1, 6, 7, 8, 9], [2, 5, 7, 8, 9], [3, 4, 7, 8, 9], [3, 5, 6, 8, 9], [4, 5, 6, 7, 9]], 6: [[1, 2, 4, 7, 8, 9], [1, 2, 5, 6, 8, 9], [1, 3, 4, 6, 8, 9], [2, 3, 4, 5, 8, 9], [1, 3, 5, 6, 7, 9], [2, 3, 4, 6, 7, 9], [1, 4, 5, 6, 7, 8], [2, 3, 5, 6, 7, 8]], 7: [[1, 2, 3, 4, 5, 7, 9], [1, 2, 3, 4, 6, 7, 8]]},
        32: { 5: [[2, 6, 7, 8, 9], [3, 5, 7, 8, 9], [4, 5, 6, 8, 9]], 6: [[1, 2, 5, 7, 8, 9], [1, 3, 4, 7, 8, 9], [1, 3, 5, 6, 8, 9], [2, 3, 4, 6, 8, 9], [1, 4, 5, 6, 7, 9], [2, 3, 5, 6, 7, 9], [2, 4, 5, 6, 7, 8]], 7: [[1, 2, 3, 4, 5, 8, 9], [1, 2, 3, 4, 6, 7, 9], [1, 2, 3, 5, 6, 7, 8]]},
        33: { 5: [[3, 6, 7, 8, 9], [4, 5, 7, 8, 9]], 6: [[1, 2, 6, 7, 8, 9], [1, 3, 5, 7, 8, 9], [2, 3, 4, 7, 8, 9], [1, 4, 5, 6, 8, 9], [2, 3, 5, 6, 8, 9], [2, 4, 5, 6, 7, 9], [3, 4, 5, 6, 7, 8]], 7: [[1, 2, 3, 4, 6, 8, 9], [1, 2, 3, 5, 6, 7, 9], [1, 2, 4, 5, 6, 7, 8]]},
        34: { 5: [[4, 6, 7, 8, 9]], 6: [[1, 3, 6, 7, 8, 9], [1, 4, 5, 7, 8, 9], [2, 3, 5, 7, 8, 9], [2, 4, 5, 6, 8, 9], [3, 4, 5, 6, 7, 9]], 7: [[1, 2, 3, 4, 7, 8, 9], [1, 2, 3, 5, 6, 8, 9], [1, 2, 4, 5, 6, 7, 9], [1, 3, 4, 5, 6, 7, 8]]},
        35: { 5: [[5, 6, 7, 8, 9]], 6: [[1, 4, 6, 7, 8, 9], [2, 3, 6, 7, 8, 9], [2, 4, 5, 7, 8, 9], [3, 4, 5, 6, 8, 9]], 7: [[1, 2, 3, 5, 7, 8, 9], [1, 2, 4, 5, 6, 8, 9], [1, 3, 4, 5, 6, 7, 9], [2, 3, 4, 5, 6, 7, 8]]},
        36: { 6: [[1, 5, 6, 7, 8, 9], [2, 4, 6, 7, 8, 9], [3, 4, 5, 7, 8, 9]], 7: [[1, 2, 3, 6, 7, 8, 9], [1, 2, 4, 5, 7, 8, 9], [1, 3, 4, 5, 6, 8, 9], [2, 3, 4, 5, 6, 7, 9]], 8: [[1,2,3,4,5,6,7,8]]},
        37: { 6: [[2, 5, 6, 7, 8, 9], [3, 4, 6, 7, 8, 9]], 7: [[1, 2, 4, 6, 7, 8, 9], [1, 3, 4, 5, 7, 8, 9], [2, 3, 4, 5, 6, 8, 9]], 8: [[1,2,3,4,5,6,7,9]]},
        38: { 6: [[3, 5, 6, 7, 8, 9]], 7: [[1, 2, 5, 6, 7, 8, 9], [1, 3, 4, 6, 7, 8, 9], [2, 3, 4, 5, 7, 8, 9]], 8: [[1,2,3,4,5,6,8,9]]},
        39: { 6: [[4, 5, 6, 7, 8, 9]], 7: [[1, 3, 5, 6, 7, 8, 9], [2, 3, 4, 6, 7, 8, 9]], 8: [[1,2,3,4,5,7,8,9]]},
        40: { 7: [[1, 4, 5, 6, 7, 8, 9], [2, 3, 5, 6, 7, 8, 9]], 8: [[1,2,3,4,6,7,8,9]]},
        41: { 7: [[2, 4, 5, 6, 7, 8, 9]], 8: [[1,2,3,5,6,7,8,9]]},
        42: { 7: [[3, 4, 5, 6, 7, 8, 9]], 8: [[1,2,4,5,6,7,8,9]]},
        43: { 8: [[1,3,4,5,6,7,8,9]]},
        44: { 8: [[2,3,4,5,6,7,8,9]]},
        45: { 9: [[1,2,3,4,5,6,7,8,9]]},
    }
    return posibilities.get(goalValue, None).get(emptyCells, None)#Obtengo una lista de listas


result =[["|","|","|","|","|","|","|"],
        ["|","|","|","|","|","|","|"],
        ["|","|","|","|","|","|","|"],
        ["|","|","|","|","|","|","|"],
        ["|","|","|","|","|","|","|"],
        ["|","|","|","|","|","|","|"],
        ["|","|","|","|","|","|","|"]]

'''result =[["|","|","|","|","|","|","|"],
        ["|","|","|",7,"|","|","|"],
        [4,3,2,8,9,1,"|"],
        ["|","|","|",3,"|","|","|"],
        ["|","|","|","|","|","|","|"],
        ["|","|","|","|","|","|","|"],
        ["|","|","|","|","|","|","|"]]'''

logging.basicConfig( level=logging.DEBUG,format='[%(levelname)s] - %(threadName)-10s : %(message)s')
ingresarResult_lock = threading.Lock()
quitarGastados=threading.Lock()
gastados=[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]

def daemon(tupla,tipo):
    #si es tipo 1 es hor, tipo es ver
    #print (getPossibleNumbers(tupla[3],tupla[2]))
    posibilidades=obtenerPosibilidades(tupla[3],tupla[2])
    if (tipo==1):
        with ingresarResult_lock:
            const=0
            for x in range(tupla[2]):
                if((posibilidades[0][x] in gastados[tupla[1]+x]) and (result[tupla[0]][tupla[1]+const] == "|" or  result[tupla[0]][tupla[1]+const] == "O")):
                    result[tupla[0]][tupla[1]+const]=posibilidades[0][x]
                    const+=1
                    with quitarGastados:
                        gastados[tupla[1]+x].remove(posibilidades[0][x])
                        print("la columa ",(tupla[1]+ x)," le quedan por gastar: ",gastados[tupla[1]+x])
                else:
                    if (result[tupla[0]][tupla[1]+const] == "|"):
                        result[tupla[0]][tupla[1]+const]="O"
                    const+=1
    
    else:
        with ingresarResult_lock:
            const=0
            for x in range(tupla[2]):
                if((posibilidades[0][x] in gastados[tupla[1]]) and (result[tupla[0]+const][tupla[1]] == "|" or result[tupla[0]+const][tupla[1]] == "O")):
                    result[tupla[0]+const][tupla[1]]=posibilidades[0][x]
                    const+=1
                    with quitarGastados:
                        gastados[tupla[1]].remove(posibilidades[0][x])
                        print("la columa ",(tupla[1])," le quedan por gastar: ",gastados[tupla[1]])
                else:
                    if(result[tupla[0]+const][tupla[1]] == "|"):
                        result[tupla[0]+const][tupla[1]]="O"
                    const+=1
                    
    print("-------------------------------------------")
    for x in result:
        print (x)
            
                                     


#def daemon():
def verificar(fila,columna,largo,pmatriz):
    #verifica que no se repitan numero en fila y columna
    gastadoH=[1,2,3,4,5,6,7,8,9]
    gastadoV=[1,2,3,4,5,6,7,8,9]
    for x in range(len(pmatriz)):
        if(((pmatriz[fila][x] in gastadoH) or pmatriz[fila][x]=="|")):
            if (pmatriz[fila][x]!="|"):
                gastadoH.remove(pmatriz[fila][x])
            else:
                continue
        else:
            return False
        if(((pmatriz[x][columna] in gastadoV) or pmatriz[x][columna]=="|")):
            if(pmatriz[x][columna]!="|"):
                gastadoV.remove(pmatriz[x][columna])
            else:
                continue
        else:
            return False
    return True

def sacarToquesHorizontales(fila,columna,largo,matriz):
    toques=[]
    for x in range(largo):
        if((matriz[fila][columna+x]!="|") and x<9):
            toques.append(((columna+x),matriz[fila][columna+x]))
        else:
            continue
    return toques

def sacarToquesVerticales(fila,columna,largo,matriz):
    toques=[]
    for x in range(largo):
        if((matriz[fila+x][columna]!="|") and x<9):
            toques.append(((fila+x),matriz[fila+x][columna]))
        else:
            continue
    return toques

def escojerMejorPosibilidad(pPosibilidades,listaToques):
    seraPos=True
    for posibilidad in pPosibilidades:
        seraPos=True
        for toques in range(len(listaToques)):
            if(listaToques[toques][1] in posibilidad):
                continue
            else:
                seraPos=False
        if(seraPos):
            return posibilidad
            
    return

def eliminarPresentes(posibilidades,aEliminar):
    for x in range(len(aEliminar)):
        if(aEliminar[x][1] in posibilidades):
            posibilidades.remove(aEliminar[x][1])
    return posibilidades 
def limpiarLoQueHizo(tupla,pMatrix,posibilidades):
    if (tupla[4]==1):
        for x in range(tupla[2]):
            if(pMatrix[tupla[0]][tupla[1]+x] in posibilidades):
                pMatrix[tupla[0]][tupla[1]+x]="|"
            else:
                continue
        return pMatrix
    else:
        for x in range(tupla[2]):
            if(pMatrix[tupla[0]+x][tupla[1]] in posibilidades):
                pMatrix[tupla[0]+x][tupla[1]]="|"
            else:
                continue
        return pMatrix
        
            
def meterEnMatriz(pmatrix,tupla,posibilidades):
    if(tupla[4]==1):#para las horizontales
        listaToques=sacarToquesHorizontales(tupla[0],tupla[1],tupla[2],pmatrix)#para ver si pega en algun lado con una vertical
        posibilidadMasFactible=escojerMejorPosibilidad(posibilidades,listaToques)
        posibilidadMasFactible=eliminarPresentes(posibilidadMasFactible,listaToques)
        contador=0
        random.shuffle(posibilidadMasFactible)
        metidos=0
        intentos=0
        while ((metidos!=len(posibilidadMasFactible))and intentos<15):
            if(pmatrix[tupla[0]][tupla[1]+contador]=="|"):
                pmatrix[tupla[0]][tupla[1]+contador]=posibilidadMasFactible[0]
                if (verificar(tupla[0],tupla[1]+contador,tupla[2],pmatrix)):
                    print("dio true")
                    metidos+=1
                    contador+=1
                else:
                    print("va a hacer cambio porque no es valido el num",posibilidadMasFactible[0]," en la posicion ",tupla[0]," ",tupla[1]+contador )
                    pmatrix[tupla[0]][tupla[1]+contador]="|"
                    random.shuffle(posibilidadMasFactible)
                    intentos+=1
                    
            else:
                contador+=1
        if(intentos>=15):
            pmatrix=limpiarLoQueHizo(tupla,pmatrix,posibilidadMasFactible)
            return (False,pmatrix)
        else:
            return (True,pmatrix)
    else:
        listaToques=sacarToquesVerticales(tupla[0],tupla[1],tupla[2],pmatrix)
        posibilidadMasFactible=escojerMejorPosibilidad(posibilidades,listaToques)
        posibilidadMasFactible=eliminarPresentes(posibilidadMasFactible,listaToques)
        contador=0
        random.shuffle(posibilidadMasFactible)
        metidos=0
        intentos=0
        while ((metidos!=len(posibilidadMasFactible))and intentos<15):
            if(pmatrix[tupla[0]+contador][tupla[1]]=="|"):
                pmatrix[tupla[0]+contador][tupla[1]]=posibilidadMasFactible[0]
                #print(pmatrix[tupla[0]][tupla[1]+contador])
                if (verificar(tupla[0]+contador,tupla[1],tupla[2],pmatrix)):
                    print("dio true")
                    metidos+=1
                    contador+=1
                else:
                    print("va a hacer cambio porque no es valido el num",posibilidadMasFactible[0]," en la posicion ",tupla[0]," ",tupla[1]+contador )
                    pmatrix[tupla[0]+contador][tupla[1]]="|"
                    random.shuffle(posibilidadMasFactible)
                    intentos+=1
                    
            else:
                contador+=1
        if(intentos>=15):
            pmatrix=limpiarLoQueHizo(tupla,pmatrix,posibilidadMasFactible)
            return (False,pmatrix)
        else:
            return (True,pmatrix)



        
def backtrack(matrizSolu,tuplaActual,listaDeTuplas,intentos):
    if (listaDeTuplas==[]):
        return matrizSolu
    else:
        resultado=meterEnMatriz(matrizSolu,tuplaActual,obtenerPosibilidades(tuplaActual[3],tuplaActual[2]))
        if (resultado[0] and (intentos < 11)):
            backtrack(resultado[1],listaDeTuplas.pop(),listaDeTuplas,0)
        else:
            intentos+=1
            backtrack(resultado[1],tuplaActual,listaDeTuplas,intentos)

        
#prueba=meterEnMatriz(result,(1,1,3,18,2),[[1, 8, 9], [2, 7, 9], [3, 6, 9], [4, 5, 9], [3, 7, 8], [4, 6, 8], [5, 6, 7]])
prueba=backtrack(result,listaDeCampos[0],listaDeCampos,0)
for x in prueba:
    print(x)




    
def solving(listaHor,listaVer):
    for x in range(len(listaHor)+len(listaVer)):
        #print (x)
        if (x<len(listaHor)):
            d = threading.Thread(target=daemon, name='Daemon', args=(listaHor[x],1,))
            d.setDaemon(True)
            d.run()
        if (x<len(listaVer)):
            d = threading.Thread(target=daemon, name='Daemon', args=(listaVer[x],2,))
            d.setDaemon(True)
            d.run()

        

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def permute(a, i, n):
    if i == n:
        print (a)
        return a
    for j in range(i, n+1):
        swap(a, i, j)
        permute(a, i+1, n)
        swap(a, i, j)  # backtrack

def main():
    start_time = time()
    a = [1,2,3,4,5,6]
    permute(a, 2, 5)
    elapsed_time = time() - start_time
    print("Duro en mili",elapsed_time)

#main()
#backtrack()
#solving(filas,columnas)
#print(sacarToquesVerticales(1,3,5,result))
#print(permute([1,2,3,4,5,6], 2, 5))
