from Ventas import *

Crear_DB()
Crear_Tabla("PRODUCTOS")
Crear_Tabla("VENCIDOS")
Crear_Tabla_Pedidos()
Crear_Tabla_Ordenes_Venta()
lista_productos = []
opcion = 0
lista = [
    (103, "ARVEJA", 35, 1, "2026-05-21", 0, "LATAS"),
    (104, "DULCE DE LECHE", 15, 2.5, "2022-12-25", 0, "LACTEOS"),
    (105, "AGUA", 25, 1.3, "2025-06-16", 0, "BEBIDAS"),
    (106, "LECHE", 10, 4, "2023-02-10", 0, 'LACTEOS'),
    (107, "HARINA", 15, 2, "2025-06-22", 0, 'SECOS'),
    (108, "ARROZ", 12, 2, "2023-01-15", 0, 'SECOS'),
    (109, "FIDEOS", 15, 3, "2023-02-11", 0, 'SECOS'),
    (110, "MANTECA", 16, 4, "2022-12-25", 0, 'LACTEOS')
]

while opcion != 10  :
    print("\n-------------- MENÚ PRINCIPAL --------------\n")
    print("\n1. GENERAR VENTA")
    print("2. CONSULTA PEDIDOS")
    print("3. AGREGAR PRODUCTO")
    print("4. ELIMINAR UN PRODUCTO")
    print("5. ELIMINAR UN PRODUCTO VENCIDO")
    print("6. LISTAR PRODUCTOS")
    print("7. CONSULTA DE STOCK")
    print("8. ACTUALIZAR PRODUCTOS")
    print("9. ARTÍCULO MÁS VENDIDO")
    print("10. SALIR DEL SISTEMA\n")

    opcion = Ingresar_Entero("\nIngrese opción de Menú: ", "\nOpción incorrecta.", 1, 10)
    
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
    elif opcion == 9:
        Calcular_Articulo_Mas_Vendido()

    '''if opcion in opciones:

    opciones = {
        1: Generar_Orden_de_Venta(),
        2: Menu_Ordenes_Ventas(),
        3: Ingresar_Valores("PRODUCTOS", lista),
        4: Eliminar_Valor("PRODUCTOS", 108),
        6: Mostrar_Tabla("PRODUCTOS"),
        8: Modificar_Valores("PRODUCTOS", 106, "Stock", 15)
    }'''

    