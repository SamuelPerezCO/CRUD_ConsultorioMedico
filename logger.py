import logging
import os
from datetime import datetime

# Nombre del proyecto
PROJECT_NAME = "CRUD-ConsultorioDermatologico"

# Obtener la fecha actual
current_date = datetime.now()
month = current_date.strftime("%Y-%m")  # Carpeta del mes (formato: Año-Mes)
day = current_date.strftime("%d")  # Subcarpeta del día

# Crear las carpetas necesarias
log_directory = os.path.join("logs", month, day)
os.makedirs(log_directory, exist_ok=True)

# Archivo de log
log_file = os.path.join(log_directory, "app.log")

# Configuración del logger
logger = logging.getLogger(PROJECT_NAME)  # Agregar el nombre del proyecto al logger
logger.setLevel(logging.DEBUG)

# Formato para los mensajes
formatter = logging.Formatter(f'%(asctime)s - %(levelname)s - {PROJECT_NAME} - %(filename)s - %(message)s')

# Manejador para la consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# Manejador para el archivo
file_handler = logging.FileHandler(log_file, mode='w')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Agregar manejadores al logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


def cerrar_log():
    """Cierra la consola de comandos que muestra el log."""
    import os
    import sys
    if os.name == 'nt':  # Solo para Windows
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    elif os.name == 'posix':
        sys.stdout = open(os.devnull, 'w')  # Redirige stdout a null en sistemas Unix
    import logging
    logger = logging.getLogger()
    logger.info("Consola de comandos cerrada, pero el log sigue activo en archivos configurados.")
