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
                    correo_electronico, direccion, tipo_sangre, alergias, condiciones_medicas_preexistentes,
                    medicamentos_actuales , nombre_contacto_emergencia, telefono_emergencia, relacion_paciente
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
def actualizar_paciente(dni, nuevos_datos):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                UPDATE Paciente
                SET 
                    nombre_completo = ?, fecha_nacimiento = ?, genero = ?, numero_identificacion = ?, telefono = ?,
                    correo_electronico = ?, direccion = ?, tipo_sangre = ?, alergias = ?, 
                    condiciones_medicas_preexistentes = ?, medicamentos_actuales = ?, 
                    nombre_contacto_emergencia = ?, telefono_emergencia = ?, relacion_paciente = ?
                WHERE numero_identificacion = ?
            """, (*nuevos_datos, dni))
            conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al actualizar paciente: {e}")
        finally:
            cerrar_conexion(conexion)
            
def eliminar_paciente_por_id(dni):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM Paciente WHERE numero_identificacion = ?", (dni,))
            conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al eliminar paciente: {e}")
        finally:
            cerrar_conexion(conexion)


# Eliminar un paciente
def eliminar_paciente(id_paciente):
    conexion, cursor = conectar()
    cursor.execute("DELETE FROM Paciente WHERE id_paciente = ?", (id_paciente,))
    conexion.commit()
    conexion.close()

def buscar_paciente_por_dni(dni):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Paciente WHERE numero_identificacion = ?", (dni,))
            resultado = cursor.fetchone()
            if resultado:
                # Convertir los datos en un diccionario para facilitar el uso
                campos = [
                    "nombre_completo", "fecha_nacimiento", "genero", "numero_identificacion", 
                    "telefono", "correo_electronico", "direccion", "tipo_sangre", 
                    "alergias", "condiciones_medicas_preexistentes", "medicamentos_actuales", 
                    "nombre_contacto_emergencia", "telefono_emergencia", "relacion_paciente"
                ]
                return dict(zip(campos, resultado))
            return None
        except sqlite3.Error as e:
            print(f"Error al buscar paciente: {e}")
            return None
        finally:
            cerrar_conexion(conexion)

