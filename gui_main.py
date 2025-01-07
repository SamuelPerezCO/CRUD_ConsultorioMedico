import customtkinter as ctk

# Configuración básica de la aplicación
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Crear ventana principal
app = ctk.CTk()
app.title("Consultorio Médico")
app.geometry("1100x600")  # Tamaño inicial
app.minsize(1100, 600)  # Tamaño mínimo

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

# Botón para crear paciente
btn_crear = ctk.CTkButton(frame_izquierdo, text="Crear paciente", font=("Arial", 14), width=170, height=50, corner_radius=15)
btn_crear.grid(row=1, column=0, padx=10, pady=20)

# Botón para buscar paciente (sin funcionalidad por ahora)
btn_buscar = ctk.CTkButton(frame_izquierdo, text="Buscar paciente", font=("Arial", 14), width=170, height=50, corner_radius=15)
btn_buscar.grid(row=2, column=0, padx=10, pady=20)

# Marco para la sección derecha
frame_derecha = ctk.CTkFrame(app, fg_color="transparent")
frame_derecha.grid(row=0, column=1, sticky="nswe")
frame_derecha.grid_rowconfigure(0, weight=1)
frame_derecha.grid_columnconfigure(0, weight=1)

# Mensaje inicial
mensaje_bienvenido = ctk.CTkLabel(frame_derecha, text="¡Bienvenido!\n¿Qué desea hacer?", font=("Arial", 20, "bold"), justify="center")
mensaje_bienvenido.grid(row=0, column=0, padx=20, pady=20)


# Función para mostrar el formulario
def mostrar_formulario():
    # Limpiar el contenido actual del marco derecho
    for widget in frame_derecha.winfo_children():
        widget.destroy()

    # Título del formulario
    titulo_form = ctk.CTkLabel(frame_derecha, text="Registro de Paciente", font=("Arial", 20, "bold"))
    titulo_form.grid(row=0, column=0, columnspan=2, pady=10)

    # Campos del formulario
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
            # Opciones de género
            genero_var = ctk.StringVar(value="Masculino")
            opciones_genero = ["Masculino", "Femenino", "Otro"]
            genero_menu = ctk.CTkOptionMenu(frame_derecha, values=opciones_genero, variable=genero_var)
            genero_menu.grid(row=idx+1, column=1, pady=5, padx=10, sticky="ew")
            entries[campo] = genero_var
        elif campo == "Tipo de Sangre":
            # Opciones de tipo de sangre
            sangre_var = ctk.StringVar(value="O+")
            opciones_sangre = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
            sangre_menu = ctk.CTkOptionMenu(frame_derecha, values=opciones_sangre, variable=sangre_var)
            sangre_menu.grid(row=idx+1, column=1, pady=5, padx=10, sticky="ew")
            entries[campo] = sangre_var
        else:
            entry = ctk.CTkEntry(frame_derecha)
            entry.grid(row=idx+1, column=1, pady=5, padx=10, sticky="ew")
            entries[campo] = entry

    # Botón para guardar los datos del paciente
    def guardar_paciente():
        # Aquí puedes agregar la lógica para guardar los datos del paciente
        datos_paciente = {campo: entrada.get() if not isinstance(entrada, ctk.StringVar) else entrada.get() for campo, entrada in entries.items()}
        print("Datos del paciente:", datos_paciente)
        # Restaurar mensaje inicial
        mostrar_mensaje_inicial()

    # Botón Guardar
    btn_guardar = ctk.CTkButton(frame_derecha, text="Guardar", command=guardar_paciente)
    btn_guardar.grid(row=len(campos)+1, column=0, columnspan=2, pady=20)

    # Ajustar columnas
    frame_derecha.grid_columnconfigure(1, weight=1)


# Función para mostrar el mensaje inicial
def mostrar_mensaje_inicial():
    # Limpiar el contenido actual del marco derecho
    for widget in frame_derecha.winfo_children():
        widget.destroy()

    # Volver a mostrar el mensaje inicial
    mensaje_bienvenido = ctk.CTkLabel(frame_derecha, text="¡Bienvenido!\n¿Qué desea hacer?", font=("Arial", 20, "bold"), justify="center")
    mensaje_bienvenido.grid(row=0, column=0, padx=20, pady=20)


# Asignar la función al botón "Crear paciente"
btn_crear.configure(command=mostrar_formulario)

# Mostrar el mensaje inicial al iniciar la aplicación
mostrar_mensaje_inicial()

# Ejecutar la aplicación
app.mainloop()
