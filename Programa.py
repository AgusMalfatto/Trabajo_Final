from Ventas import *

Crear_DB()
Crear_Tabla("PRODUCTOS")
Crear_Tabla("VENCIDOS")
Crear_Tabla_Pedidos()
Crear_Tabla_Ordenes_Venta()
lista_productos = []
opcion = 0
lista = [
    (106, "Leche", 10, 4, "2023-02-10", 'Lacteos'),
    (107, "Harina", 15, 2, "2025-06-22", 'Secos'),
    (108, "Arroz", 12, 2, "2023-01-15", 'Secos'),
    (109, "Fideos", 15, 3, "2023-02-11", 'Secos'),
    (110, "Manteca", 16, 4, "2022-12-25", 'Lacteos')
]

while opcion != 9:
    print("\n1. GENERAR VENTA")
    print("2. CONSULTA PEDIDOS")
    print("3. AGREGAR PRODUCTO")
    print("4. ELIMINAR UN PRODUCTO")
    print("5. ELIMINAR UN PRODUCTO VENCIDO")
    print("6. LISTAR PRODUCTOS")
    print("7. CONSULTA DE STOCK")
    print("8. ACTUALIZAR PRODUCTOS")
    print("9. SALIR DEL SISTEMA\n")

    opcion = Ingresar_Entero("\nIngrese opción de Menú: ", "\nOpción incorrecta.", 1, 9)
    
    if opcion == 1:
        Generar_Orden_de_Venta()
    elif opcion == 2:
        Menu_Ordenes_Ventas()
    elif opcion == 3:
        #Ingresar_Valores("PRODUCTOS", lista)
        Ingresar_Nuevo_Producto()      
    elif opcion == 4:
        Menu_Eliminar_Producto()
    elif opcion == 6:
        Mostrar_Tabla("PRODUCTOS")
    elif opcion == 8: 
        Menu_Modificaciones()

    '''if opcion in opciones:

    opciones = {
        1: Generar_Orden_de_Venta(),
        2: Menu_Ordenes_Ventas(),
        3: Ingresar_Valores("PRODUCTOS", lista),
        4: Eliminar_Valor("PRODUCTOS", 108),
        6: Mostrar_Tabla("PRODUCTOS"),
        8: Modificar_Valores("PRODUCTOS", 106, "Stock", 15)
    }'''

    