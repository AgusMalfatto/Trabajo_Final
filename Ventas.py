from ast import If
from Operaciones import *

def Mostrar_una_Venta(prod):
    print("{:<15} | {:<10} | {:<10} | ".format(prod[1], prod[2], prod[3]))

def Mostrar_Una_Orden(orden):
    print("{:<10} | {:<20} | {:<30} | {:<10} | {:<10} | {:<10} | {:<8} |".format(orden[0], orden[1], orden[2], orden[3], orden[4], orden[5], orden[6]))

def Numero_Orden_Venta():
    orden = Seleccionar_Orden("MAX")
    if not(orden[0][0] is None):
        orden = orden[0][0] + 1
    else:
        orden = 100
    return orden

def Mostrar_Ticket(cantidad, lista):
    print("{:<10} | {:<15} | {:<10} |".format(cantidad, lista[0][1], lista[0][3]))

# SOLICITA Y VALIDA DATOS PARA LOS PRODUCTOS QUE DESEE EL CLIENTE, LOS DEVUELVE EN LISTA
def Generar_Venta():    
    venta = []
    cadena = Ingresar_Cadena("\nIngrese el producto desea comprar: ")
    stock_producto = Validar_Stock(cadena)
    
    if len(stock_producto) > 0:
        cantidad = Ingresar_Entero("\nIngrese cantidad de unidades: ", "No hay stock suficiente", 1, stock_producto[0][2])
        venta = [cadena, cantidad]
    else:
        print(f"No hay stock suficiente de {cadena}")
    return venta
    
# RECIBE LA LISTA DE PRODUCTOS QUE DESEA EL CLIENTE Y LOS DATOS DEL CLIENTE. 
# SE ALMACENA EN BD Y SE IMPRIME EL TICKET
def Procesar_Venta(lista, orden):
    total_precio = Sumar("PEDIDOS", "Precio_Total", orden)
    hora = datetime.now()
    dia = date.today()
    print("\n*******************************************")
    print(f"\n{dia}  |  {hora.hour}:{hora.minute} hs")
    print("\n{:<10} | {:<15} | {:<10} |".format("CANTIDAD", "PRODUCTO", "PRECIO U."))

    for producto in lista: # RECORRO LA LISTA DE PRODUCTOS
        datos_producto = Validar_Stock(producto[0]) 
        Mostrar_Ticket(producto[1], datos_producto)

    print(f"\nTOTAL DE COMPRA: ${total_precio[0][0]}")
    print("\n*******************************************")

# SOLICITA LOS DATOS DEL CLIENTE
def Pedir_Datos_Cliente():
    nombre_cliente = Ingresar_Cadena("\nIngrese el nombre del cliente: ")
    direccion = Ingresar_Cadena("\nIngrese la dirección del cliente: ")
    telefono = Ingresar_Entero("\nIngrese el número del cliente: ", "\nNúmero de teléfono no válido (debe iniciar con 42...)", 42000000, 42999999)
    datos_cliente = [nombre_cliente, direccion, telefono]

    return datos_cliente

# AGREGO LOS DATOS DE LA VENTA A LA BD DE ORDENES DE VENTA
def Actualizar_Ordenes_Venta(datos_cliente, orden):
    productos = Consultar_Producto("PEDIDOS", "Orden_de_Venta", orden)
    total_productos = Sumar("PEDIDOS", "CANTIDAD", orden)
    total_precio = Sumar("PEDIDOS", "Precio_Total", orden)
    pedido = [(orden, datos_cliente[0], datos_cliente[1], datos_cliente[2], total_productos[0][0], len(productos), total_precio[0][0])]
    Ingresar_Valores_Ordenes_Venta(pedido)

# AGREGO LOS DATOS DE LA VENTA A LA BD DE PEDIDOS
def Actualizar_BD_Pedido(lista_productos, orden):
    for producto in lista_productos:
        datos_producto = Validar_Stock(producto[0])
        pedido = [(orden, producto[0], producto[1], datos_producto[0][3] * producto[1])]
        Ingresar_Valores_Pedidos(pedido)

# GENERA LA VENTA.
def Generar_Orden_de_Venta():
    Mostrar_Tabla("PRODUCTOS")
    compra = []
    valor = 'si'
    while valor == 'si':
        un_producto = Generar_Venta()
        if len(un_producto) > 0:
            compra.append(un_producto)
        valor = Ingresar_Tipo("¿Desea seguir comprando? ", "Caracter no válido ('si' o 'no')", 'si', 'no')

    datos_cliente = Pedir_Datos_Cliente()
    orden = Numero_Orden_Venta()
    Actualizar_BD_Pedido(compra, orden)
    Actualizar_Ordenes_Venta(datos_cliente, orden)
    Procesar_Venta(compra, orden)

def Mostrar_Ventas(orden):
    ventas = Consultar_Producto("PEDIDOS", "Orden_de_Venta", orden)
    cliente = Consultar_Producto("ORDENES_VENTA", "Orden_de_Venta", orden)
    print(f"\nPedido de {cliente[0][1]}")
    print("\n{:<15} | {:<10} | {:<10} | ".format("PRODUCTO", "CANTIDAD", "PRECIO"))    
    for prod in ventas:
        Mostrar_una_Venta(prod)


def Mostrar_Ordenes_Venta():
    pedidos = Consultar_Tabla("ORDENES_VENTA")
    print("\n{:<10} | {:<20} | {:<30} | {:<10} | {:<10} | {:<10} | {:<8} |".format("N° ORDEN", "CLIENTE", "DIRECCIÓN", "TELÉFONO", "BULTOS", "PRODUCTOS", "PRECIO"))
    for orden in pedidos:
        Mostrar_Una_Orden(orden)

def Consultar_Orden_Venta():
    maximo = Seleccionar_Orden("MAX")
    orden = Ingresar_Entero("Ingrese la orden de venta: ", "Orden de venta no válida", 100, maximo[0][0])
    Mostrar_Ventas(orden)


def Menu_Ordenes_Ventas():
    cont = Contar("ORDENES_VENTA")
    if len(cont) > 0:        
        valor = 0
        while valor != 3:
            Mostrar_Ordenes_Venta()
            print("\n1. Consultar Orden de venta.")
            print("2. Generar una venta.")
            print("3. Volver al menú.")

            valor = Ingresar_Entero("\nIngrese opción de menú: ", "\nOpción de menú incorrecta", 1, 3)

            if valor == 1:
                Consultar_Orden_Venta()
            elif valor == 2:
                Generar_Orden_de_Venta()
            
    else:
        print("\nAún no se han generado ventas.\n")