CREATE TABLE Paciente (
    id_paciente INTEGER PRIMARY KEY,
    nombre_completo TEXT NOT NULL,
    fecha_nacimiento TEXT,
    genero TEXT,
    numero_identificacion TEXT,
    telefono TEXT,
    correo_electronico TEXT,
    direccion TEXT,
    tipo_sangre TEXT,
    alergias TEXT,
    condiciones_medicas_preexistentes TEXT,
    medicamentos_actuales TEXT,
    nombre_contacto_emergencia TEXT,
    telefono_emergencia TEXT,
    relacion_paciente TEXT
);

CREATE TABLE Historia_Clinica (
    id_historia INTEGER PRIMARY KEY,
    id_paciente INTEGER,
    fecha TEXT NOT NULL,
    motivo TEXT,
    diagnostico TEXT,
    tratamiento TEXT,
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente)
);

CREATE TABLE Cita (
    id_cita INTEGER PRIMARY KEY,
    id_paciente INTEGER,
    fecha_hora TEXT NOT NULL,
    motivo TEXT,
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente)
);
