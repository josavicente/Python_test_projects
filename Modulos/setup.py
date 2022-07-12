from setuptools import setup

# Creating a setup.py file.
setup(
    name='Mensajes',
    version='1.1',
    description='Un paquete para saludar',
    author='Josavicente',
    author_email='jvicenpe@gmail.com',
    url='http://www.google.es',
    packages=['mensajes', 'mensajes.hola'],
    scripts=['test.py']
) 