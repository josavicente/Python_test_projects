from clases import Catalogo
from clases import Pelicula

# Creamos un catálogo
c = Catalogo()

# Mostramos el contenido
c.mostrar()

# Agregamos unas películas
c.agregar( Pelicula("El Padrino", 175, 1972) )
c.agregar( Pelicula("El Padrino: Parte 2", 202, 1974) )

# Mostramos el catálogo de nuevo
c.mostrar()

# Borramos el catálogo de la memoria ram (persistirá el fichero)
del(c)