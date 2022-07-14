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
