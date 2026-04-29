🏥 Hospital Appointment System (Python CLI)

📌 Overview

This project is a command-line based Hospital Appointment System built using Python.
It simulates real-world hospital operations such as patient registration, doctor search, slot management, appointment booking, cancellation, and history tracking.

The system is designed using modular functions and in-memory data structures (lists and dictionaries) instead of databases.


Features:

-  Patient Registration
-  Search Doctors by Name or Specialty
-  View Available Appointment Slots
-  Book Appointment
-  Cancel Appointment
-  View Patient History
-  Dynamic Slot Generation per Date
-  Prevent Double Booking
-  Emergency Slot Reserved (Not Bookable)



🧠 System Architecture

The system is divided into logical domains:

1. Patient Domain

- Stores patient details in a list
- Each patient has:
  - ID, Name, Age, Phone



2. Doctor Domain

- Predefined doctors (demo setup)
- Each doctor contains:
  - ID, Name, Specialty, Slots



3. Slot Management

- Slots are dynamically created using:
  build_slots_for_date()
- Each slot includes:
  - ID, Date, Time, Booked Status, Emergency Flag



4. Appointment Domain

- Stores all bookings
- Each appointment contains:
  - Appointment ID
  - Patient ID
  - Doctor ID
  - Slot ID
  - Date & Time
  - Status (CONFIRMED / CANCELLED)



5. Utility Functions

- "parse_date()" → Validates date format
- "find_*()" → Search helpers for doctors, patients, appointments



🔄 Flow of Execution

Start Program
    ↓
Menu Display
    ↓
User Choice
    ↓
[Register / Search / Show Slots / Book / Cancel / History]
    ↓
Update Data (Patients / Doctors / Appointments)
    ↓
Repeat Until Exit



⚙️ Technologies Used

- Python (Core)
- CLI (Command Line Interface)
- Data Structures:
  - List
  - Dictionary



📂 Data Storage Design

Entity| Data Structure
Doctors| List of Dictionaries
Patients| List of Dictionaries
Appointments| List of Dictionaries
Slots| Nested inside Doctors



🧩 Key Concepts Used

- Functional Programming (modular functions)
- Data Validation (date, input checks)
- List Comprehension
- Dictionary Handling
- State Management (booked / available)
- Real-world system modeling



🚀 How to Run

python main.py



📌 Sample Menu

1. Register patient
2. Search doctor
3. Show slots
4. Book
5. Cancel
6. History
0. Exit



🧠 Learning Outcomes

- Understanding system design basics
- Breaking real-world problems into code modules
- Managing state without databases
- Writing clean, structured CLI applications



🔮 Future Improvements

- Add payment system
- Add login/authentication
- Use database (SQLite / MySQL)
- Convert to GUI / Web app
- Add doctor availability scheduling



🙌 Author

Kumaran.R

B.E Robotics and Automation [231601027]
