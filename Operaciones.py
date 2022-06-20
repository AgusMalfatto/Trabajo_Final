from Ingresar_Datos import *
from Tablas import *


# PERMITE INGRESAR LOS DATOS DE UN NUEVO PRODUCTO
def Ingresar_Nuevo_Producto():
    '''codigo = Definir_Codigo(lista)'''
    descripcion = Ingresar_Cadena("\nIngrese la descripción del producto: ")
    cantidad = Ingresar_Entero("\nIngrese cantidad de productos: ", "Cantidad no válida", 1, 50)
    precio = Ingresar_Precio("Ingrese el precio del producto: ", "Precio no válido", 1, 30)
    fecha = Ingresar_Fecha()
    '''tipo = Ingresar_Tipo("Ingrese el tipo del producto: ", "Tipo no válido", "Lacteos", )'''
    Ingresar_Valor("PRODUCTOS", 101, descripcion, cantidad, precio, fecha, 'L')

# CONSULTA EL STOCK DE UN PRODUCTO. DEVUELVE LISTA DE TUPLA VACÍA SI NO HAY STOCK. DEVUELVE DATOS DEL PRODUCTO SI HAY STOCK.
def Validar_Stock(prod):
    consulta = []
    stock = Consultar_Producto("PRODUCTOS", "Descripcion", prod)
    if (len(stock) != 0) and stock[0][2] > 0:
        consulta = stock
    return consulta