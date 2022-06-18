from Ingresar_Datos import *
from Tablas import Ingresar_Valor


def Ingresar_Nuevo_Producto():
    '''codigo = Definir_Codigo(lista)'''
    descripcion = Ingresar_Cadena("\nIngrese la descripción del producto: ")
    cantidad = Ingresar_Entero("\nIngrese cantidad de productos: ", "Cantidad no válida", 1, 50)
    precio = Ingresar_Precio("Ingrese el precio del producto: ", "Precio no válido", 1, 30)
    fecha = Ingresar_Fecha()
    '''tipo = Ingresar_Tipo("Ingrese el tipo del producto: ", "Tipo no válido", "Lacteos", )'''
    Ingresar_Valor("PRODUCTOS", 101, descripcion, cantidad, precio, fecha, 'L')

