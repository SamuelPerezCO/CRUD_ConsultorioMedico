
from database import agregar_paciente, buscar_paciente_por_dni, actualizar_paciente, eliminar_paciente_por_id, obtener_pacientes, obtener_historia_clinica, agregar_historia_clinica , buscar_id_paciente_por_nombre
from database import agregar_cita , actualizar_cita , obtener_citas , buscar_paciente_por_dni,obtener_numero_identificacion_por_cita , eliminar_cita , obtener_citas_por_paciente
from logger import logger , cerrar_log
import customtkinter as ctk

logger.debug("INICIO")
cerrar_log()
# Configuración básica de la aplicación
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

pacientes = []

# Crear ventana principal
app = ctk.CTk()
app.title("Consultorio Médico")
app.geometry("1300x900")  # Tamaño inicial
app.minsize(1300, 900)  # Tamaño mínimo

# Configurar diseño de la ventana
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=4)

# Crear marco izquierdo para los botones
frame_izquierdo = ctk.CTkFrame(app)
frame_izquierdo.grid(row=0, column=0, sticky="nswe")
frame_izquierdo.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)  # Ajustar filas
frame_izquierdo.grid_columnconfigure(0, weight=1)

# Título en el marco izquierdo
titulo = ctk.CTkLabel(frame_izquierdo, text="Consultorio Dermatologico  \n Dra. Benilda Martel", font=("Arial", 16, "bold"))
titulo.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="n")

# Botones en el menú izquierdo (organizados ergonómicamente)
btn_crear = ctk.CTkButton(frame_izquierdo, text="Crear paciente", font=("Arial", 14),
                          width=170, height=50, corner_radius=15, command=lambda: mostrar_formulario())
btn_crear.grid(row=1, column=0, padx=10, pady=20, sticky="n")

btn_buscar = ctk.CTkButton(frame_izquierdo, text="Buscar paciente", font=("Arial", 14),
                           width=170, height=50, corner_radius=15, command=lambda: mostrar_buscar_paciente())
btn_buscar.grid(row=2, column=0, padx=10, pady=20, sticky="n")

btn_crear_cita = ctk.CTkButton(frame_izquierdo, text="Citas", font=("Arial", 14),
                               width=170, height=50, corner_radius=15, command=lambda: mostrar_citas())
btn_crear_cita.grid(row=3, column=0, padx=10, pady=20, sticky="n")

btn_listar_pacientes = ctk.CTkButton(frame_izquierdo, text="Listar Pacientes", font=("Arial", 14),
                                     width=170, height=50, corner_radius=15, command=lambda:listar_pacientes())
btn_listar_pacientes.grid(row=4, column=0, padx=10, pady=20, sticky="n")

frame_izquierdo.grid_rowconfigure(4, weight=2)  # Espacio adicional para balancear

# Marco para la sección derecha
frame_derecha = ctk.CTkFrame(app, fg_color="transparent")
frame_derecha.grid(row=0, column=1, sticky="nswe")
frame_derecha.grid_rowconfigure(0, weight=1)
frame_derecha.grid_columnconfigure(0, weight=1)

def listar_pacientes():
    """
    Genera una vista en la interfaz para listar todos los pacientes registrados.

    La función limpia el contenido actual del marco derecho y muestra una tabla
    con los datos de los pacientes obtenidos desde la base de datos. Incluye un
    botón para regresar al menú principal.

    Args:
        Ninguno

    Returns:
        None
    """
    logger.debug("Entre en listar pacientes")
    
    for widget in frame_derecha.winfo_children():
        widget.destroy()

    # Título de la vista
    titulo = ctk.CTkLabel(frame_derecha, text="Lista de Pacientes", font=("Arial", 20, "bold"))
    titulo.grid(row=0, column=0, pady=10, columnspan=2)

    # Marco desplazable para la tabla
    scroll_frame = ctk.CTkScrollableFrame(frame_derecha)
    scroll_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
    scroll_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

    # Encabezados de la tabla
    encabezados = ["Nombre", "DNI", "Teléfono", "Correo Electrónico"]
    for col_idx, encabezado in enumerate(encabezados):
        label_encabezado = ctk.CTkLabel(scroll_frame, text=f"{encabezado}", font=("Arial", 14, "bold"))
        label_encabezado.grid(row=0, column=col_idx, padx=10, pady=10)

    # Obtener datos desde la base de datos
    pacientes = obtener_pacientes()
    for row_idx, paciente in enumerate(pacientes, start=1):
        for col_idx, dato in enumerate([paciente[0], paciente[3], paciente[4], paciente[5]]):  # Seleccionamos campos necesarios
            label_dato = ctk.CTkLabel(scroll_frame, text=f"{dato}", font=("Arial", 12))
            label_dato.grid(row=row_idx, column=col_idx, padx=10, pady=5)

    # Botón para volver
    btn_volver = ctk.CTkButton(frame_derecha, text="Volver", command=mostrar_mensaje_inicial)
    btn_volver.grid(row=2, column=0, columnspan=2, pady=20)

def gestionar_historia_clinica(paciente):
    """
    Muestra la vista de la historia clínica de un paciente en la interfaz.

    Esta función permite visualizar los registros de historia clínica de un paciente
    y agregar nuevos registros. Además, ofrece opciones para navegar de vuelta al
    menú principal.

    Args:
        paciente (dict): Diccionario que contiene la información del paciente,
            incluyendo el nombre y el número de identificación.

    Returns:
        None
    """

    logger.debug(f"Entre en gestionar_historia_clinica y el paciente es {paciente}")

    for widget in frame_derecha.winfo_children():
        widget.destroy()

    # Validar si el diccionario 'paciente' contiene la clave esperada
    if 'Nombre Completo' not in paciente:
        logger.error("El diccionario del paciente no contiene la clave 'Nombre Completo'")
        mensaje_error = ctk.CTkLabel(frame_derecha, text="Error: Información del paciente incompleta.", font=("Arial", 14), fg_color="red")
        mensaje_error.grid(row=0, column=0, pady=20)
        return

    # Título principal
    titulo = ctk.CTkLabel(frame_derecha, text=f"Historia Clínica - {paciente['Nombre Completo']}", font=("Arial", 20, "bold"))
    titulo.grid(row=0, column=0, columnspan=2, pady=20)

    # Crear marco desplazable para la historia clínica
    scroll_frame = ctk.CTkScrollableFrame(frame_derecha)
    scroll_frame.grid(row=1, column=0, columnspan=2, sticky="nswe", padx=20, pady=10)
    scroll_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

    # Encabezados de la tabla
    encabezados = ["Fecha", "Historia Clinica", "Diagnóstico", "Tratamiento"]
    for idx, encabezado in enumerate(encabezados):
        label_encabezado = ctk.CTkLabel(scroll_frame, text=encabezado, font=("Arial", 14, "bold"))
        label_encabezado.grid(row=0, column=idx, padx=10, pady=10)

    # Obtener registros desde la base de datos
    registros = obtener_historia_clinica(paciente["numero_identificacion"])

    # Mostrar registros en la tabla
    for row_idx, registro in enumerate(registros, start=1):
        for col_idx, campo in enumerate(encabezados):
            valor = registro[campo]
            label = ctk.CTkLabel(scroll_frame, text=valor, font=("Arial", 12))
            label.grid(row=row_idx, column=col_idx, padx=10, pady=5)

    # Función para agregar un nuevo registro
    def agregar_registro():
        """
        Muestra un formulario para agregar un nuevo registro a la historia clínica.

        Args:
            None

        Returns:
            None
        """

        logger.debug("Entre en agregar_registro")

        for widget in frame_derecha.winfo_children():
            widget.destroy()

        # Título del formulario
        titulo_form = ctk.CTkLabel(frame_derecha, text=f"Agregar Registro - {paciente['Nombre Completo']}", font=("Arial", 20, "bold"))
        titulo_form.grid(row=0, column=0, columnspan=2, pady=20)

        # Campos para el nuevo registro
        campos_registro = ["Fecha (DD/MM/AAAA)", "Historia Clinica", "Diagnóstico", "Tratamiento"]
        entries = {}

        for idx, campo in enumerate(campos_registro[:-1]):  # Excluye "Tratamiento" del bucle
            label = ctk.CTkLabel(frame_derecha, text=campo + ":", font=("Arial", 14))
            label.grid(row=idx + 1, column=0, padx=20, pady=10, sticky="e")

            entry = ctk.CTkEntry(frame_derecha, font=("Arial", 14), width=300)
            entry.grid(row=idx + 1, column=1, padx=20, pady=10, sticky="w")
            entries[campo] = entry

        # Campo de texto para "Tratamiento"
        label_tratamiento = ctk.CTkLabel(frame_derecha, text="Tratamiento:", font=("Arial", 14))
        label_tratamiento.grid(row=len(campos_registro), column=0, padx=20, pady=10, sticky="e")

        text_tratamiento = ctk.CTkTextbox(frame_derecha, font=("Arial", 14), height=120, width=300, wrap="word")
        text_tratamiento.grid(row=len(campos_registro), column=1, padx=20, pady=10, sticky="w")

        # Función para guardar el registro en la base de datos
        def guardar_nuevo_registro():
            """
            Guarda un nuevo registro de historia clínica en la base de datos.

            Args:
                None

            Returns:
                None

            Raises:
                Exception: Si ocurre un error durante la inserción del registro.
            """

            logger.debug("Entre en guardar_nuevo_registro")

            nuevo_registro = {
                "Fecha": entries["Fecha (DD/MM/AAAA)"].get(),
                "Motivo": entries["Motivo"].get(),
                "Diagnóstico": entries["Diagnóstico"].get(),
                "Tratamiento": text_tratamiento.get("1.0", "end-1c")
            }

            try:
                agregar_historia_clinica(paciente["numero_identificacion"], nuevo_registro)
                gestionar_historia_clinica(paciente)  # Recargar la vista de historia clínica
            except Exception as e:
                mensaje_error = ctk.CTkLabel(frame_derecha, text=f"Error: {e}", font=("Arial", 14), fg_color="red")
                mensaje_error.grid(row=len(campos_registro) + 1, column=0, columnspan=2, pady=10)
                logger.error(f"Error en guardar_nuevo_registro {e}")

        # Botón para guardar el nuevo registro
        btn_guardar = ctk.CTkButton(frame_derecha, text="Guardar", font=("Arial", 14), command=guardar_nuevo_registro)
        btn_guardar.grid(row=len(campos_registro) + 1, column=0, columnspan=2, pady=20)

        # Botón para volver
        btn_volver = ctk.CTkButton(frame_derecha, text="Volver", font=("Arial", 14), command=lambda: gestionar_historia_clinica(paciente))
        btn_volver.grid(row=len(campos_registro) + 2, column=0, columnspan=2, pady=10)

    # Botón para agregar un nuevo registro
    btn_agregar = ctk.CTkButton(frame_derecha, text="Agregar Registro", font=("Arial", 14), command=agregar_registro)
    btn_agregar.grid(row=2, column=0, pady=20, padx=10)

    # Botón para volver al menú principal
    btn_volver = ctk.CTkButton(frame_derecha, text="Volver", font=("Arial", 14), command=mostrar_mensaje_inicial)
    btn_volver.grid(row=2, column=1, pady=20, padx=10)

def mostrar_historia_clinica(paciente):
    """
    Muestra la vista de la historia clínica de un paciente, incluyendo una tabla con los
    registros existentes y opciones para agregar nuevos registros.

    Args:
        paciente (dict): Diccionario que contiene la información del paciente y su historia clínica.

    Returns:
        None
    """

    logger.info(f"Entre en mostrar_historia_clinica con paciente {paciente}")
    for widget in frame_derecha.winfo_children():
        widget.destroy()

    # Encabezado principal
    titulo_historia = ctk.CTkLabel(frame_derecha, text=f"Historia Clínica - {paciente['Nombre Completo']}", font=("Arial", 20, "bold"))
    titulo_historia.grid(row=0, column=0, columnspan=2, pady=20)

    # Crear marco desplazable para la historia clínica
    scroll_frame = ctk.CTkScrollableFrame(frame_derecha)
    scroll_frame.grid(row=1, column=0, columnspan=2, sticky="nswe", padx=20, pady=10)
    scroll_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

    # Encabezados de la tabla
    encabezados = ["Fecha", "Historia Clinica", "Diagnóstico", "Tratamiento"]
    for idx, encabezado in enumerate(encabezados):
        label_encabezado = ctk.CTkLabel(scroll_frame, text=encabezado, font=("Arial", 14, "bold"))
        label_encabezado.grid(row=0, column=idx, padx=10, pady=10, sticky="nsew")

    # Datos simulados del historial clínico
    historia_clinica = paciente.get("Historia Clínica", [])

    # Filas de la tabla
    for row_idx, registro in enumerate(historia_clinica, start=1):
        for col_idx, campo in enumerate(encabezados):
            valor = registro.get(campo, "N/A")
            label = ctk.CTkLabel(scroll_frame, text=valor, font=("Arial", 12))
            label.grid(row=row_idx, column=col_idx, padx=10, pady=5, sticky="nsew")

    # Botón para agregar un nuevo registro
    def agregar_registro():
        """
        Muestra un formulario para agregar un nuevo registro a la historia clínica del paciente.

        Args:
            None

        Returns:
            None
        """

        logger.debug("Entre en agregar_registro")

        for widget in frame_derecha.winfo_children():
            widget.destroy()

        # Título del formulario
        titulo_form = ctk.CTkLabel(frame_derecha, text=f"Agregar Registro - {paciente['Nombre Completo']}", font=("Arial", 22, "bold"))
        titulo_form.grid(row=0, column=0, columnspan=2, pady=20)

        # Campos del formulario
        campos_registro = ["Fecha (DD/MM/AAAA)", "Historia Clinica", "Diagnóstico"]
        entries = {}

        for idx, campo in enumerate(campos_registro):
            label = ctk.CTkLabel(frame_derecha, text=campo + ":", anchor="w", font=("Arial", 16))
            label.grid(row=idx + 1, column=0, sticky="e", padx=20, pady=10)

            entry = ctk.CTkEntry(frame_derecha, font=("Arial", 14), width=300)
            entry.grid(row=idx + 1, column=1, sticky="w", padx=20, pady=10)
            entries[campo] = entry

        # Área de texto para "Tratamiento"
        label_tratamiento = ctk.CTkLabel(frame_derecha, text="Tratamiento:", anchor="w", font=("Arial", 16))
        label_tratamiento.grid(row=len(campos_registro) + 1, column=0, sticky="ne", padx=20, pady=10)

        text_tratamiento = ctk.CTkTextbox(frame_derecha, font=("Arial", 14), height=120, width=300, wrap="word")
        text_tratamiento.grid(row=len(campos_registro) + 1, column=1, sticky="w", padx=20, pady=10)

        # Guardar el registro en el historial
        def guardar_registro():
            """
            Guarda un nuevo registro en la historia clínica del paciente.

            Args:
                None

            Returns:
                None
            """

            logger.debug("Entre en guardar_registro")

            nuevo_registro = {campo: entrada.get() for campo, entrada in entries.items()}
            nuevo_registro["Tratamiento"] = text_tratamiento.get("1.0", "end-1c")  # Obtener texto completo del área
            if "Historia Clínica" not in paciente:
                paciente["Historia Clínica"] = []
            paciente["Historia Clínica"].append(nuevo_registro)
            mostrar_historia_clinica(paciente)

        # Botón para guardar
        btn_guardar = ctk.CTkButton(frame_derecha, text="Guardar Registro", font=("Arial", 14), command=guardar_registro)
        btn_guardar.grid(row=len(campos_registro) + 2, column=0, columnspan=2, pady=20)

        # Botón para volver a la historia clínica
        btn_volver = ctk.CTkButton(frame_derecha, text="Volver", font=("Arial", 14), command=lambda: mostrar_historia_clinica(paciente))
        btn_volver.grid(row=len(campos_registro) + 3, column=0, columnspan=2, pady=10)

    # Botón para agregar registro
    btn_agregar = ctk.CTkButton(frame_derecha, text="Agregar Registro", command=agregar_registro)
    btn_agregar.grid(row=2, column=0, pady=20, padx=20, sticky="w")

    # Botón para volver al menú principal
    btn_volver = ctk.CTkButton(frame_derecha, text="Volver", command=mostrar_mensaje_inicial)
    btn_volver.grid(row=2, column=1, pady=20, padx=20, sticky="e")

def mostrar_mensaje_inicial():
    """
    Muestra el mensaje inicial en la interfaz con las citas filtradas según la selección del usuario.

    Esta función limpia el contenido del marco derecho y muestra una tabla con las
    citas obtenidas desde la base de datos, incluyendo su ID, hora, paciente y motivo.

    Además, permite al usuario alternar entre ver todas las citas y las citas seleccionadas.

    Args:
        None

    Returns:
        None
    """
    global mostrar_todas_citas  # Controla si se muestran todas las citas o solo las seleccionadas
    if 'mostrar_todas_citas' not in globals():
        mostrar_todas_citas = True

    # Lista global de citas seleccionadas
    global citas_seleccionadas
    if 'citas_seleccionadas' not in globals():
        citas_seleccionadas = []

    for widget in frame_derecha.winfo_children():
        widget.destroy()

    frame_derecha.grid_rowconfigure(0, weight=0)
    frame_derecha.grid_rowconfigure(1, weight=1)
    frame_derecha.grid_columnconfigure(0, weight=1)

    # Encabezado principal
    titulo_citas = ctk.CTkLabel(frame_derecha, text="Citas", font=("Arial", 20, "bold"))
    titulo_citas.grid(row=0, column=0, pady=(10, 20))

    # Botón para alternar entre todas las citas y citas seleccionadas
    def alternar_vista():
        global mostrar_todas_citas
        mostrar_todas_citas = not mostrar_todas_citas
        mostrar_mensaje_inicial()

    btn_alternar = ctk.CTkButton(
        frame_derecha, 
        text="Ver Todas" if not mostrar_todas_citas else "Ver Seleccionadas",
        command=alternar_vista
    )
    btn_alternar.grid(row=0, column=1, pady=(10, 20), padx=10, sticky="e")

    # Crear marco desplazable para la tabla
    scroll_frame = ctk.CTkScrollableFrame(frame_derecha)
    scroll_frame.grid(row=1, column=0, columnspan=2, sticky="nswe", padx=20, pady=10)
    scroll_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

    # Encabezados de la tabla
    encabezados = ["ID", "Hora", "Paciente", "Historia Clinica"]
    for idx, encabezado in enumerate(encabezados):
        label_encabezado = ctk.CTkLabel(scroll_frame, text=encabezado, font=("Arial", 14, "bold"))
        label_encabezado.grid(row=0, column=idx, padx=10, pady=10, sticky="nsew")

    # Obtener citas desde la base de datos
    citas = obtener_citas()

    if not mostrar_todas_citas:
        citas = [cita for cita in citas if cita["ID"] in citas_seleccionadas]

    # Filas de la tabla
    for row_idx, cita in enumerate(citas, start=1):
        # ID de la cita
        label_id = ctk.CTkLabel(scroll_frame, text=cita["ID"], font=("Arial", 12))
        label_id.grid(row=row_idx, column=0, padx=10, pady=5, sticky="nsew")

        # Fecha y hora
        label_hora = ctk.CTkLabel(scroll_frame, text=cita["Hora"], font=("Arial", 12))
        label_hora.grid(row=row_idx, column=1, padx=10, pady=5, sticky="nsew")

        # Nombre del paciente
        label_paciente = ctk.CTkLabel(scroll_frame, text=cita["Paciente"], font=("Arial", 12))
        label_paciente.grid(row=row_idx, column=2, padx=10, pady=5, sticky="nsew")

        # Motivo
        label_motivo = ctk.CTkLabel(scroll_frame, text=cita["Motivo"], font=("Arial", 12))
        label_motivo.grid(row=row_idx, column=3, padx=10, pady=5, sticky="nsew")

        # Checkbox para marcar como seleccionada
        def toggle_seleccion(cita=cita):
            if cita["ID"] in citas_seleccionadas:
                citas_seleccionadas.remove(cita["ID"])
            else:
                citas_seleccionadas.append(cita["ID"])

        check_var = ctk.BooleanVar(value=cita["ID"] in citas_seleccionadas)
        check_btn = ctk.CTkCheckBox(scroll_frame, variable=check_var, command=toggle_seleccion , text="Seleccionar")
        check_btn.grid(row=row_idx, column=4, padx=10, pady=5, sticky="nsew")



# Ajusta el encabezado y las columnas para incluir "ID" en la vista de citas.
mostrar_mensaje_inicial()

def mostrar_crear_cita():
    global pacientes

    for widget in frame_derecha.winfo_children():
        widget.destroy()

    frame_derecha.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
    frame_derecha.grid_columnconfigure((0, 1), weight=1)

    titulo_form = ctk.CTkLabel(frame_derecha, text="Crear Cita", font=("Arial", 20, "bold"))
    titulo_form.grid(row=0, column=0, columnspan=2, pady=20)

    label_dni = ctk.CTkLabel(frame_derecha, text="DNI del Paciente:", font=("Arial", 14), anchor="w")
    label_dni.grid(row=1, column=0, padx=20, pady=10, sticky="e")

    entry_dni = ctk.CTkEntry(frame_derecha)
    entry_dni.grid(row=1, column=1, padx=20, pady=10, sticky="w")

    label_nombre = ctk.CTkLabel(frame_derecha, text="Paciente:", font=("Arial", 14), anchor="w")
    label_nombre.grid(row=2, column=0, padx=20, pady=10, sticky="e")

    entry_nombre = ctk.CTkEntry(frame_derecha, state="disabled")
    entry_nombre.grid(row=2, column=1, padx=20, pady=10, sticky="w")

    def buscar_paciente_dni():
        dni = entry_dni.get().strip()
        if not dni:
            mensaje_error = ctk.CTkLabel(frame_derecha, text="Por favor, ingrese un DNI válido.", font=("Arial", 14), fg_color="red")
            mensaje_error.grid(row=5, column=0, columnspan=2, pady=10)
            return

        paciente = buscar_paciente_por_dni(dni)
        if paciente:
            entry_nombre.configure(state="normal")
            entry_nombre.delete(0, "end")
            entry_nombre.insert(0, paciente["nombre_completo"])
            entry_nombre.configure(state="disabled")
        else:
            mensaje_error = ctk.CTkLabel(frame_derecha, text="Paciente no encontrado.", font=("Arial", 14), fg_color="red")
            mensaje_error.grid(row=5, column=0, columnspan=2, pady=10)

    btn_buscar = ctk.CTkButton(frame_derecha, text="Buscar", font=("Arial", 14), command=buscar_paciente_dni)
    btn_buscar.grid(row=1, column=2, padx=10, pady=10)

    label_fecha_hora = ctk.CTkLabel(frame_derecha, text="Fecha y Hora (YYYY-MM-DD HH:MM):", font=("Arial", 14), anchor="w")
    label_fecha_hora.grid(row=3, column=0, padx=20, pady=10, sticky="e")

    entry_fecha_hora = ctk.CTkEntry(frame_derecha)
    entry_fecha_hora.grid(row=3, column=1, padx=20, pady=10, sticky="w")

    label_historial = ctk.CTkLabel(frame_derecha, text="Historial Clínico:", font=("Arial", 14), anchor="w")
    label_historial.grid(row=4, column=0, padx=20, pady=10, sticky="ne")

    text_historial = ctk.CTkTextbox(frame_derecha, font=("Arial", 14), height=300, width=600, wrap="word")
    text_historial.grid(row=4, column=1, padx=20, pady=10, sticky="w")

    def guardar_cita():
        dni = entry_dni.get().strip()
        fecha_hora = entry_fecha_hora.get().strip()
        historial = text_historial.get("1.0", "end-1c").strip()

        if not dni or not fecha_hora or not historial:
            mensaje_error = ctk.CTkLabel(frame_derecha, text="Por favor, complete todos los campos.", font=("Arial", 14), fg_color="red")
            mensaje_error.grid(row=6, column=0, columnspan=2, pady=10)
            return

        try:
            agregar_cita(dni, fecha_hora, historial)
            mostrar_mensaje_inicial()
        except Exception as e:
            mensaje_error = ctk.CTkLabel(frame_derecha, text=f"Error: {e}", font=("Arial", 14), fg_color="red")
            mensaje_error.grid(row=6, column=0, columnspan=2, pady=10)

    btn_guardar = ctk.CTkButton(frame_derecha, text="Guardar Cita", font=("Arial", 14), command=guardar_cita)
    btn_guardar.grid(row=5, column=1, pady=20)

    btn_volver = ctk.CTkButton(frame_derecha, text="Volver", font=("Arial", 14), command=mostrar_mensaje_inicial)
    btn_volver.grid(row=6, column=1, pady=10)


# Función para mostrar el formulario de búsqueda (centrado)
def mostrar_buscar_paciente():
    """
    Muestra el formulario para buscar un paciente por su número de identificación (DNI).

    Este formulario permite al usuario ingresar un número de identificación y buscar
    al paciente correspondiente en la base de datos. Si el paciente es encontrado,
    se muestra su información; de lo contrario, se muestra un mensaje de error.

    Args:
        None

    Returns:
        None
    """

    logger.debug("Entre en mostrar_buscar_paciente")

    for widget in frame_derecha.winfo_children():
        widget.destroy()

    # Configurar el diseño
    frame_derecha.grid_rowconfigure((0, 1, 2, 3), weight=1)
    frame_derecha.grid_columnconfigure((0, 1), weight=1)

    # Título de búsqueda
    titulo_busqueda = ctk.CTkLabel(frame_derecha, text="Buscar Paciente", font=("Arial", 20, "bold"))
    titulo_busqueda.grid(row=0, column=0, columnspan=2, pady=20)

    # Campo de texto para el DNI
    label_dni = ctk.CTkLabel(frame_derecha, text="Número de Identificación (DNI):", font=("Arial", 14))
    label_dni.grid(row=1, column=0, padx=20, pady=10, sticky="e")

    entry_dni = ctk.CTkEntry(frame_derecha)
    entry_dni.grid(row=1, column=1, padx=20, pady=10, sticky="w")

    def buscar_paciente():
        """
        Busca un paciente en la base de datos por su número de identificación.

        Verifica que el campo de entrada no esté vacío. Si el paciente es encontrado,
        se llama a la función para mostrar su información. Si no, se muestra un mensaje
        de error indicando que no se encontró.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """

        logger.debug("Entre en buscar paciente")

        dni = entry_dni.get().strip()
        if not dni:
            mensaje_error = ctk.CTkLabel(frame_derecha, text="Por favor, ingrese un número de identificación válido.", font=("Arial", 14), fg_color="red")
            mensaje_error.grid(row=3, column=0, columnspan=2, pady=10)
            logger.error("Ingreso un numero de identificacion no valido")
            return
        
        # Buscar el paciente en la base de datos
        resultado = buscar_paciente_por_dni(dni)
        if resultado:
            mostrar_informacion_paciente(resultado)
        else:
            mensaje_error = ctk.CTkLabel(frame_derecha, text="Paciente no encontrado.", font=("Arial", 14), fg_color="red")
            mensaje_error.grid(row=3, column=0, columnspan=2, pady=10)
            logger.error("Paciente no encontrado")

    # Botón para buscar al paciente
    btn_buscar = ctk.CTkButton(frame_derecha, text="Buscar", font=("Arial", 14), command=buscar_paciente)
    btn_buscar.grid(row=2, column=0, columnspan=2, pady=20)

def actualizar_citas():
    """
    Actualiza la lista de citas global y la interfaz gráfica para reflejar los cambios.

    Esta función limpia la lista global de citas, la actualiza con datos
    obtenidos desde la base de datos y convierte estos datos a un formato
    adecuado para su visualización en la interfaz gráfica.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """

    logger.debug("entre en actualizar_citas")

    global citas  # Aseguramos que estamos trabajando con la lista global `citas`

    # Limpiar la lista actual
    citas.clear()

    # Obtener las citas desde la base de datos
    citas_db = obtener_citas()

    # Convertir las citas en un formato legible para la interfaz gráfica
    for cita in citas_db:
        citas.append({
            "Hora": cita[2],  # Suponiendo que la hora está en la posición 2 de la tupla
            "Paciente": buscar_paciente_por_dni(cita[1]),  # Convertir ID en nombre
            "Motivo": cita[3],  # Suponiendo que el motivo está en la posición 3
        })

    # Recargar la tabla gráfica
    mostrar_mensaje_inicial()

# Función para mostrar la información del paciente
# Declaración global para pacientes_var
pacientes_var = ctk.StringVar(value="Seleccionar paciente")

def mostrar_informacion_paciente(paciente, editable=False):
    """
    Muestra la información de un paciente, incluyendo la posibilidad de editar, eliminar, y realizar otras acciones.

    Args:
        paciente (dict): Diccionario con los datos del paciente.
        editable (bool): Indica si la información del paciente puede ser editada. Por defecto es False.

    Returns:
        None
    """

    logger.debug("Entre en mostrar_informacion_paciente")

    for widget in frame_derecha.winfo_children():
        widget.destroy()

    # Título
    titulo_info = ctk.CTkLabel(frame_derecha, text="Información del Paciente", font=("Arial", 20, "bold"))
    titulo_info.grid(row=0, column=0, columnspan=2, pady=20)

    # Mostrar todos los campos del paciente
    campos = {
        "Nombre Completo": paciente["nombre_completo"],
        "Fecha de Nacimiento": paciente["fecha_nacimiento"],
        "Género": paciente["genero"],
        "Número de Identificación": paciente["numero_identificacion"],
        "Teléfono": paciente["telefono"],
        "Correo Electrónico": paciente["correo_electronico"],
        "Dirección": paciente["direccion"],
        "Tipo de Sangre": paciente["tipo_sangre"],
        "Alergias": paciente["alergias"],
        "Condiciones Médicas Preexistentes": paciente["condiciones_medicas_preexistentes"],
        "Medicamentos Actuales": paciente["medicamentos_actuales"],
        "Nombre Contacto de Emergencia": paciente["nombre_contacto_emergencia"],
        "Teléfono de Emergencia": paciente["telefono_emergencia"],
        "Relación con el Paciente": paciente["relacion_paciente"],
        # "Historia Clínica": paciente["historia_clinica"]
    }

    labels = {}
    entries = {}

    for idx, (campo, valor) in enumerate(campos.items()):
        label_campo = ctk.CTkLabel(frame_derecha, text=f"{campo}:", font=("Arial", 14, "bold"), anchor="w")
        label_campo.grid(row=idx + 1, column=0, sticky="w", padx=20, pady=10)  # Aumentar padding vertical

        label_valor = ctk.CTkLabel(frame_derecha, text=valor if valor else "N/A", font=("Arial", 14), anchor="w")
        label_valor.grid(row=idx + 1, column=1, sticky="w", padx=20, pady=10)
        labels[campo] = label_valor

    def habilitar_edicion(paciente):
        """
        Habilita la edición de los datos del paciente.

        Args:
            paciente (dict): Diccionario con los datos del paciente.

        Returns:
            None
        """

        logger.debug(f"Entre en habilitar edicion con el paciente {paciente}")

        for widget in labels.values():
            widget.grid_forget()

        # Crear entradas en lugar de etiquetas
        for idx, (campo, valor) in enumerate(campos.items()):
            if campo == "Historia Clínica":
                entry = ctk.CTkTextbox(frame_derecha, font=("Arial", 14), height=200, wrap="word")
                entry.insert("1.0", valor)
            else:
                entry = ctk.CTkEntry(frame_derecha, font=("Arial", 14))
                entry.insert(0, valor)  # Mostrar el valor actual

            entry.grid(row=idx, column=1, sticky="w", padx=20, pady=5)
            entries[campo] = entry

        # Ocultar el botón de editar y agregar el de guardar
        btn_editar.grid_forget()
        btn_guardar = ctk.CTkButton(frame_derecha, text="Guardar Cambios", command=lambda: guardar_cambios(paciente))
        btn_guardar.grid(row=len(campos) + 1, column=0, columnspan=2, pady=10)

    def guardar_cambios(paciente):
        """
        Guarda los cambios editados del paciente en la base de datos.

        Args:
            paciente (dict): Diccionario con los datos del paciente.

        Returns:
            None
        """

        logger.debug(f"Entre en guardar_cambios con el paciente {paciente}")

        nuevos_datos = {campo: entry.get("1.0", "end-1c") if isinstance(entry, ctk.CTkTextbox) else entry.get() for campo, entry in entries.items()}  # Extraer datos de las entradas

        try:
            # Actualizar la base de datos
            actualizar_paciente(paciente["numero_identificacion"], list(nuevos_datos.values()))

            # Mostrar mensaje de éxito
            mensaje = ctk.CTkLabel(frame_derecha, text="Cambios guardados exitosamente.", font=("Arial", 14), fg_color="green")
            mensaje.grid(row=len(campos) + 2, column=0, columnspan=2, pady=10)

            # Recargar el paciente desde la base de datos
            paciente_actualizado = buscar_paciente_por_dni(paciente["numero_identificacion"])
            if paciente_actualizado:
                mostrar_informacion_paciente(paciente_actualizado, editable=True)
            else:
                print("Error: No se pudo obtener el paciente actualizado.")
                logger.error("No se pudo obtener el paciente actualizado")

        except Exception as e:
            mensaje = ctk.CTkLabel(frame_derecha, text=f"Error al guardar cambios: {str(e)}", font=("Arial", 14), fg_color="red")
            mensaje.grid(row=len(campos) + 2, column=0, columnspan=2, pady=10)
            logger.error(f"Error en guardar_cambios:{e}")

    def eliminar_paciente(paciente):
        """
        Elimina al paciente de la base de datos.

        Args:
            paciente (dict): Diccionario con los datos del paciente.

        Returns:
            None
        """
        logger.debug("Entre en eliminar paciente")

        try:
            confirmar = ctk.CTkLabel(frame_derecha, text="¿Está seguro de eliminar este paciente?", font=("Arial", 14), fg_color="yellow")
            confirmar.grid(row=len(campos) + 2, column=0, columnspan=2, pady=10)

            def confirmar_eliminacion():
                logger.info("Entre en confirmar_eliminacion")

                eliminar_paciente_por_id(paciente["numero_identificacion"])
                mostrar_buscar_paciente()

            btn_confirmar = ctk.CTkButton(frame_derecha, text="Sí, eliminar", command=confirmar_eliminacion)
            btn_confirmar.grid(row=len(campos) + 3, column=0, pady=10)

            btn_cancelar = ctk.CTkButton(frame_derecha, text="Cancelar", command=lambda: mostrar_informacion_paciente(paciente, editable=True))
            btn_cancelar.grid(row=len(campos) + 3, column=1, pady=10)
        except Exception as e:
            mensaje = ctk.CTkLabel(frame_derecha, text=f"Error al eliminar paciente: {str(e)}", font=("Arial", 14), fg_color="red")
            mensaje.grid(row=len(campos) + 2, column=0, columnspan=2, pady=10)
        logger.error(f"Error al eliminar paciente {paciente}")


    # Botones de acción
    botones_frame = ctk.CTkFrame(frame_derecha)
    botones_frame.grid(row=len(campos) + 2, column=0, columnspan=2, pady=20, padx=20)

    btn_editar = ctk.CTkButton(botones_frame, text="Editar Información", command=lambda: habilitar_edicion(paciente))
    btn_editar.grid(row=0, column=0, padx=10)

    btn_crear_cita = ctk.CTkButton(botones_frame, text="Crear Cita", command=lambda: mostrar_crear_cita())
    btn_crear_cita.grid(row=0, column=1, padx=10)

    btn_eliminar = ctk.CTkButton(botones_frame, text="Eliminar Paciente", command=lambda: eliminar_paciente(paciente))
    btn_eliminar.grid(row=0, column=2, padx=10)

    btn_volver = ctk.CTkButton(botones_frame, text="Volver", command=mostrar_mensaje_inicial)
    btn_volver.grid(row=0, column=3, padx=10)


# Función para mostrar el formulario de crear paciente (sin cambios)
def mostrar_formulario():
    """
    Muestra el formulario para crear un nuevo paciente, permitiendo ingresar todos los datos necesarios.

    El formulario incluye campos para información básica del paciente como nombre, fecha de nacimiento,
    género, contacto de emergencia, entre otros. Una vez completados los datos, el usuario puede guardar
    al paciente en la base de datos.

    Args:
        None

    Returns:
        None
    """

    logger.debug("Entre en mostrar_crear_paciente")

    for widget in frame_derecha.winfo_children():
        widget.destroy()

    titulo_form = ctk.CTkLabel(frame_derecha, text="Crear Paciente", font=("Arial", 20, "bold"))
    titulo_form.grid(row=0, column=0, columnspan=2, pady=10)

    campos = [
        "Nombre Completo",
        "Fecha de Nacimiento (DD/MM/AAAA)",
        "Género",
        "DNI",
        "Teléfono",
        "Correo Electrónico",
        "Dirección",
        "Tipo de Sangre",
        "Alergias",
        "Condiciones Médicas Preexistentes",
        "Medicamentos Actuales",
        "Nombre Contacto de Emergencia",
        "Teléfono de Emergencia",
        "Relación con el Paciente"
    ]

    entries = {}
    for idx, campo in enumerate(campos):
        label = ctk.CTkLabel(frame_derecha, text=campo + ":", anchor="w")
        label.grid(row=idx + 1, column=0, pady=5, sticky="w", padx=10)

        if campo == "Género":
            genero_var = ctk.StringVar(value="Masculino")
            opciones_genero = ["Masculino", "Femenino", "Otro"]
            genero_menu = ctk.CTkOptionMenu(frame_derecha, values=opciones_genero, variable=genero_var)
            genero_menu.grid(row=idx + 1, column=1, pady=5, padx=10, sticky="ew")
            entries[campo] = genero_var
        elif campo == "Tipo de Sangre":
            sangre_var = ctk.StringVar(value="O+")
            opciones_sangre = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
            sangre_menu = ctk.CTkOptionMenu(frame_derecha, values=opciones_sangre, variable=sangre_var)
            sangre_menu.grid(row=idx + 1, column=1, pady=5, padx=10, sticky="ew")
            entries[campo] = sangre_var
        else:
            entry = ctk.CTkEntry(frame_derecha)
            entry.grid(row=idx + 1, column=1, pady=5, padx=10, sticky="ew")
            entries[campo] = entry

    def guardar_paciente():
        """
        Guarda los datos ingresados en el formulario en la base de datos y muestra la información del paciente.
        """
        logger.debug("Entre en guardar_paciente")

        # Iterar sobre las entradas y obtener sus valores
        datos_paciente = []
        for campo, entrada in entries.items():
            if isinstance(entrada, ctk.StringVar):  # Caso de OptionMenu
                datos_paciente.append(entrada.get())
            else:  # Caso de CTkEntry
                datos_paciente.append(entrada.get())

        try:
            agregar_paciente(datos_paciente)  # Guardar en la base de datos

            # Actualizar la lista de pacientes
            global pacientes
            pacientes = [{"DNI": row[3], "Nombre Completo": row[0], "Teléfono": row[4], "Correo Electrónico": row[5]} for row in obtener_pacientes()]

            # Buscar el paciente recién agregado
            nuevo_paciente = {
                "nombre_completo": datos_paciente[0],
                "fecha_nacimiento": datos_paciente[1],
                "genero": datos_paciente[2],
                "numero_identificacion": datos_paciente[3],
                "telefono": datos_paciente[4],
                "correo_electronico": datos_paciente[5],
                "direccion": datos_paciente[6],
                "tipo_sangre": datos_paciente[7],
                "alergias": datos_paciente[8],
                "condiciones_medicas_preexistentes": datos_paciente[9],
                "medicamentos_actuales": datos_paciente[10],
                "nombre_contacto_emergencia": datos_paciente[11],
                "telefono_emergencia": datos_paciente[12],
                "relacion_paciente": datos_paciente[13]
            }

            # Mostrar la información del paciente recién creado
            mostrar_informacion_paciente(nuevo_paciente)

        except Exception as e:
            mensaje = ctk.CTkLabel(frame_derecha, text=f"Error: {str(e)}", font=("Arial", 14), fg_color="red")
            mensaje.grid(row=len(campos) + 2, column=0, columnspan=2, pady=10)
            logger.error(f"Error en guardar_paciente: {e}")


    btn_guardar = ctk.CTkButton(frame_derecha, text="Guardar", command=guardar_paciente)
    btn_guardar.grid(row=len(campos) + 1, column=0, columnspan=2, pady=20)

    frame_derecha.grid_columnconfigure(1, weight=1)

def obtener_dni_paciente(nombre):
    """
    Obtiene el DNI de un paciente dado su nombre.

    Args:
        nombre (str): Nombre completo del paciente.

    Returns:
        str: DNI del paciente si se encuentra.
        None: Si no se encuentra el DNI del paciente.

    Raises:
        None
    """

    logger.debug(f"Entre en obtener_dni_paciente {nombre}")

    dni = buscar_id_paciente_por_nombre(nombre)
    if not dni:
        print(f"No se encontró el DNI para el paciente: {nombre}")
    return dni

def mostrar_citas():
    """
    Muestra la interfaz de gestión de citas, permitiendo crear, actualizar o eliminar citas.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """

    logger.debug("Entre en mostrar_citas")

    for widget in frame_derecha.winfo_children():
        widget.destroy()

    frame_derecha.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
    frame_derecha.grid_columnconfigure((0, 1), weight=1)

    titulo_citas = ctk.CTkLabel(frame_derecha, text="Gestión de Citas", font=("Arial", 20, "bold"))
    titulo_citas.grid(row=0, column=0, columnspan=2, pady=20)

    def crear_cita():
        """
        Navega a la interfaz para crear una nueva cita.

        Args:
            None

        Returns:
            None
        """
        logger.debug("Entre en crear_cita")

        mostrar_crear_cita()

    def formulario_actualizar_cita():
        """
        Muestra el formulario para actualizar una cita existente.

        Args:
            None

        Returns:
            None
        """

        logger.debug("Entre en formulario_actualizar_cita")

        for widget in frame_derecha.winfo_children():
            widget.destroy()

        titulo_actualizar = ctk.CTkLabel(frame_derecha, text="Actualizar Cita", font=("Arial", 20, "bold"))
        titulo_actualizar.grid(row=0, column=0, columnspan=2, pady=20)

        label_id_cita = ctk.CTkLabel(frame_derecha, text="ID de la Cita:", font=("Arial", 14))
        label_id_cita.grid(row=1, column=0, padx=20, pady=10, sticky="e")

        entry_id_cita = ctk.CTkEntry(frame_derecha)
        entry_id_cita.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        label_nueva_fecha = ctk.CTkLabel(frame_derecha, text="Nueva Fecha y Hora (YYYY-MM-DD HH:MM):", font=("Arial", 14))
        label_nueva_fecha.grid(row=2, column=0, padx=20, pady=10, sticky="e")

        entry_nueva_fecha = ctk.CTkEntry(frame_derecha)
        entry_nueva_fecha.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        label_historia_clinica = ctk.CTkLabel(frame_derecha, text="Historia Clínica:", font=("Arial", 14))
        label_historia_clinica.grid(row=3, column=0, padx=20, pady=10, sticky="e")

        text_historia_clinica = ctk.CTkTextbox(frame_derecha, font=("Arial", 14), height=200, width=500, wrap="word")
        text_historia_clinica.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        def guardar_actualizacion():
            """
            Guarda los cambios realizados en una cita existente en la base de datos.

            Args:
                None

            Returns:
                None

            Raises:
                ValueError: Si no se encuentra el número de identificación para la cita.
            """

            logger.debug("Entre en guardar_actualizacion")

            id_cita = entry_id_cita.get().strip()
            nueva_fecha = entry_nueva_fecha.get().strip()
            nueva_historia = text_historia_clinica.get("1.0", "end-1c").strip()

            if not id_cita or not nueva_fecha or not nueva_historia:
                mensaje_error = ctk.CTkLabel(frame_derecha, text="Por favor, complete todos los campos.", font=("Arial", 14), fg_color="red")
                mensaje_error.grid(row=5, column=0, columnspan=2, pady=10)
                return

            try:
                numero_identificacion = obtener_numero_identificacion_por_cita(id_cita)
                if not numero_identificacion:
                    raise ValueError("No se encontró el número de identificación para la cita.")

                actualizar_cita(id_cita, [numero_identificacion, nueva_fecha, nueva_historia])
                mostrar_citas()
            except Exception as e:
                mensaje_error = ctk.CTkLabel(frame_derecha, text=f"Error: {e}", font=("Arial", 14), fg_color="red")
                mensaje_error.grid(row=5, column=0, columnspan=2, pady=10)
                logger.error(f"Error en guardar_actualizacion {e}")

        btn_guardar = ctk.CTkButton(frame_derecha, text="Guardar Cambios", command=guardar_actualizacion)
        btn_guardar.grid(row=4, column=0, columnspan=2, pady=20)


    def eliminar_cita_button():
        """
        Muestra el formulario para eliminar una cita existente.

        Args:
            None

        Returns:
            None
        """

        logger.debug("Entre en eliminar_cita_button")

        for widget in frame_derecha.winfo_children():
            widget.destroy()

        titulo_eliminar = ctk.CTkLabel(frame_derecha, text="Eliminar Cita", font=("Arial", 20, "bold"))
        titulo_eliminar.grid(row=0, column=0, columnspan=2, pady=20)

        label_id_cita = ctk.CTkLabel(frame_derecha, text="ID de la Cita:", font=("Arial", 14))
        label_id_cita.grid(row=1, column=0, padx=20, pady=10, sticky="e")

        entry_id_cita = ctk.CTkEntry(frame_derecha)
        entry_id_cita.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        def confirmar_eliminacion():
            """
            Elimina una cita de la base de datos según su ID.

            Args:
                None

            Returns:
                None

            Raises:
                None
            """
            id_cita = entry_id_cita.get().strip()

            if not id_cita:
                mensaje_error = ctk.CTkLabel(frame_derecha, text="Por favor, ingrese un ID de cita.", font=("Arial", 14), fg_color="red")
                mensaje_error.grid(row=3, column=0, columnspan=2, pady=10)
                return

            try:
                eliminar_cita(id_cita)
                mostrar_citas()
            except Exception as e:
                mensaje_error = ctk.CTkLabel(frame_derecha, text=f"Error: {e}", font=("Arial", 14), fg_color="red")
                mensaje_error.grid(row=3, column=0, columnspan=2, pady=10)
                logger.error(f"Error en confirmar_eliminacion {e}")

        btn_eliminar = ctk.CTkButton(frame_derecha, text="Eliminar", command=confirmar_eliminacion)
        btn_eliminar.grid(row=2, column=0, columnspan=2, pady=20)

    btn_crear = ctk.CTkButton(frame_derecha, text="Crear Cita", command=crear_cita)
    btn_crear.grid(row=1, column=0, pady=20, padx=20, sticky="e")

    btn_actualizar = ctk.CTkButton(frame_derecha, text="Actualizar Cita", command=formulario_actualizar_cita)
    btn_actualizar.grid(row=1, column=1, pady=20, padx=20, sticky="w")

    btn_eliminar = ctk.CTkButton(frame_derecha, text="Eliminar Cita", command=eliminar_cita_button)
    btn_eliminar.grid(row=2, column=0, pady=20, padx=20, sticky="e")

    btn_ver_citas = ctk.CTkButton(frame_derecha, text="Ver Citas", command=mostrar_mensaje_inicial)
    btn_ver_citas.grid(row=2, column=1, pady=20, padx=20, sticky="w")

def consultar_citas_por_dni():
    """
    Actualiza el marco derecho para permitir consultar citas por DNI.
    """
    for widget in frame_derecha.winfo_children():
        widget.destroy()

    # Título de la vista
    titulo = ctk.CTkLabel(frame_derecha, text="Consultar Citas por DNI", font=("Arial", 20, "bold"), text_color="#34495e")
    titulo.grid(row=0, column=0, columnspan=2, pady=5)

    # Campo para ingresar el DNI
    label_dni = ctk.CTkLabel(frame_derecha, text="Ingrese el DNI:", font=("Arial", 14), text_color="#34495e")
    label_dni.grid(row=1, column=0, padx=20, pady=5, sticky="e")

    entry_dni = ctk.CTkEntry(frame_derecha, width=250)
    entry_dni.grid(row=1, column=1, padx=20, pady=5, sticky="w")

    # Marco para la tabla
    scroll_frame = ctk.CTkScrollableFrame(frame_derecha, fg_color="#ecf0f1", height=600)
    scroll_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")
    scroll_frame.grid_columnconfigure((0, 1), weight=1)

    encabezados = ["Fecha y Hora", "Motivo"]
    for col_idx, encabezado in enumerate(encabezados):
        label_encabezado = ctk.CTkLabel(scroll_frame, text=encabezado, font=("Arial", 14, "bold"), text_color="#2c3e50")
        label_encabezado.grid(row=0, column=col_idx, padx=10, pady=5)

    def buscar_citas():
        for widget in scroll_frame.winfo_children():
            widget.destroy()
        for col_idx, encabezado in enumerate(encabezados):
            label_encabezado = ctk.CTkLabel(scroll_frame, text=encabezado, font=("Arial", 14, "bold"), text_color="#2c3e50")
            label_encabezado.grid(row=0, column=col_idx, padx=10, pady=5)

        dni = entry_dni.get().strip()
        if not dni:
            mensaje_error = ctk.CTkLabel(frame_derecha, text="Por favor, ingrese un DNI válido.", font=("Arial", 14), text_color="red")
            mensaje_error.grid(row=3, column=0, columnspan=2, pady=10)
            return

        citas = obtener_citas_por_paciente(dni)
        if not citas:
            mensaje_error = ctk.CTkLabel(frame_derecha, text="No se encontraron citas para este DNI.", font=("Arial", 14), text_color="red")
            mensaje_error.grid(row=3, column=0, columnspan=2, pady=10)
            return

        for row_idx, cita in enumerate(citas, start=1):
            if len(cita) >= 2:
                ctk.CTkLabel(scroll_frame, text=cita[0], font=("Arial", 12), text_color="#34495e").grid(row=row_idx, column=0, padx=10, pady=5)
                ctk.CTkLabel(scroll_frame, text=cita[1], font=("Arial", 12), text_color="#34495e").grid(row=row_idx, column=1, padx=10, pady=5)

    btn_buscar = ctk.CTkButton(frame_derecha, text="Buscar", font=("Arial", 14), fg_color="#2980b9", hover_color="#3498db", text_color="white", command=buscar_citas)
    btn_buscar.grid(row=3, column=0, columnspan=2, pady=10)


# Añadir el botón en el menú izquierdo
btn_consultar_citas = ctk.CTkButton(frame_izquierdo, text="Consultar Citas", font=("Arial", 14),
                                     width=170, height=50, corner_radius=15, command=consultar_citas_por_dni)
btn_consultar_citas.grid(row=5, column=0, padx=10, pady=20, sticky="n")


# Ejecutar la aplicación
app.mainloop()