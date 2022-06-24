from Ingresar_Datos import *


# PERMITE INGRESAR LOS DATOS DE UN NUEVO PRODUCTO
def Ingresar_Nuevo_Producto():
    tipos = (
        "lacteos",
        "verduleria",
        "secos",
        "higiene",
        "carnes",
        "bebidas",
        "vinos",
        "latas",
        "galletitas"
    )
    codigo = Definir_Codigo()
    descripcion = Ingresar_Cadena("Ingrese la descripción del producto: ")
    cantidad = Ingresar_Entero("Ingrese cantidad de productos: ", "Cantidad no válida", 1, 50)
    precio = Ingresar_Precio("Ingrese el precio del producto: ", "Precio no válido", 1, 30)
    fecha = Ingresar_Fecha()
    for i in tipos:
        print(f"{i} - ", end="")
    tipo = Ingresar_Tipo("Ingrese el tipo del producto: ", "Tipo no válido", 
        "lacteos",
        "verduleria",
        "secos",
        "higiene",
        "carnes",
        "bebidas",
        "vinos",
        "latas",
        "galletitas"
        )
    Ingresar_Valor("PRODUCTOS", codigo, descripcion, cantidad, precio, fecha, tipo)

# CONSULTA EL STOCK DE UN PRODUCTO. DEVUELVE LISTA DE TUPLA VACÍA SI NO HAY STOCK. DEVUELVE DATOS DEL PRODUCTO SI HAY STOCK.
def Validar_Stock(prod):
    consulta = []
    stock = Consultar_Producto("PRODUCTOS", "Descripcion", prod)
    if (len(stock) != 0) and stock[0][2] > 0:
        consulta = stock
    return consulta

def Modificar(*args): # funcion, codigo, columna, 
    valor = args[0](args[3], args[4], args[5], args[6])
    Modificar_Valores("PRODUCTOS", args[1], args[2], valor)

def Menu_Modificar(codigo):
    opcion = 0

    while opcion != 3:
        print("1. MODIFICAR STOCK.")
        print("2. MODIFICAR PRECIO.")
        print("3. VOLVER AL MENÚ PRINCIPAL.")

        opcion = Ingresar_Entero("Ingrese opción de menú: ", "Opción de menú no válida.", 1, 3)

        if opcion == 1:
            Modificar(Ingresar_Entero, codigo, "Stock", "Ingresar el nuevo stock: ", "Valor no válido.", 1, 50)
        elif opcion == 2:
            Modificar(Ingresar_Precio, codigo, "Precio", "Ingrese el nuevo precio: ", "Precio no válido.", 1, 30)


def Menu_Modificaciones():    
    opcion = 'si'

    while opcion.lower() == 'si':
        Mostrar_Tabla("PRODUCTOS")
        min, max = Seleccionar_Orden("MIN", "Codigo", "PRODUCTOS"), Seleccionar_Orden("MAX", "Codigo", "PRODUCTOS")
        codigo = Ingresar_Entero("Ingrese código del producto a modificar: ", "Código incorrecto.", int(min[0][0]), int(max[0][0]))

        Menu_Modificar(codigo)

        opcion = Ingresar_Tipo("Desea modificar un nuevo producto: ", "Respuesta incorrecta ('si' o 'no')", 'si', 'no')

def Menu_Eliminar_Producto():
    Mostrar_Tabla("PRODUCTOS")
    maximo = Seleccionar_Orden("MAX", "Codigo", "PRODUCTOS")
    valor = 0
    while valor == 0:
        orden = Ingresar_Entero("Ingrese el Código del producto a eliminar: ", ">> Código no válido o no encontrado en stock", 100, maximo[0][0])
        consulta = Consultar_Producto("PRODUCTOS", "Codigo", orden)
        if not(consulta[0][0] is None):
            Eliminar_Valor("PRODUCTOS", "Codigo", orden)
            valor = 1
        else:
            print(f">> No se encuentra producto en stock con códgio: {orden}")