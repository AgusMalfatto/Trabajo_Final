import sqlite3

def Ingresar_Tabla(nombre):
    database = sqlite3.connect('Supermercado.db')
    cursor = database.cursor()
    comando = "CREATE TABLE " + nombre 
    cursor.execute("CREATE TABLE PRODUCTO" \
        "(Descripcion VARCHAR(100), Stock INTEGER, Precio FLOAT, Vencimiento VARCHAR(11))")
    
    database.commit()
    database.close()

def Ingresar_Valor():
    conexion = sqlite3.connect('Supermercado.db')
    cursor = conexion.cursor()

    # Insertamos un registro en la tabla de usuarios
    cursor.execute("INSERT INTO PRODUCTO VALUES " \
        "('Leche', 10, 120, '15/09/2022')")

    # Guardamos los cambios haciendo un commit
    conexion.commit()

    conexion.close()

def Mostrar_Tabla():
    database = sqlite3.connect('Supermercado.db')
    cursor = database.cursor()

    cursor.execute("SELECT * FROM PRODUCTO")

    productos = cursor.fetchall()

    print(productos)

    database.close()