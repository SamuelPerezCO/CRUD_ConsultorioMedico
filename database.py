from db_connector import conectar, cerrar_conexion
import sqlite3

def agregar_historia_clinica(dni_paciente, registro):
    """
    Agrega un nuevo registro de historia clínica para un paciente dado su DNI.

    Args:
        dni_paciente (str): Número de identificación del paciente.
        registro (dict): Diccionario con los detalles del registro, incluyendo Fecha, Motivo, Diagnóstico y Tratamiento.

    Returns:
        None

    Raises:
        sqlite3.Error: Si ocurre un error al insertar el registro en la base de datos.
    """
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Historia_Clinica (numero_identificacion, fecha, motivo, diagnostico, tratamiento) 
            VALUES (?, ?, ?, ?, ?)
        """, (
            dni_paciente,
            registro.get("Fecha"),
            registro.get("Motivo"),
            registro.get("Diagnóstico"),
            registro.get("Tratamiento")
        ))
        conexion.commit()
        print("Registro de historia clínica agregado correctamente.")
    except sqlite3.Error as e:
        print(f"Error al agregar registro de historia clínica: {e}")
        raise
    finally:
        cerrar_conexion(conexion)


def obtener_historia_clinica(dni_paciente):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT fecha, motivo, diagnostico, tratamiento 
            FROM Historia_Clinica 
            WHERE numero_identificacion = ?
        """, (dni_paciente,))
        resultados = cursor.fetchall()
        return [
            {"Fecha": r[0], "Motivo": r[1], "Diagnóstico": r[2], "Tratamiento": r[3]} 
            for r in resultados
        ]
    finally:
        cerrar_conexion(conexion)


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
                    medicamentos_actuales, nombre_contacto_emergencia, telefono_emergencia, relacion_paciente
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, datos_paciente[:15])  # Ajustamos la longitud de los datos a 15 valores
            conexion.commit()
            print("Paciente agregado exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al agregar paciente: {e}")
        finally:
            cerrar_conexion(conexion)

# Asegúrate de que `datos_paciente` tenga solo 15 elementos al momento de llamarlo o ajusta el número en el código.


def buscar_paciente(id_paciente):
    conexion, cursor = conectar()
    cursor.execute("SELECT * FROM Paciente WHERE id_paciente = ?", (id_paciente,))
    paciente = cursor.fetchone()
    conexion.close()
    return paciente


# Actualizar información de un paciente
def actualizar_paciente(dni, nuevos_datos):
    print("Entre en actualizar_paciente")
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
    conexion = conectar()  # Función para conectar a la base de datos
    if conexion:
        try:
            cursor = conexion.cursor()
            # Asegúrate de que las columnas seleccionadas existen en la tabla
            cursor.execute("SELECT * FROM Paciente WHERE numero_identificacion = ?", (dni,))
            resultado = cursor.fetchone()

            if resultado:
                # Mapeo de las columnas según el orden en la base de datos
                campos = [
                    "nombre_completo", "fecha_nacimiento", "genero", "numero_identificacion", 
                    "telefono", "correo_electronico", "direccion", "tipo_sangre", 
                    "alergias", "condiciones_medicas_preexistentes", "medicamentos_actuales", 
                    "nombre_contacto_emergencia", "telefono_emergencia", "relacion_paciente"
                ]
                
                # Asegúrate de que el número de columnas coincida con los campos
                if len(campos) != len(resultado):
                    print("Error: Los campos del diccionario no coinciden con las columnas de la tabla.")
                    print(f"Datos retornados: {resultado}")
                    return None

                # Crear el diccionario mapeado
                return dict(zip(campos, resultado))

            # Si no se encuentra el paciente
            print(f"No se encontró el paciente con DNI: {dni}")
            return None
        except sqlite3.Error as e:
            print(f"Error al buscar paciente: {e}")
            return None
        finally:
            cerrar_conexion(conexion)


# Crear una nueva cita
def agregar_cita(datos_cita):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Cita (
                numero_identificacion, fecha_hora, motivo
            ) VALUES (?, ?, ?)
        """, datos_cita)
        conexion.commit()
        print("Cita agregada exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al agregar cita: {e}")
    finally:
        cerrar_conexion(conexion)

# Actualizar una cita existente
def actualizar_cita(id_cita, nuevos_datos):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Cita
            SET 
                numero_identificacion = ?, fecha_hora = ?, motivo = ?
            WHERE id_cita = ?
        """, (*nuevos_datos, id_cita))
        conexion.commit()
        print("Cita actualizada exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al actualizar cita: {e}")
    finally:
        cerrar_conexion(conexion)

# Eliminar una cita
def eliminar_cita(id_cita):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Cita WHERE id_cita = ?", (id_cita,))
        conexion.commit()
        print("Cita eliminada exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al eliminar cita: {e}")
    finally:
        cerrar_conexion(conexion)
        

def buscar_id_paciente_por_nombre(nombre):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT numero_identificacion 
            FROM Paciente 
            WHERE nombre_completo = ?
        """, (nombre,))
        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]  # Devuelve el número de identificación
        return None  # Si no encuentra resultados
    except sqlite3.Error as e:
        print(f"Error al buscar ID del paciente: {e}")
        return None
    finally:
        cerrar_conexion(conexion)


# Función para agregar una nueva cita
def agregar_cita(numero_identificacion, fecha_hora, motivo):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO Cita (numero_identificacion, fecha_hora, motivo)
                VALUES (?, ?, ?)
            """, (numero_identificacion, fecha_hora, motivo))
            conexion.commit()
        except sqlite3.Error as e:
            print(f"Error al agregar cita: {e}")
        finally:
            cerrar_conexion(conexion)

# Función para obtener todas las citas
def obtener_citas():
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT Cita.id_cita, Cita.fecha_hora, Paciente.nombre_completo, Cita.motivo
            FROM Cita
            LEFT JOIN Paciente ON Cita.numero_identificacion = Paciente.numero_identificacion
        """)
        resultados = cursor.fetchall()
        return [
            {
                "ID": r[0],
                "Hora": r[1],
                "Paciente": r[2] if r[2] else "Paciente no registrado",
                "Motivo": r[3]
            }
            for r in resultados
        ]
    except sqlite3.Error as e:
        print(f"Error al obtener citas: {e}")
        return []
    finally:
        cerrar_conexion(conexion)

# Función para obtener citas por número de identificación
def obtener_citas_por_paciente(numero_identificacion):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT fecha_hora, motivo 
                FROM Cita 
                WHERE numero_identificacion = ?
            """, (numero_identificacion,))
            resultados = cursor.fetchall()
            return resultados
        except sqlite3.Error as e:
            print(f"Error al obtener citas: {e}")
            return []
        finally:
            cerrar_conexion(conexion)


def obtener_numero_identificacion_por_cita(id_cita):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT numero_identificacion FROM Cita WHERE id_cita = ?", (id_cita,))
        resultado = cursor.fetchone()
        return resultado[0] if resultado else None
    finally:
        cerrar_conexion(conexion)
 