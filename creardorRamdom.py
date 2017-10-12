import random

def sacarRamdom(totalDeEspacios):
    #En la pos [0] de la lista estan las posibilidades de tener 2 espacios (menor,mayor)
    #esto es para los limites del ramdom
    try:
        lista=[(3,17),(6,24),(10,30),(15,35),(21,39),(28,42),(36,44),(45,45)]
        digit=random.randint(lista[totalDeEspacios-2][0], lista[totalDeEspacios-2][1])
        #print(digit)
        return digit
    except:
        return 0
