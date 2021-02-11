from bd import conexion

class Eliminar():

    def eliminar(self):
      try:
         with conexion.cursor() as cursor:

        consulta = "DELETE FROM peliculas WHERE anio < ?;"
        anio = 2000
        cursor.execute(consulta, (anio))
 
       # No olvidemos hacer commit cuando hacemos un cambio a la BD
        conexion.commit()
      except Exception as e:
        print("Error eliminando: ", e)
      finally:
        conexion.close()
