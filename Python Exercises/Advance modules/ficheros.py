from io import open

texto = "Una linea con texto \nOtra linea con texto"

fichero = open('fichero.txt', 'w')
fichero.write(texto)
fichero.close()


fichero = open('fichero.txt', 'r')
# Reading the file and assigning it to the variable `texto`.
texto = fichero.read
fichero.close()



fichero = open('fichero.txt', 'r')
lineas = fichero.readlines()
fichero.close()

print(lineas)

fichero = open('fichero.txt', 'a')

fichero.write('\nOtra linea mas en el fichero')

fichero.close()

# Opening the file and reading it line by line.
with open('fichero.txt', 'r') as fichero:
    for linea in fichero:
        print(linea)

fichero.close()
del(fichero)


# Moving the cursor to the 10th position in the file.
fichero = open('fichero.txt', 'r')
fichero.seek(10)

# It reads the file and returns a string with the content of the file.
fichero.read()

# It moves the cursor to the beginning of the file.
fichero.seek(0)

fichero.read(5)

fichero.seek(0)
texto = fichero.read()
fichero.seek(len(texto) / 2)

fichero.read()

fichero.close()
del(fichero)

# It opens the file in read and write mode.
fichero = open('fichero.txt', 'r+')

# Reading the file line by line and assigning it to the variable `lineas`.
# Then it is modifying the third line of the file.
# Then it is moving the cursor to the beginning of the file.
# Then it is writing the content of the variable `lineas` in the file.
lineas = fichero.readlines()

lineas[2] = 'Esta linea la he modificado en memoria'

fichero.seek(0)

fichero.writelines(lineas)

fichero.close()

