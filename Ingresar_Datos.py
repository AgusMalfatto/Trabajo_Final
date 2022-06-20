from datetime import date, datetime

# DEFINE EL CÓDIGO DE UN NUEVO PRODUCTO
def Definir_Codigo(lista):
    if len(lista) == 0:
        codigo = 100
    else:
        codigo = lista[-1]["codigo"] + 1
    
    return codigo

# INGRESA UN NÚMERO ENTERO POR TECLADO EN RANGO MIN Y MAX
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

# INGRESA UN NUMERO DECIMAL POR TECLADO ENTRE MIN Y MAX
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

# INGRESA LA FECHA
def Ingresar_Fecha():
    dia = Ingresar_Entero("Ingrese el día de vencimiento", "Día no válido (1 a 30)", 1, 30)
    mes = Ingresar_Entero("Ingrese el mes de vencimiento", "mes no válido (1 a 30)", 1, 12)
    anio = Ingresar_Entero("Ingrese el año de vencimiento", "año no válido (1 a 30)", 2022, 2030)
    fecha = date((anio), mes, dia)
    return fecha

# INGRESA UNA CADENA SIN RESTRICCIÓN
def Ingresar_Cadena(mensaje):
    cadena = input(mensaje) 

    return cadena

# INGRESA EL TIPO DE UN PRODUCTO, SE ENVÍAN LOS TIPOS VÁLIDOS COMO PARÁMETROS
def Ingresar_Tipo(mensaje, mensaje_error, *args):
    valor = 0
    while valor == 0:
        try:
            cadena = input(mensaje)
            assert cadena.lower() in args
            valor = 1
        except:
            print(mensaje_error)
    
    return cadena

'''def Ingresar_Producto(lista):
    '''
