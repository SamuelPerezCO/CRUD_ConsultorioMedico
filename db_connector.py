import sqlite3
import os
import sys

def conectar():
    """Establece y devuelve una conexión a la base de datos SQLite."""
    base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))  # Para PyInstaller
    db_path = os.path.join(base_dir, 'ConsultorioMedicoDB.db')

    try:
        conexion = sqlite3.connect(db_path)
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def cerrar_conexion(conexion):
    """Cierra la conexión a la base de datos."""
    if conexion:
        conexion.close()
