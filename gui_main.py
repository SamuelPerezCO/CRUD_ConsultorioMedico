import customtkinter as ctk

# Configuración básica de la aplicación
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Crear ventana principal
app = ctk.CTk()
app.title("Consultorio")
app.geometry("1100x600")  # Tamaño inicial
app.minsize(1100, 600)  # Tamaño mínimo

# Configurar diseño de la ventana
app.grid_rowconfigure(0, weight=1)  # Ajustar la fila principal
app.grid_columnconfigure(0, weight=1)  # Columna izquierda ajustable
app.grid_columnconfigure(1, weight=4)  # Columna derecha ajustable

# Crear marco izquierdo para los botones
frame = ctk.CTkFrame(app)
frame.grid(row=0, column=0, sticky="nswe")  # Ajustar completamente
frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)  # Proporción para título y botones
frame.grid_columnconfigure(0, weight=1)

# Título en el marco izquierdo
titulo = ctk.CTkLabel(frame, text="Consultorio", font=("Arial", 16, "bold"))
titulo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Botones con tamaño fijo y ajustados
btn_crear = ctk.CTkButton(frame, text="Crear paciente", font=("Arial", 14), width=150, height=50)
btn_crear.grid(row=1, column=0, padx=10, pady=10)

btn_buscar = ctk.CTkButton(frame, text="Buscar paciente", font=("Arial", 14), width=150, height=50)
btn_buscar.grid(row=2, column=0, padx=10, pady=10)

btn_editar = ctk.CTkButton(frame, text="Editar paciente", font=("Arial", 14), width=150, height=50)
btn_editar.grid(row=3, column=0, padx=10, pady=10)

btn_eliminar = ctk.CTkButton(frame, text="Eliminar paciente", font=("Arial", 14), width=150, height=50)
btn_eliminar.grid(row=4, column=0, padx=10, pady=10)

# Mensaje de bienvenida en el área derecha
mensaje = ctk.CTkLabel(app, text="¡Bienvenido!", font=("Arial", 20, "bold"))
mensaje.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)  # Centrado automáticamente

# Ejecutar la aplicación
app.mainloop()
