from Operaciones import *
from Tablas import *

Crear_DB()
lista_productos = []
opcion = 0

while opcion != 9:
    print("1. GENERAR VENTA")
    print("2. CONSULTA PEDIDOS")
    print("3. AGREGAR PRODUCTO")
    print("4. ELIMINAR UN PRODUCTO")
    print("5. ELIMINAR UN PRODUCTO VENCIDO")
    print("6. LISTAR PRODUCTOS")
    print("7. CONSULTA DE STOCK")
    print("8. ACTUALIZAR PRECIOS")
    print("9. SALIR DEL SISTEMA")

    opcion = Ingresar_Entero("Ingrese opción de Menú: ", "Opción incorrecta.", 1, 8)

    if opcion == 2:
        cadena = Ingresar_Cadena("Ingrese nombre de la tabla: ")
        Crear_Tabla(cadena)
        '''Ingresar_Valor()'''
    elif opcion == 3:
        Ingresar_Nuevo_Producto()
    elif opcion == 5:
        Mostrar_Tabla()   
'''elif opcion == 2:

elif opcion == 4:'''
    
'''elif opcion == 6:
elif opcion == 7:'''
