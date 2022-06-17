from Ingresar_Datos import *

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

    if opcion == 1:
        print("hola")
'''  elif opcion == 2:
elif opcion == 3:
elif opcion == 4:
elif opcion == 5:
elif opcion == 6:
elif opcion == 7:'''
