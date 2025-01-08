from db_connector import conectar, cerrar_conexion
import sqlite3

# Función para obtener pacientes
def obtener_pacientes():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Paciente")
            resultados = cursor.fetchall()
            return resultados
        except sqlite3.Error as e:
            print(f"Error al obtener pacientes: {e}")
            return []
        finally:
            cerrar_conexion(conexion)

# Función para agregar un nuevo paciente
def agregar_paciente(datos_paciente):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO Paciente (
                    nombre_completo, fecha_nacimiento, genero, numero_identificacion, telefono,
                    correo_electronico, direccion, tipo_sangre, alergias, condiciones_medicas,
                    nombre_contacto_emergencia, telefono_emergencia, relacion_contacto
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, datos_paciente)
            conexion.commit()
            print("Paciente agregado exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al agregar paciente: {e}")
        finally:
            cerrar_conexion(conexion)

def buscar_paciente(id_paciente):
    conexion, cursor = conectar()
    cursor.execute("SELECT * FROM Paciente WHERE id_paciente = ?", (id_paciente,))
    paciente = cursor.fetchone()
    conexion.close()
    return paciente


# Actualizar información de un paciente
def actualizar_paciente(id_paciente, nuevos_datos):
    conexion, cursor = conectar()
    cursor.execute("""
        UPDATE Paciente
        SET nombre_completo = ?, fecha_nacimiento = ?, genero = ?, numero_identificacion = ?, telefono = ?,
            correo_electronico = ?, direccion = ?, tipo_sangre = ?, alergias = ?, condiciones_medicas = ?,
            nombre_contacto_emergencia = ?, telefono_emergencia = ?, relacion_contacto = ?
        WHERE id_paciente = ?
    """, (*nuevos_datos, id_paciente))
    conexion.commit()
    conexion.close()

# Eliminar un paciente
def eliminar_paciente(id_paciente):
    conexion, cursor = conectar()
    cursor.execute("DELETE FROM Paciente WHERE id_paciente = ?", (id_paciente,))
    conexion.commit()
    conexion.close()

# Ejemplo de uso
# if __name__ == "__main__":
#     # Leer pacientes
#     pacientes = obtener_pacientes()
#     print("Pacientes existentes:", pacientes)

#     # Agregar un paciente
#     nuevo_paciente = (
#         "Pedro González", "1990-05-20", "M", "123456789", "555-7890",
#         "pedro@example.com", "Calle 123", "O+", "Ninguna", "Ninguna",
#         "María López", "555-5678", "Madre"
#     )
#     agregar_paciente(nuevo_paciente)

#     # Leer pacientes nuevamente
#     pacientes = obtener_pacientes()
#     print("Pacientes actualizados:", pacientes)
