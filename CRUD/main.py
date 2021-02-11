import pyodbc
import pelicula
from bd import conexion

print('1.Consultar')
op = input('Seleccione una opción: ')

if op== "1":
    npelicula = pelicula.Pelicula()
    npelicula.obtener()
elif op == '2':
    npelicula = pelicula.Pelicula()
    Nombre = input('Escriba el nombre de la pelicula: ')
    Año = input('Año de estreno: ')
    npelicula.insertar(Nombre,Año)
    pass    
else:
    print('opción inválida')