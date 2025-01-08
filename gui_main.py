import customtkinter as ctk

# Configuración básica de la aplicación
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Crear ventana principal
app = ctk.CTk()
app.title("Consultorio Médico")
app.geometry("1300x800")  # Tamaño inicial
app.minsize(1300, 800)  # Tamaño mínimo

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

btn_crear_cita = ctk.CTkButton(frame_izquierdo, text="Crear Cita", font=("Arial", 14),
                               width=170, height=50, corner_radius=15 , command=lambda: mostrar_crear_cita())
btn_crear_cita.grid(row=3, column=0, padx=10, pady=20, sticky="n")

btn_listar_pacientes = ctk.CTkButton(frame_izquierdo , text="Listar Pacientes" , font=("Arial" , 14),
                                     width=170 , height=50 , corner_radius=15 )
btn_listar_pacientes.grid(row=4 , column = 0, padx = 10, pady= 20 , sticky="n")

frame_izquierdo.grid_rowconfigure(4, weight=2)  # Espacio adicional para balancear

# Marco para la sección derecha
frame_derecha = ctk.CTkFrame(app, fg_color="transparent")
frame_derecha.grid(row=0, column=1, sticky="nswe")
frame_derecha.grid_rowconfigure(0, weight=1)
frame_derecha.grid_columnconfigure(0, weight=1)

# Lista de pacientes simulada
pacientes = [
    {"DNI": "123456", "Nombre Completo": "Juan Pérez", "Teléfono": "555-1234", "Correo Electrónico": "juan@example.com"}
]

# Lista de citas simulada
citas = [
    {"Hora": "10:00 AM", "Paciente": "Juan Pérez", "Motivo": "Consulta general"},
    {"Hora": "11:30 AM", "Paciente": "María Gómez", "Motivo": "Chequeo anual"},
    {"Hora": "02:00 PM", "Paciente": "Carlos López", "Motivo": "Dolor de cabeza"}
]

def mostrar_historia_clinica(paciente):
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
    encabezados = ["Fecha", "Motivo", "Diagnóstico", "Tratamiento"]
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
        for widget in frame_derecha.winfo_children():
            widget.destroy()

        # Título del formulario
        titulo_form = ctk.CTkLabel(frame_derecha, text=f"Agregar Registro - {paciente['Nombre Completo']}", font=("Arial", 22, "bold"))
        titulo_form.grid(row=0, column=0, columnspan=2, pady=20)

        # Campos del formulario
        campos_registro = ["Fecha (DD/MM/AAAA)", "Motivo", "Diagnóstico"]
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

# Mensaje inicial
def mostrar_mensaje_inicial():
    for widget in frame_derecha.winfo_children():
        widget.destroy()

    frame_derecha.grid_rowconfigure(0, weight=0)  # Encabezado fijo
    frame_derecha.grid_rowconfigure(1, weight=1)  # Espacio para la tabla
    frame_derecha.grid_columnconfigure(0, weight=1)

    # Encabezado principal
    titulo_citas = ctk.CTkLabel(frame_derecha, text="Citas de Hoy", font=("Arial", 20, "bold"))
    titulo_citas.grid(row=0, column=0, pady=(10, 20))  # Espaciado abajo

    # Crear marco desplazable para la tabla
    scroll_frame = ctk.CTkScrollableFrame(frame_derecha)
    scroll_frame.grid(row=1, column=0, sticky="nswe", padx=20, pady=10)
    scroll_frame.grid_columnconfigure((0, 1, 2), weight=1)  # Ajustar columnas

    # Encabezados de la tabla
    encabezados = ["Hora", "Paciente", "Motivo"]
    for idx, encabezado in enumerate(encabezados):
        label_encabezado = ctk.CTkLabel(scroll_frame, text=encabezado, font=("Arial", 14, "bold"))
        label_encabezado.grid(row=0, column=idx, padx=10, pady=10, sticky="nsew")

    # Filas de la tabla
    for row_idx, cita in enumerate(citas, start=1):
        label_hora = ctk.CTkLabel(scroll_frame, text=cita["Hora"], font=("Arial", 12))
        label_hora.grid(row=row_idx, column=0, padx=10, pady=5, sticky="nsew")

        label_paciente = ctk.CTkLabel(scroll_frame, text=cita["Paciente"], font=("Arial", 12))
        label_paciente.grid(row=row_idx, column=1, padx=10, pady=5, sticky="nsew")

        label_motivo = ctk.CTkLabel(scroll_frame, text=cita["Motivo"], font=("Arial", 12))
        label_motivo.grid(row=row_idx, column=2, padx=10, pady=5, sticky="nsew")


mostrar_mensaje_inicial()

def mostrar_crear_cita():
    for widget in frame_derecha.winfo_children():
        widget.destroy()

    # Configurar diseño
    frame_derecha.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
    frame_derecha.grid_columnconfigure((0, 1), weight=1)

    # Título
    titulo_form = ctk.CTkLabel(frame_derecha, text="Crear Cita", font=("Arial", 20, "bold"))
    titulo_form.grid(row=0, column=0, columnspan=2, pady=20)

    # Campos del formulario
    # Seleccionar Paciente
    label_paciente = ctk.CTkLabel(frame_derecha, text="Paciente:", font=("Arial", 14), anchor="w")
    label_paciente.grid(row=1, column=0, padx=20, pady=10, sticky="e")

    pacientes_var = ctk.StringVar(value="Seleccionar paciente")
    pacientes_nombres = [p["Nombre Completo"] for p in pacientes]
    menu_pacientes = ctk.CTkOptionMenu(frame_derecha, values=pacientes_nombres, variable=pacientes_var)
    menu_pacientes.grid(row=1, column=1, padx=20, pady=10, sticky="w")

    # Ingresar Hora
    label_hora = ctk.CTkLabel(frame_derecha, text="Hora (HH:MM AM/PM):", font=("Arial", 14), anchor="w")
    label_hora.grid(row=2, column=0, padx=20, pady=10, sticky="e")

    entry_hora = ctk.CTkEntry(frame_derecha)
    entry_hora.grid(row=2, column=1, padx=20, pady=10, sticky="w")

    # Motivo de la cita
    label_motivo = ctk.CTkLabel(frame_derecha, text="Motivo:", font=("Arial", 14), anchor="w")
    label_motivo.grid(row=3, column=0, padx=20, pady=10, sticky="e")

    entry_motivo = ctk.CTkEntry(frame_derecha)
    entry_motivo.grid(row=3, column=1, padx=20, pady=10, sticky="w")

    # Botón para guardar cita
    def guardar_cita():
        paciente_seleccionado = pacientes_var.get()
        hora = entry_hora.get().strip()
        motivo = entry_motivo.get().strip()

        if paciente_seleccionado == "Seleccionar paciente" or not hora or not motivo:
            mensaje_error = ctk.CTkLabel(frame_derecha, text="Por favor, complete todos los campos.", font=("Arial", 14), fg_color="red")
            mensaje_error.grid(row=5, column=0, columnspan=2, pady=10)
            return

        nueva_cita = {
            "Hora": hora,
            "Paciente": paciente_seleccionado,
            "Motivo": motivo
        }
        citas.append(nueva_cita)
        mostrar_mensaje_inicial()  # Regresar a la lista de citas

    btn_guardar = ctk.CTkButton(frame_derecha, text="Guardar Cita", command=guardar_cita)
    btn_guardar.grid(row=4, column=0, columnspan=2, pady=20)

# Función para mostrar el formulario de búsqueda (centrado)
def mostrar_buscar_paciente():
    for widget in frame_derecha.winfo_children():
        widget.destroy()

    # Configurar centrado
    frame_derecha.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
    frame_derecha.grid_columnconfigure((0, 1), weight=1)

    # Título de búsqueda
    titulo_busqueda = ctk.CTkLabel(frame_derecha, text="Buscar Paciente", font=("Arial", 20, "bold"))
    titulo_busqueda.grid(row=1, column=0, columnspan=2, pady=10)

    # Campo para el DNI
    label_dni = ctk.CTkLabel(frame_derecha, text="DNI:", anchor="w", font=("Arial", 14))
    label_dni.grid(row=2, column=0, sticky="e", padx=10)

    entry_dni = ctk.CTkEntry(frame_derecha)
    entry_dni.grid(row=2, column=1, sticky="w", padx=10)

    def buscar_paciente():
        dni = entry_dni.get().strip()
        paciente = next((p for p in pacientes if p["DNI"] == dni), None)
        if paciente:
            mostrar_informacion_paciente(paciente)
        else:
            mensaje_error = ctk.CTkLabel(frame_derecha, text="Paciente no encontrado", font=("Arial", 14), fg_color="red")
            mensaje_error.grid(row=4, column=0, columnspan=2, pady=20)

    # Botón de búsqueda
    btn_buscar = ctk.CTkButton(frame_derecha, text="Buscar", command=buscar_paciente)
    btn_buscar.grid(row=3, column=0, columnspan=2, pady=10)

# Función para mostrar la información del paciente
# Declaración global para pacientes_var
pacientes_var = ctk.StringVar(value="Seleccionar paciente")

def mostrar_informacion_paciente(paciente):
    for widget in frame_derecha.winfo_children():
        widget.destroy()

    titulo_info = ctk.CTkLabel(frame_derecha, text="Información del Paciente", font=("Arial", 20, "bold"))
    titulo_info.grid(row=0, column=0, columnspan=2, pady=10)

    # Diccionario para campos y valores
    campos = {
        "Nombre Completo": paciente.get("Nombre Completo", ""),
        "DNI": paciente.get("DNI", ""),
        "Fecha de Nacimiento (DD/MM/AAAA)": paciente.get("Fecha de Nacimiento (DD/MM/AAAA)" , ""),
        "Género": paciente.get("Género" , ""),
        "Teléfono": paciente.get("Teléfono", ""),
        "Correo Electrónico": paciente.get("Correo Electrónico", ""),
        "Dirección":paciente.get("Dirección" , ""),
        "Tipo de Sangre":paciente.get("Tipo de Sangre" , ""),
        "Alergias":paciente.get("Alergias" , ""),
        "Condiciones Médicas Preexistentes":paciente.get("Condiciones Médicas Preexistentes" , ""),
        "Medicamentos Actuales":paciente.get("Medicamentos Actuales" , ""),
        "Nombre Contacto de Emergencia":paciente.get("Nombre Contacto de Emergencia" , ""),
        "Teléfono de Emergencia":paciente.get("Nombre Contacto de Emergencia" , ""),
        "Relación con el Paciente":paciente.get("Relación con el Paciente" , "")
    }

    labels = {}

    # Mostrar datos como etiquetas
    for idx, (campo, valor) in enumerate(campos.items()):
        label_campo = ctk.CTkLabel(frame_derecha, text=f"{campo}:", font=("Arial", 14, "bold"), anchor="w")
        label_campo.grid(row=idx+1, column=0, pady=5, sticky="w", padx=10)

        label_valor = ctk.CTkLabel(frame_derecha, text=valor, font=("Arial", 14), anchor="w")
        label_valor.grid(row=idx+1, column=1, pady=5, sticky="w", padx=10)
        labels[campo] = label_valor

    entries = {}  # Mover entries al ámbito de la función principal

    def habilitar_edicion():
        for widget in labels.values():
            widget.grid_forget()
        for idx, (campo, valor) in enumerate(campos.items()):
            entry = ctk.CTkEntry(frame_derecha)
            entry.insert(0, valor)
            entry.grid(row=idx+1, column=1, pady=5, sticky="w", padx=10)
            entries[campo] = entry

        btn_editar.grid_forget()
        btn_guardar.grid(row=len(campos)+1, column=0, columnspan=2, pady=10)

    def guardar_cambios():
        for campo, entry in entries.items():
            paciente[campo] = entry.get()
            labels[campo].configure(text=entry.get())
            entry.grid_forget()
            labels[campo].grid(row=list(campos.keys()).index(campo)+1, column=1, pady=5, sticky="w", padx=10)

        btn_guardar.grid_forget()
        btn_editar.grid(row=len(campos)+1, column=0, columnspan=2, pady=10)

    def ir_a_crear_cita():
        mostrar_crear_cita()
        if paciente["Nombre Completo"] in [p["Nombre Completo"] for p in pacientes]:
            pacientes_var.set(paciente["Nombre Completo"])

    # Botón para guardar cambios (declarado antes para que sea accesible)
    btn_guardar = ctk.CTkButton(frame_derecha, text="Guardar Cambios", command=guardar_cambios)

    # Botón para editar información
    btn_editar = ctk.CTkButton(frame_derecha, text="Editar Información", command=habilitar_edicion)
    btn_editar.grid(row=len(campos)+1, column=0, columnspan=2, pady=10)

    # Botón para crear cita
    btn_crear_cita = ctk.CTkButton(frame_derecha, text="Crear Cita", command=ir_a_crear_cita)
    btn_crear_cita.grid(row=len(campos)+2, column=0, columnspan=2, pady=10)

    # Botón para volver
    btn_volver = ctk.CTkButton(frame_derecha, text="Volver", command=mostrar_mensaje_inicial)
    btn_volver.grid(row=len(campos)+3, column=0, columnspan=2, pady=10)

    btn_eliminar = ctk.CTkButton(frame_derecha , text = "Eliminar")
    btn_eliminar.grid(row=len(campos)+4, column=0 , columnspan= 2, pady=10)

    frame_derecha.grid_columnconfigure(1, weight=1)

# Función para mostrar el formulario de crear paciente (sin cambios)
def mostrar_formulario():
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
        label.grid(row=idx+1, column=0, pady=5, sticky="w", padx=10)

        if campo == "Género":
            genero_var = ctk.StringVar(value="Masculino")
            opciones_genero = ["Masculino", "Femenino", "Otro"]
            genero_menu = ctk.CTkOptionMenu(frame_derecha, values=opciones_genero, variable=genero_var)
            genero_menu.grid(row=idx+1, column=1, pady=5, padx=10, sticky="ew")
            entries[campo] = genero_var
        elif campo == "Tipo de Sangre":
            sangre_var = ctk.StringVar(value="O+")
            opciones_sangre = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
            sangre_menu = ctk.CTkOptionMenu(frame_derecha, values=opciones_sangre, variable=sangre_var)
            sangre_menu.grid(row=idx+1, column=1, pady=5, padx=10, sticky="ew")
            entries[campo] = sangre_var
        else:
            entry = ctk.CTkEntry(frame_derecha)
            entry.grid(row=idx+1, column=1, pady=5, padx=10, sticky="ew")
            entries[campo] = entry

    def guardar_paciente():
        datos_paciente = {campo: entrada.get() if not isinstance(entrada, ctk.StringVar) else entrada.get() for campo, entrada in entries.items()}
        pacientes.append(datos_paciente)
        mostrar_informacion_paciente(datos_paciente)

    btn_guardar = ctk.CTkButton(frame_derecha, text="Guardar", command=guardar_paciente)
    btn_guardar.grid(row=len(campos)+1, column=0, columnspan=2, pady=20)

    frame_derecha.grid_columnconfigure(1, weight=1)


# Ejecutar la aplicación
app.mainloop()
