import sqlite3

# MUESTRA UN SOLO PRODUCTO ENVÍADO COMO PARÁMETRO EN FORMA DE TUPLA
def Mostrar_Un_Producto(prod):
    print("{:<8} | {:<20} | {:<8} | {:<8} | {:<13} | {:<15}".format (prod[0], prod[1], prod[2], prod[3], prod[4], prod[5]))

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
            Codigo text,
            Descripcion text,
            Stock integer,
            Precio float,
            Vencimiento date,
            Tipo text
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
            Codigo text,
            Descripcion text,
            Cantidad integer,
            Precio float,
            Vencimiento date,
            Precio_Final float
        )  
        """
    )
        
    
    database.commit()
    database.close()

# INGRESA UN SOLO VALOR CON CADA CAMPO ENVIADO COMO PARÁMTERO
def Ingresar_Valor(nombre, codigo, descripcion, cantidad, precio, fecha, tipo):
    conexion = sqlite3.connect('Supermercado.db')
    cursor = conexion.cursor()
    comando = f"INSERT INTO {nombre} VALUES ('{codigo}', '{descripcion}', '{cantidad}', '{precio}', '{fecha}', '{tipo}')"
    # Insertamos un registro en la tabla de usuarios
    cursor.execute(comando)
    # Guardamos los cambios haciendo un commit
    conexion.commit()
    conexion.close()

# INGRESA MUCHOS VALORES A LA VEZ ENVÍADOS COMO PARÁMETROS EN FORMA DE LISTA DE TUPLAS
def Ingresar_Valores(nombre, values):
    conexion = sqlite3.connect('Supermercado.db')
    cursor = conexion.cursor()
    comando = f"INSERT INTO {nombre} VALUES (?, ?, ?, ?, ?, ?)"
    cursor.executemany(comando, values)
    conexion.commit()
    conexion.close()

# MODIFICA UN ELEMENTO BASADO EN SU CÓDIGO, SE PASA EL ASPECTO A MODIFICAR Y SU NUEVO VALOR
def Modificar_Valores(nombre, codigo, valor, nuevo_valor):
    conexion = sqlite3.connect('Supermercado.db')
    cursor = conexion.cursor()
    comando = f"UPDATE {nombre} SET {valor} = {nuevo_valor} WHERE Codigo = {codigo}"
    cursor.execute(comando)
    conexion.commit()
    conexion.close()

# ELIMINA UN ELEMENTO, SE ENVÍA EL NOMBRE DE LA TABLA Y EL CÓDIGO DEL ELEMENTO COMO PARÁMTERO
def Eliminar_Valor(nombre, valor):
    conexion = sqlite3.connect('Supermercado.db')
    cursor = conexion.cursor()
    comando = f"DELETE FROM {nombre} WHERE Codigo = {valor}"
    cursor.execute(comando)
    conexion.commit()
    conexion.close()

# MUESTRA TODOS LOS VALORES DE UNA TABLA
def Mostrar_Tabla(nombre):
    database = sqlite3.connect('Supermercado.db')
    cursor = database.cursor()
    comando = f"SELECT * FROM {nombre}"
    cursor.execute(comando)

    productos = cursor.fetchall()
    print("\n{:<8} | {:<20} | {:<8} | {:<8} | {:<13} | {:<15}\n".format ("CÓDIGO", "DESCRIPCIÓN", "STOCK", "PRECIO", "VENCIMIENTO", "TIPO"))

    for i in productos:
        Mostrar_Un_Producto(i)

    database.close()