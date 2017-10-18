#lector de matriz y espacios
from time import time
#Este es para las filas 
def espaciosFilas(pMatrix):
    start_time = time()
    #lista de tuplas (numeroFila,columna donde empieza el espacio ,cantidad de espacios)
    listaEspaciosHorizontales=[]
    contador=0
    for contador in range( len(pMatrix)):
        contadorTemp=0
        print ("contador=",contador)
        while contadorTemp < (len(pMatrix[contador])):
            print ("contadorTemp=",contadorTemp)
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
    #lista de tuplas (fila donde empieza el espacio, numeroColumna ,cantidad de espacios)
    listaEspaciosVerticales=[]
    contador=0
    for contador in range( len(pMatrix)):
        contadorTemp=0
        num=0
        while (contadorTemp<len(pMatrix)):
            if( pMatrix[contadorTemp][contador]==1):
                empezoEn=contadorTemp
                num+=1
                contadorTemp+=1
                while(contadorTemp<len(pMatrix) and pMatrix[contadorTemp][contador]==1):
                    num+=1
                    contadorTemp+=1
            else:
                contadorTemp+=1
            if(num>1): 
                print("va por la fila ",contadorTemp," ,de la columna ",contador)
                print("metio en respuesta")
                listaEspaciosVerticales.append((empezoEn,contador,num))
                num=0
    elapsed_time = time() - start_time
    print("Duro en mili la funcion 2",elapsed_time)
    return listaEspaciosVerticales

def menu():
    matrix=[[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[0,1,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,1,0],[1,1,1,0,0,0,0,0,1,1],[1,1,1,0,0,0,0,0,1,0],[1,1,1,0,0,0,0,0,1,0]]
    for a in matrix:
        print (a)
    #try:
    opcion = int (input ("Escoja una opcion: "))
    if opcion >=1 and opcion <=11:  #ojo
        if opcion == 1:
              filas=espaciosFilas(matrix)
              print("resultado= ",filas)
        elif opcion ==2:
            columnas=espaciosVerticales(matrix)
            print("resultado= ",columnas)
                
        else:
            return 
    else:
        print ("Opcion invalida")
        menu()
    #except:
    menu()
    


#inicio del programa
menu()
