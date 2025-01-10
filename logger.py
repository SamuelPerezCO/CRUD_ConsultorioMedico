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
    """Cierra el log al iniciar la aplicación pero mantiene el registro activo."""
    import logging
    logger = logging.getLogger()
    for handler in logger.handlers:
        if isinstance(handler, logging.StreamHandler):
            logger.removeHandler(handler)
    logger.info("Log de ventana cerrado pero sigue registrando en archivos o configuraciones activas.")
