from bd import conexion

class Pelicula:
    def obtener(self):
      try:
        with conexion.cursor() as cursor:
        # En este caso no necesitamos limpiar ningún dato
         cursor.execute("SELECT id, titulo, anio FROM peliculas;")

        # Con fetchall traemos todas las filas
         peliculas = cursor.fetchall()
         print(peliculas)

        # Recorrer e imprimir
         for pelicula in peliculas:
            print(pelicula)
      except Exception as e:
        print("Ocurrió un error al consultar: ", e)
      finally:
       conexion.close()

    def insertar(self, nombre, año):
      try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO peliculas(titulo, anio) VALUES (?, ?);"
            cursor.execute(consulta, (nombre,año))


      except Exception as e:
           print("Ocurrió un error al insertar: ", e)
      finally:
           conexion.close()       