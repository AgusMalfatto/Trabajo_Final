from datetime import date

def Definir_Codigo(lista):
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

def Ingresar_Fecha():
    dia = Ingresar_Entero("Ingrese el día de vencimiento", "Día no válido (1 a 30)", 1, 30)
    mes = Ingresar_Entero("Ingrese el mes de vencimiento", "mes no válido (1 a 30)", 1, 12)
    anio = Ingresar_Entero("Ingrese el año de vencimiento", "año no válido (1 a 30)", 2022, 2030)
    fecha = date((anio), mes, dia)
    return fecha

def Ingresar_Cadena(mensaje):
    cadena = input(mensaje) 

    return cadena

def Ingresar_Tipo(mensaje, mensaje_error, *args):
    valor = 0
    while valor == 0:
        try:
            cadena = input(mensaje)
            assert cadena in args
            valor = 1
        except:
            print(mensaje_error)
    
    return cadena

'''def Ingresar_Producto(lista):
    '''
