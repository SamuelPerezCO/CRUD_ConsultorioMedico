from db_connector import conectar, cerrar_conexion

# Conectar a la base de datos
conexion = conectar()

# Realizar operaciones con la base de datos
if conexion:
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Paciente")
    resultados = cursor.fetchall()
    print(resultados)

    # Cerrar conexión
    cerrar_conexion(conexion)
