from Ingresar_Datos import *
from Tablas import Ingresar_Tabla, Ingresar_Valor, Mostrar_Tabla

lista_productos = []

opcion = 0

while opcion != 8:
    print("1. GENERAR VENTA")
    print("2. AGREGAR PRODUCTO")
    print("3. ELIMINAR UN PRODUCTO")
    print("4. ELIMINAR UN PRODUCTO VENCIDO")
    print("5. LISTAR PRODUCTOS")
    print("6. CONSULTA DE STOCK")
    print("7. ACTUALIZAR PRECIOS")
    print("8. SALIR DEL SISTEMA")

    opcion = Ingresar_Entero("Ingrese opción de Menú: ", "Opción incorrecta.", 1, 8)

    if opcion == 2:
        #cadena = Ingresar_Cadena("Ingrese nombre de la tabla: ")
        #Ingresar_Tabla(cadena)
        Ingresar_Valor()
    elif opcion == 5:
        Mostrar_Tabla()   
'''elif opcion == 2:
elif opcion == 3:
elif opcion == 4:'''
    
'''elif opcion == 6:
elif opcion == 7:'''
