# CRUD Consultorio Médico
 
A desktop CRUD application for managing a medical clinic's patient records, medical history, and appointments — built with Python and CustomTkinter, using SQLite for data storage.
 
## Features
 
- **Patient management (CRUD)**
  - Create new patients with full personal and medical details (name, date of birth, gender, ID number, contact info, blood type, allergies, pre-existing conditions, current medications, emergency contact)
  - Search patients by ID (DNI)
  - List all registered patients in a scrollable table
  - Edit patient information
  - Delete patients
- **Medical history**
  - View a patient's medical history (date, notes, diagnosis, treatment)
  - Add new medical history entries per patient
- **Appointments (Citas)**
  - Create appointments linked to a patient (via DNI lookup)
  - View all appointments or filter to a selected subset
  - Track appointment date/time and reason for visit
- **Logging**
  - Application events and errors are logged via a custom logger module, with logs organized by date
## Tech Stack
 
- **Language:** Python
- **GUI:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- **Database:** SQLite (local `.db` file)
## Project Structure
 
```
CRUD_ConsultorioMedico/
├── gui_main.py          # Main application entry point and all UI views
├── database.py          # CRUD functions (patients, history, appointments)
├── db_connector.py       # SQLite connection handling
├── logger.py             # Logging configuration
├── Scripts_SQl.sql       # SQL script to create the database schema
├── ConsultorioMedicoDB.db # SQLite database file
├── icono.ico             # Application icon
└── logs/                 # Generated log files, organized by date
```
 
## How It Works
 
On first run, the app copies `ConsultorioMedicoDB.db` into the user's home directory (so the packaged app always has a writable local database, even when bundled as an executable). All patient, history, and appointment data is then read from and written to that local copy via `db_connector.py` and `database.py`.
 
## Getting Started
 
### Prerequisites
 
- Python 3.9+
- pip
### Installation
 
1. Clone the repository:
```bash
   git clone https://github.com/SamuelPerezCO/CRUD_ConsultorioMedico.git
   cd CRUD_ConsultorioMedico
```
 
2. Install dependencies:
```bash
   pip install customtkinter
```
 
3. Run the app:
```bash
   python gui_main.py
```
 
The database file (`ConsultorioMedicoDB.db`) will be copied automatically to your home directory the first time you run the app.
 
## Database Schema
 
The database schema (tables for patients, medical history, and appointments) is defined in [`Scripts_SQl.sql`](./Scripts_SQl.sql). You can review this file to see the exact table structure and relationships.
 
## Notes
 
- This project was built as a hands-on exercise to practice CRUD operations, GUI development with CustomTkinter, and working with SQLite in Python.
- Currently designed for a single clinic/doctor use case (interface is labeled for "Consultorio Dermatológico").
## License
 
This project currently has no license specified. Feel free to reach out to the repository owner if you'd like to use or contribute to it.
