import sqlite3

conexion = sqlite3.connect("usuarios.db")

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

cursor.execute(''' 
               CREATE TABLE usuarios(
                   dni VARCHAR(9) PRIMARY KEY,
                   nombre VARCHAR(100),
                   edad INTEGER,
                   email VARCHAR(100)
                   )
               ''')

usuarios = [
   ('11111111','Mario', 51, 'mario@ejemplo.com'),
   ('22222222','Mercedes', 30, 'mercedes@ejemplo.com'),
   ('33333333','juan', 19, 'juan@ejemplo.com')
]


cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)


# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

conexion.commit()

conexion.close()