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

