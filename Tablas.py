import sqlite3

def Mostrar_Un_Producto(prod):
    print("{:<8} | {:<20} | {:<8} | {:<8} | {:<10} | {:<15}".format (prod[0], prod[1], prod[2], prod[3], prod[4], prod[5]))

def Crear_DB():
    database = sqlite3.connect('Supermercado.db')
    database.commit()
    database.close()

def Crear_Tabla(nombre):
    database = sqlite3.connect('Supermercado.db')
    cursor = database.cursor()
    cursor.execute(
        "CREATE TABLE " + nombre + """(
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

def Ingresar_Valor(nombre, codigo, descripcion, cantidad, precio, fecha, tipo):
    conexion = sqlite3.connect('Supermercado.db')
    cursor = conexion.cursor()
    comando = f"INSERT INTO {nombre} VALUES ('{codigo}', '{descripcion}', '{cantidad}', '{precio}', '{fecha}', '{tipo}')"
    # Insertamos un registro en la tabla de usuarios
    cursor.execute(comando)

    # Guardamos los cambios haciendo un commit
    conexion.commit()

    conexion.close()

def Mostrar_Tabla():
    database = sqlite3.connect('Supermercado.db')
    cursor = database.cursor()

    cursor.execute("SELECT * FROM PRODUCTOS")

    productos = cursor.fetchall()
    print("{:<8} | {:<20} | {:<8} | {:<8} | {:<10} | {:<15}".format ("CÓDIGO", "DESCRIPCIÓN", "STOCK", "PRECIO", "VENCIMIENTO", "TIPO"))

    for i in productos:
        Mostrar_Un_Producto(i)

    database.close()