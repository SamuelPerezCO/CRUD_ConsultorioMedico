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
frame_izquierdo.grid_rowconfigure((0, 1, 2), weight=1)
frame_izquierdo.grid_columnconfigure(0, weight=1)

# Título en el marco izquierdo
titulo = ctk.CTkLabel(frame_izquierdo, text="Consultorio", font=("Arial", 16, "bold"))
titulo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

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

# Mensaje inicial
def mostrar_mensaje_inicial():
    for widget in frame_derecha.winfo_children():
        widget.destroy()

    titulo_citas = ctk.CTkLabel(frame_derecha, text="Citas de Hoy", font=("Arial", 20, "bold"))
    titulo_citas.grid(row=0, column=0, columnspan=3, pady=10)

    for idx, cita in enumerate(citas):
        label_hora = ctk.CTkLabel(frame_derecha, text=f"Hora: {cita['Hora']}", font=("Arial", 14))
        label_hora.grid(row=idx+1, column=0, sticky="w", padx=10, pady=5)

        label_paciente = ctk.CTkLabel(frame_derecha, text=f"Paciente: {cita['Paciente']}", font=("Arial", 14))
        label_paciente.grid(row=idx+1, column=1, sticky="w", padx=10, pady=5)

        label_motivo = ctk.CTkLabel(frame_derecha, text=f"Motivo: {cita['Motivo']}", font=("Arial", 14))
        label_motivo.grid(row=idx+1, column=2, sticky="w", padx=10, pady=5)

mostrar_mensaje_inicial()

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
def mostrar_informacion_paciente(paciente):
    for widget in frame_derecha.winfo_children():
        widget.destroy()

    # Título de la información
    titulo_info = ctk.CTkLabel(frame_derecha, text="Información del Paciente", font=("Arial", 20, "bold"))
    titulo_info.grid(row=0, column=0, columnspan=2, pady=10)

    # Mostrar los datos del paciente
    for idx, (campo, valor) in enumerate(paciente.items()):
        label_campo = ctk.CTkLabel(frame_derecha, text=f"{campo}:", font=("Arial", 14, "bold"), anchor="w")
        label_campo.grid(row=idx+1, column=0, sticky="w", padx=10, pady=5)

        valor_campo = ctk.CTkLabel(frame_derecha, text=valor, font=("Arial", 14), anchor="w")
        valor_campo.grid(row=idx+1, column=1, sticky="w", padx=10, pady=5)

    # Botones adicionales
    btn_editar = ctk.CTkButton(frame_derecha, text="Editar", command=lambda: print("Editar paciente"))
    btn_editar.grid(row=len(paciente)+1, column=0, pady=20)

    btn_cita = ctk.CTkButton(frame_derecha, text="Crear Cita", command=lambda: print("Crear cita"))
    btn_cita.grid(row=len(paciente)+1, column=1, pady=20)

    btn_historia = ctk.CTkButton(frame_derecha, text="Generar Historia Clínica", command=lambda: print("Generar historia clínica"))
    btn_historia.grid(row=len(paciente)+2, column=0, columnspan=2, pady=10)

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
        "Número de Identificación (CI)",
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

# Botones en el menú izquierdo
btn_crear = ctk.CTkButton(frame_izquierdo, text="Crear paciente", font=("Arial", 14),
                          width=170, height=50, corner_radius=15, command=mostrar_formulario)
btn_crear.grid(row=1, column=0, padx=10, pady=20)

btn_buscar = ctk.CTkButton(frame_izquierdo, text="Buscar paciente", font=("Arial", 14),
                           width=170, height=50, corner_radius=15, command=mostrar_buscar_paciente)
btn_buscar.grid(row=2, column=0, padx=10, pady=20)

btn_crear_cita = ctk.CTkButton(frame_izquierdo , text="Crear Cita", font=("Arial" , 14),
                                width=170, height=50, corner_radius=15)
btn_crear_cita.grid(row=3 , column=0 , padx=10 , pady = 20)

# Ejecutar la aplicación
app.mainloop()
