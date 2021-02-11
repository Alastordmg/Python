import pyodbc
direccion_servidor = 'localhost'
nombre_bd = 'test'
nombre_usuario = 'sa'
password = 'masterkey'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    print('conexion exitosa')
    # OK! conexión exitosa
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)