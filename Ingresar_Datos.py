from datetime import date, datetime
from Tablas import *

'''from Trabajo_Final.Tablas import Contar, Seleccionar_Orden'''

# DEFINE EL CÓDIGO DE UN NUEVO PRODUCTO
def Definir_Codigo():
    orden = Seleccionar_Orden("MAX", "Codigo", "PRODUCTOS")
    if not(orden[0][0] is None):
        orden = orden[0][0] + 1
    else:
        orden = 100
    return orden

# INGRESA UN NÚMERO ENTERO POR TECLADO EN RANGO MIN Y MAX
def Ingresar_Entero(mensaje, mensaje_error, min, max):
    valor = 0
    while valor == 0:
        try:
            numero = int(input(f"\n{mensaje}"))
            assert numero >= min and numero <= max
            valor = 1
        except:
            print(f"\n{mensaje_error}")
    
    return numero

# INGRESA UN NUMERO DECIMAL POR TECLADO ENTRE MIN Y MAX
def Ingresar_Precio(mensaje, mensaje_error, min, max):
    valor = 0
    while valor == 0:
        try:
            numero = float(input(f"\n{mensaje}"))
            assert numero >= min and numero <= max
            valor = 1
        except:
            print(f"\n{mensaje_error}")
    
    return numero

# INGRESA LA FECHA
def Ingresar_Fecha():
    dia = Ingresar_Entero("Ingrese el día de vencimiento: ", ">> Día no válido (1 a 30)", 1, 30)
    mes = Ingresar_Entero("Ingrese el mes de vencimiento: ", ">> Mes no válido (1 a 30)", 1, 12)
    anio = Ingresar_Entero("Ingrese el año de vencimiento: ", ">> Año no válido (1 a 30)", 2022, 2030)
    fecha = date(anio, mes, dia)
    return fecha

# INGRESA UNA CADENA SIN RESTRICCIÓN
def Ingresar_Cadena(mensaje):
    cadena = input(f"\n{mensaje}") 

    return cadena

# INGRESA EL TIPO DE UN PRODUCTO, SE ENVÍAN LOS TIPOS VÁLIDOS COMO PARÁMETROS
def Ingresar_Tipo(mensaje, mensaje_error, *args):
    valor = 0
    while valor == 0:
        try:
            cadena = input(f"\n{mensaje}")
            assert cadena.lower() in args
            valor = 1
        except:
            print(f"\n{mensaje_error}")
    
    return cadena


