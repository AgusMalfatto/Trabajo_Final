import sqlite3

def Crear_DB():
    database = sqlite3.connect('Supermercado.db')
    database.commit()
    database.close()

def Ingresar_Tabla(nombre):
    database = sqlite3.connect('Supermercado.db')
    cursor = database.cursor()
    cursor.execute(
        "CREATE TABLE " + nombre + """(
            Codigo text,
            Stock integer,
            Precio float,
            Vencimiento text,
            Tipo text
        )      
        """
    )
        
    
    database.commit()
    database.close()

def Ingresar_Valor(nombre):
    conexion = sqlite3.connect('Supermercado.db')
    cursor = conexion.cursor()
    comando = "INSERT INTO " + nombre +" VALUES "
    # Insertamos un registro en la tabla de usuarios
    cursor.execute( 
        comando + """(
            
        )
        """
       )

    # Guardamos los cambios haciendo un commit
    conexion.commit()

    conexion.close()

def Mostrar_Tabla():
    database = sqlite3.connect('Supermercado.db')
    cursor = database.cursor()

    cursor.execute("SELECT * FROM PEDIDOS")

    productos = cursor.fetchall()

    print(productos)

    database.close()