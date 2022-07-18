import sqlite3

conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()

# cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))") 

# cursor.execute("INSERT INTO usuarios VALUES ('Josa', 42, 'jvicenpe@gmail.com' )")

# cursor.execute("SELECT * FROM usuarios")
# usuario = cursor.fetchone()

# usuarios = [
#   ('Mario', 51, 'mario@ejemplo.com'),
#   ('Mercedes', 30, 'mercedes@ejemplo.com'),
#   ('juan', 19, 'juan@ejemplo.com')
#]

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)
    
# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

conexion.commit()

conexion.close()