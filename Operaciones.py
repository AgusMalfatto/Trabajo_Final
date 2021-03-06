from Ingresar_Datos import *


# PERMITE INGRESAR LOS DATOS DE UN NUEVO PRODUCTO
def Ingresar_Nuevo_Producto():
    print("\n-------------- INGRESAR NUEVO PRODUCTO --------------\n")
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
    descuento = Ingresar_Entero("Ingrese el descuento del producto (en caso de no tener descuento ingrese 'cero'): ", "\n>> Descuento no válido.", 0, 90)
    print("\n")
    for i in tipos:
        print(f"{i} - ", end="")

    tipo = Ingresar_Tipo("\nIngrese el tipo del producto: ", "Tipo no válido", 
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

    Ingresar_Valor("PRODUCTOS", codigo, descripcion.upper(), cantidad, precio, fecha, descuento, tipo.upper())

# CONSULTA EL STOCK DE UN PRODUCTO. DEVUELVE LISTA DE TUPLA VACÍA SI NO HAY STOCK. DEVUELVE DATOS DEL PRODUCTO SI HAY STOCK.
def Validar_Stock(prod):
    consulta = []
    stock = Consultar_Producto("PRODUCTOS", "Descripcion", prod)
    if (len(stock) != 0) and stock[0][2] > 0:
        consulta = stock
    return consulta

# SOLICITA EL NUEVO VALOR Y MODIFICA LA BD
def Modificar(*args): # funcion, codigo, columna, 
    valor = args[0](args[3], args[4], args[5], args[6])
    Modificar_Valores("PRODUCTOS", args[1], args[2], valor, "Codigo")

# MODIFICA EL PRECIO DEL PRODUCTO SEGÚN UN PORCENTAJE RECIBIDO
def Calcular_Porcentaje(precio, porcentaje, codigo):
    precio += (precio * porcentaje / 100)
    Modificar_Valores("PRODUCTOS", codigo, "Precio", precio, "Codigo")

# MENÚ PARA MODIFICAR UN PRECIO
def Menu_Modificar_Precio(codigo):
    print("\n-------------- MENU MODIFICAR PRECIO --------------\n")
    producto = Consultar_Producto("PRODUCTOS", "Codigo", codigo)
    print("\n1. Colocar nuevo precio.")
    print("2. Actualizar con porcentaje.")

    opcion = Ingresar_Entero("\nIngrese opción: ", ">> Opcion no válida", 1, 2)

    if opcion == 1:
        Modificar(Ingresar_Precio, codigo, "Precio", "\nIngrese el nuevo precio: ", ">> Precio no válido.", 1, 30)
    elif opcion == 2:
        porcentaje = Ingresar_Entero("\nIngrese el porcentaje de aumento: ", ">> Porcentaje no válido.", 1, 200)
        Calcular_Porcentaje(producto[0][3], porcentaje, codigo)

# MENÚ PARA MODIFICAR UN PRODUCTO RECIBIDO CÓMO PARÁMETRO
def Menu_Modificar(codigo, producto):
    opcion = 0

    while opcion != 4:
        print("\n-------------- MENÚ MODIFICACIONES --------------\n")
        print("\n1. MODIFICAR STOCK.")
        print("2. MODIFICAR PRECIO.")
        print("3. MODIFICAR DESCUENTO.")
        print("4. VOLVER AL MENÚ PRINCIPAL.")

        opcion = Ingresar_Entero("\nIngrese opción de menú: ", ">> Opción de menú no válida.", 1, 4)

        if opcion == 1:
            Modificar(Ingresar_Entero, codigo, "Stock", "\nIngresar el nuevo stock: ", ">> Valor no válido.", 1, 50)
            print(f"\nSe ha modificado el stock del producto '{producto}'")
        elif opcion == 2:
            Menu_Modificar_Precio(codigo)
            print(f"\nSe ha modificado el precio del producto '{producto}'")
        elif opcion == 3:
            Modificar(Ingresar_Entero, codigo, "Descuento", "\nIngresar el nuevo descuento: ", "\n>> Descuento no válido.", 0, 90)
            print(f"\nSe ha modificado el descuento del producto '{producto}'")

# MENÚ PARA MODIFICAR PRODUCTOS
def Menu_Modificaciones():    
    opcion = 'si'

    while opcion.lower() == 'si':
        Mostrar_Tabla("PRODUCTOS")
        min, max = Seleccionar_Orden("MIN", "Codigo", "PRODUCTOS"), Seleccionar_Orden("MAX", "Codigo", "PRODUCTOS")
        codigo = Ingresar_Entero("\nIngrese código del producto a modificar: ", "Código incorrecto.", int(min[0][0]), int(max[0][0]))
        consulta = Consultar_Producto("PRODUCTOS", "Codigo", codigo)
        if not(consulta[0][0] is None):
            Menu_Modificar(codigo, consulta[0][1])
            opcion = Ingresar_Tipo("\nDesea modificar un nuevo producto: ", "Respuesta incorrecta ('si' o 'no')", 'si', 'no')
        else:
            print(f"\nNo se encuentra el producto '{consulta[0][1]}' en Stock.\n")

# ELIMINA UN PRODUCTO DE LA BD
def Menu_Eliminar_Producto():
    print("\n-------------- ELIMINAR UN PRODUCTO --------------\n")
    Mostrar_Tabla("PRODUCTOS")
    maximo = Seleccionar_Orden("MAX", "Codigo", "PRODUCTOS")
    codigo = Ingresar_Entero("\nIngrese el Código del producto a eliminar: ", ">> Código no válido o no encontrado en stock", 100, maximo[0][0])
    consulta = Consultar_Producto("PRODUCTOS", "Codigo", codigo)
    if not(consulta[0][0] is None):
        Eliminar_Valor("PRODUCTOS", "Codigo", codigo)
        print(f"\nEl producto '{consulta[0][1]}' ha sido eliminado correctamente.\n")
        valor = 1
    else:
        print(f"\n>> No se encuentra producto en stock con códgio: {codigo}")

# CALCULA EL DESCUENTO DE UN PRODUCTO ENVÍADO COMO PARÁMETRO SEGÚN SU FECHA DE VENCIMIENTO
def Calcular_Descuento(producto):
    vencimiento = Consultar_Producto("PRODUCTOS", "Descripcion", producto[1])
    vencimiento = str(vencimiento[0][4])
    vencimiento = datetime.strptime(vencimiento, "%Y-%m-%d")
    fecha_actual = datetime.today()
    diferencia = vencimiento - fecha_actual
    descuento = 0

    if (diferencia.days <= 7):
        descuento = 10

    return descuento

# DETERMINA EL ARTÍCULO MÁS VENDIDO
def Articulo_Mas_Vendido(productos, tipo = 0):
    dic = dict()
    for un_producto in productos:
        if not(un_producto[1] in dic):
            suma_producto = Sumar("PEDIDOS", "Cantidad", "Descripcion", un_producto[1])
            if suma_producto[0][0] != None:
                dic[un_producto[1]] = suma_producto[0][0]
    valores = list(dic.values()) 
    if len(valores) > 0:
        valor = max(valores)      
        lista = list()
        for i in dic:
            if dic[i] == valor:
                lista.append(i)
        if tipo == 0:
            print("\nLos artículos más vendidos son: ")             
        else:
            print(f"\nLos artículos más vendidos de tipo '{tipo}' son:")
        for i in lista:
                print(f">> {i}")
    else:
        print(f"\nNo se han generado ventas de artículos de categoría '{tipo}'")   

# MENÚ PARA BUSCAR EL ARTÍCULO MÁS VENDIDO
def Calcular_Articulo_Mas_Vendido():

    print("\n-------------- MENÚ ARTÍCULOS MÁS VENDIDOS --------------\n")
    opcion = 0
    cantidad_pedidos = Contar("PEDIDOS")
    if cantidad_pedidos[0][0] != 0:
        while opcion != 3:
            print("\n1. Consultar artículo más vendido.")
            print("2. Consultar artículo más vendido según el tipo.")
            print("3. Volver al menú principal.")

            opcion = Ingresar_Entero("\nIngrese opción de menú: ", ">> Opción de menú no válida", 1, 3)

            if opcion == 1:            
                productos = Consultar_Tabla("PEDIDOS")
                Articulo_Mas_Vendido(productos)
            elif opcion == 2:
                tipo_ingresado = Ingresar_Tipo("\nIngrese el tipo de producto que desee consultar: ", ">> Artículo no válido", "lacteos",
                "verduleria",
                "secos",
                "higiene",
                "carnes",
                "bebidas",
                "vinos",
                "latas",
                "galletitas")
                productos = Consultar_Producto("PRODUCTOS", "Tipo", tipo_ingresado)
                
                Articulo_Mas_Vendido(productos, tipo_ingresado)

    else:
        print("\nAún no se han generado ventas.\n")

# MUESTRA LA CONSULTA DE STOCK
def Mostrar_Consulta(columna, consulta):
    producto_consultado = Consultar_Producto("PRODUCTOS", columna, consulta)
    if len(producto_consultado) > 0:
        print("\n+ {:-<8} + {:-<20} + {:-<8} + {:-<8} + {:-<13} + {:-<10} + {:-<15} +".format ("", "", "", "", "", "", ""))
        print("| {:^8} | {:^20} | {:^8} | {:^8} | {:^13} | {:^10} | {:^15} |".format ("CÓDIGO", "DESCRIPCIÓN", "STOCK", "PRECIO", "VENCIMIENTO", "DESCUENTO", "TIPO"))
        print("+ {:-<8} + {:-<20} + {:-<8} + {:-<8} + {:-<13} + {:-<10} + {:-<15} +".format ("", "", "", "", "", "", ""))
        for i in producto_consultado:
            Mostrar_Un_Producto(i)

        print("+ {:-<8} + {:-<20} + {:-<8} + {:-<8} + {:-<13} + {:-<10} + {:-<15} +\n".format ("", "", "", "", "", "", ""))
    else:
        print(f"\nNo se ha encontrado producto con {columna}: {consulta}")

# MENÚ PARA CONSULTAR EL STOCK
def Menu_Consultar_Stock():
    opcion = 0

    while opcion != 3:
        print("\n------------ MENU CONSULTA DE STOCK ------------\n")
        print("\n1. Consultar por código.")
        print("2. Consultar por descripción.")
        print("3. Volver al menú principal.")

        opcion = Ingresar_Entero("\nIngrese opción de menú: ", ">> Opción de menú no válida.", 1, 3)
        
        if opcion == 1:
            consulta = Ingresar_Entero("\nIngrese el cóodigo del producto: ", ">> Código no válido.", 100, 9000)
            Mostrar_Consulta("Codigo", consulta)
        elif opcion == 2:
            consulta = Ingresar_Cadena("\nIngrese la descripción del producto: ")
            Mostrar_Consulta("Descripcion", consulta)

# ELIMINA LOS PRODUCTOS VENCIDOS DE LA BD 'PRODUCTOS' Y LAS AGREGA A LA BD 'VENCIDOS'
def Recargar_Modulos():
    fecha_actual = datetime.today()
    productos = Consultar_Producto_Vencido("PRODUCTOS", fecha_actual)
    if len(productos) > 0:
        for prod in productos:
            Eliminar_Valor("PRODUCTOS", "Codigo", prod[0])
        Ingresar_Valores("VENCIDOS", productos)
        print("\nMódulos recargados correctamente.")
    else:
        print("\nNo hay productos vencidos hasta la fecha.")
    
# LISTA TODOS LOS PRODUCTOS EN STOCK O LOS PRODUCTOS VENCIDOS
def Listado_Stock():
    opcion = 0

    while opcion != 3:
        print("\n------------ MENÚ LISTADO DE PRODUCTOS ------------\n")
        print("\n1. Mostrar listado de productos en Stock.")
        print("2. Mostrar listado de productos vencidos.")
        print("3. Volver al menú principal.")

        opcion = Ingresar_Entero("\nIngrese opción de menú: ", ">> Opción de menú incorrecta", 1, 3)

        if opcion == 1:
            Mostrar_Tabla("PRODUCTOS")
        elif opcion == 2:
            cantidad = Contar("VENCIDOS")
            if cantidad[0][0] != 0:
                Mostrar_Tabla("VENCIDOS")
            else:
                print("\nNo se han registrado productos vencidos.")