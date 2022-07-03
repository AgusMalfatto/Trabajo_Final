import sqlite3

# MUESTRA UN SOLO PRODUCTO ENVÍADO COMO PARÁMETRO EN FORMA DE TUPLA
def Mostrar_Un_Producto(prod):
    print("| {:^8} | {:^20} | {:^8} | {:^8} | {:^13} | {:^10} | {:^15} |".format (prod[0], prod[1], prod[2], prod[3], prod[4], prod[5], prod[6]))

# CREA UNA BASE DE DATOS
def Crear_DB():
    database = sqlite3.connect('Supermercado.db')
    database.commit()
    database.close()

# CREA UNA TABLA CON NOMBRE ENVIADO COMO PARÁMETRO
def Crear_Tabla(nombre):
    database = sqlite3.connect('Supermercado.db')
    cursor = database.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS " + nombre + """(
            Codigo integer,
            Descripcion text,
            Stock integer,
            Precio float,
            Vencimiento date,
            Descuento integer,
            Tipo text
        )      
        """
    )
        
    
    database.commit()
    database.close()

# CREA UNA TABLA PARA ORDENES DE VENTA
def Crear_Tabla_Ordenes_Venta():
    database = sqlite3.connect('Supermercado.db')
    cursor = database.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS ORDENES_VENTA (
            Orden_de_Venta integer,
            Cliente text,
            Direccion text,
            Telefono integer,
            Cantidad_Total integer,
            Cantidad_Prod integer,
            Precio_Final float,
            Entregado text
        )  
        """
    )    
    database.commit()
    database.close()

# CREA UNA TABLA PARA PEDIDOS
def Crear_Tabla_Pedidos():
    database = sqlite3.connect('Supermercado.db')
    cursor = database.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS PEDIDOS (
            Orden_de_Venta integer,
            Descripcion text,
            Cantidad integer,
            Precio_Total float
        )  
        """
    )   
    database.commit()
    database.close()

# INGRESA UN SOLO VALOR CON CADA CAMPO ENVIADO COMO PARÁMTERO
def Ingresar_Valor(nombre, codigo, descripcion, cantidad, precio, fecha, descuento, tipo):
    conexion = sqlite3.connect('Supermercado.db')
    cursor = conexion.cursor()
    comando = f"INSERT INTO {nombre} VALUES ('{codigo}', '{descripcion}', '{cantidad}', '{precio}', '{fecha}', '{descuento}', '{tipo}')"
    # Insertamos un registro en la tabla de usuarios
    cursor.execute(comando)
    # Guardamos los cambios haciendo un commit
    conexion.commit()
    conexion.close()

# INGRESA MUCHOS VALORES A LA VEZ ENVÍADOS COMO PARÁMETROS EN FORMA DE LISTA DE TUPLAS A LA TABLA DE ORDENES_VENTA
def Ingresar_Valores_Ordenes_Venta(values):
    conexion = sqlite3.connect('Supermercado.db')
    cursor = conexion.cursor()
    comando = f"INSERT INTO ORDENES_VENTA VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.executemany(comando, values)
    conexion.commit()
    conexion.close()

# INGRESA MUCHOS VALORES A LA VEZ ENVÍADOS COMO PARÁMETROS EN FORMA DE LISTA DE TUPLAS A LA TABLA DE PEDIDOS
def Ingresar_Valores_Pedidos(values):
    conexion = sqlite3.connect('Supermercado.db')
    cursor = conexion.cursor()
    comando = f"INSERT INTO PEDIDOS VALUES (?, ?, ?, ?)"
    cursor.executemany(comando, values)
    conexion.commit()
    conexion.close()

# SUMA LOS ELEMENTO DE UNA TABLA DE UNA COLUMNA ENVÍADA COMO PARÁMETRO. RETORNA UN VALOR EN UNA TUPLA DENTRO DE UNA LISTA
def Sumar(tabla, columna, columna_orden, orden):
    database = sqlite3.connect('Supermercado.db')
    cursor = database.cursor()
    comando = f"SELECT SUM({columna}) FROM {tabla} WHERE {columna_orden} = '{orden}'"
    cursor.execute(comando)
    producto = cursor.fetchall()
    database.commit()
    database.close()
    return producto

# INGRESA MUCHOS VALORES A LA VEZ ENVÍADOS COMO PARÁMETROS EN FORMA DE LISTA DE TUPLAS
def Ingresar_Valores(nombre, values):
    conexion = sqlite3.connect('Supermercado.db')
    cursor = conexion.cursor()
    comando = f"INSERT INTO {nombre} VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.executemany(comando, values)
    conexion.commit()
    conexion.close()

# MODIFICA UN ELEMENTO BASADO EN SU CÓDIGO, SE PASA EL ASPECTO A MODIFICAR Y SU NUEVO VALOR
def Modificar_Valores(tabla, codigo, columna, nuevo_valor, columna_codigo):
    conexion = sqlite3.connect('Supermercado.db')
    cursor = conexion.cursor()
    comando = f"UPDATE {tabla} SET {columna} = '{nuevo_valor}' WHERE {columna_codigo} = {codigo}"
    cursor.execute(comando)
    conexion.commit()
    conexion.close()

# ELIMINA UN ELEMENTO, SE ENVÍA EL NOMBRE DE LA TABLA Y EL CÓDIGO DEL ELEMENTO COMO PARÁMTERO
def Eliminar_Valor(tabla, columna,  valor):
    conexion = sqlite3.connect('Supermercado.db')
    cursor = conexion.cursor()
    comando = f"DELETE FROM {tabla} WHERE {columna} = {valor}"
    cursor.execute(comando)
    conexion.commit()
    conexion.close()

# BUSCA UN PRODUCTO DE UNA TABLA SEGÚN UN CÓDIGO ENVIADO COMO PARÁMETRO
def Consultar_Producto(tabla, columna, valor):
    database = sqlite3.connect('Supermercado.db')
    cursor = database.cursor()
    comando = f"SELECT * FROM {tabla} WHERE {columna} LIKE '{valor}'"
    cursor.execute(comando)
    producto = cursor.fetchall()
    database.commit()
    database.close()
    return producto

# DEVUELVE EL MÁXIMO O EL MÍNIMO VALOR DE LAS ORDENES DE VENTA
def Seleccionar_Orden(valor, columna, tabla):
    database = sqlite3.connect('Supermercado.db')
    cursor = database.cursor()
    comando = f"SELECT {valor}({columna}) FROM {tabla}"
    cursor.execute(comando)
    producto = cursor.fetchall()
    database.commit()
    database.close()
    return producto

def Contar(tabla):
    database = sqlite3.connect('Supermercado.db')
    cursor = database.cursor()
    comando = f"SELECT COUNT(*) FROM {tabla}"
    cursor.execute(comando)
    cantidad = cursor.fetchall()
    database.commit()
    database.close()
    return cantidad

def Consultar_Tabla(tabla):
    database = sqlite3.connect('Supermercado.db')
    cursor = database.cursor()
    comando = f"SELECT * FROM {tabla}"
    cursor.execute(comando)
    productos = cursor.fetchall()
    database.commit()
    database.close()
    return productos

# MUESTRA TODOS LOS VALORES DE UNA TABLA 
def Mostrar_Tabla(nombre):
    print("\n----------------------------------------- PRODUCTOS EN STOCK  -----------------------------------------\n")
    database = sqlite3.connect('Supermercado.db')
    cursor = database.cursor()
    comando = f"SELECT * FROM {nombre}"
    cursor.execute(comando)

    productos = cursor.fetchall()
    database.commit()
    database.close()
    print("\n+ {:-<8} + {:-<20} + {:-<8} + {:-<8} + {:-<13} + {:-<10} + {:-<15} +".format ("", "", "", "", "", "", ""))
    print("| {:^8} | {:^20} | {:^8} | {:^8} | {:^13} | {:^10} | {:^15} |".format ("CÓDIGO", "DESCRIPCIÓN", "STOCK", "PRECIO", "VENCIMIENTO", "DESCUENTO", "TIPO"))
    print("+ {:-<8} + {:-<20} + {:-<8} + {:-<8} + {:-<13} + {:-<10} + {:-<15} +".format ("", "", "", "", "", "", ""))
    for i in productos:
        Mostrar_Un_Producto(i)

    print("+ {:-<8} + {:-<20} + {:-<8} + {:-<8} + {:-<13} + {:-<10} + {:-<15} +\n".format ("", "", "", "", "", "", ""))

