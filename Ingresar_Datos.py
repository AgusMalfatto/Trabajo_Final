import sqlite3

database = sqlite3.connect('C:\Users\agusm\OneDrive\Escritorio\Trabajo_Final_Super\Trabajo_Final')

def Definir_Código(lista):
    if len(lista) == 0:
        codigo = 100
    else:
        codigo = lista[-1]["codigo"] + 1
    
    return codigo

def Ingresar_Entero(mensaje, mensaje_error, min, max):
    valor = 0
    while valor == 0:
        try:
            numero = int(input(mensaje))
            assert numero >= min and numero <= max
            valor = 1
        except:
            print(mensaje_error)
    
    return numero

def Ingresar_Precio(mensaje, mensaje_error, min, max):
    valor = 0
    while valor == 0:
        try:
            numero = float(input(mensaje))
            assert numero >= min and numero <= max
            valor = 1
        except:
            print(mensaje_error)
    
    return numero

def Ingresar_Cadena(mensaje):
    cadena = input(mensaje) 

    return cadena

def Ingresar_Tipo(mensaje, mensaje_error, valido):
    valor = 0
    while valor == 0:
        try:
            cadena = input(mensaje)
            assert cadena in valido
            valor = 1
        except:
            print(mensaje_error)
    
    return cadena

'''def Ingresar_Producto(lista):
    '''
