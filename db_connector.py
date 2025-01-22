import sqlite3
import os
import sys
from pathlib import Path
import shutil

def conectar():
    """Establece y devuelve una conexión a la base de datos SQLite."""
    # Directorio donde se ejecuta el programa empaquetado
    base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

    # Ruta de la base de datos en el directorio de usuario
    user_db_path = os.path.join(Path.home(), 'ConsultorioMedicoDB.db')

    # Si la base de datos no existe en el directorio del usuario, cópiala
    if not os.path.exists(user_db_path):
        original_db_path = os.path.join(base_dir, 'ConsultorioMedicoDB.db')
        shutil.copy(original_db_path, user_db_path)

    try:
        # Conectar a la base de datos en el directorio del usuario
        conexion = sqlite3.connect(user_db_path)
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def cerrar_conexion(conexion):
    """Cierra la conexión a la base de datos."""
    if conexion:
        conexion.close()
