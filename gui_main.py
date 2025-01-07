import customtkinter as ctk

# Configuración básica de la aplicación
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Crear ventana principal
app = ctk.CTk()
app.title("Consultorio Médico")
app.geometry("1100x600")  # Tamaño inicial
app.minsize(1100, 600)  # Tamaño mínimo
app.maxsize(1100, 600)  # Tamaño mínimo

# Configurar diseño de la ventana
app.grid_rowconfigure(0, weight=1)  # Ajustar la fila principal
app.grid_columnconfigure(0, weight=1)  # Columna izquierda ajustable
app.grid_columnconfigure(1, weight=4)  # Columna derecha ajustable

# Crear marco izquierdo para los botones
frame = ctk.CTkFrame(app)
frame.grid(row=0, column=0, sticky="nswe")  # Ajustar completamente
frame.grid_rowconfigure((0, 1, 2), weight=1)  # Proporción para título y botones
frame.grid_columnconfigure(0, weight=1)

# Título en el marco izquierdo
titulo = ctk.CTkLabel(frame, text="Consultorio", font=("Arial", 16, "bold"))
titulo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Botón para crear paciente
btn_crear = ctk.CTkButton(frame, text="Crear paciente", font=("Arial", 14), width=170, height=50, corner_radius=15)
btn_crear.grid(row=1, column=0, padx=10, pady=20)

# Botón para buscar paciente
btn_buscar = ctk.CTkButton(frame, text="Buscar paciente", font=("Arial", 14), width=170, height=50, corner_radius=15)
btn_buscar.grid(row=2, column=0, padx=10, pady=20)

# Marco para los mensajes en el área derecha
frame_derecha = ctk.CTkFrame(app, fg_color="transparent")  # Sin fondo para mejor integración
frame_derecha.grid(row=0, column=1, sticky="nswe")
frame_derecha.grid_rowconfigure(0, weight=1)  # Centrado verticalmente
frame_derecha.grid_columnconfigure(0, weight=1)  # Centrado horizontalmente

# Mensaje principal combinado
mensaje_bienvenido = ctk.CTkLabel(frame_derecha, text="¡Bienvenido!\n¿Qué desea hacer?", font=("Arial", 20, "bold"), justify="center")
mensaje_bienvenido.grid(row=0, column=0, padx=20, pady=20)

# Ejecutar la aplicación
app.mainloop()
