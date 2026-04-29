def parse_date(text):
    parts = text.split("-")
    if len(parts) != 3:
        return None
    year, month, day = parts
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return None
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return None
    return text


def build_slots_for_date(doctor, date_text):
    existing = [slot for slot in doctor["slots"] if slot["date"] == date_text]
    if existing:
        return
    slot_times = [
        "09:00-09:40",
        "09:50-10:30",
        "10:40-11:20",
        "11:30-12:10",
        "13:00-13:40",
        "13:50-14:30",
        "14:40-15:20",
    ]
    for index, time in enumerate(slot_times, start=1):
        doctor["slots"].append({
            "id": f"{doctor['id']}-{date_text.replace('-', '')}-{index}",
            "date": date_text,
            "time": time,
            "booked": False,
            "emergency": index == len(slot_times),
        })


def setup_demo():
    doctors = [
        {"id": "D01", "name": "Dr. Reddy", "specialty": "General", "slots": []},
        {"id": "D02", "name": "Dr. Khan", "specialty": "Dermatology", "slots": []},
        {"id": "D03", "name": "Dr. Singh", "specialty": "ENT", "slots": []},
    ]
    patients = []
    appointments = []
    return doctors, patients, appointments


def find_doctor(doctors, doctor_id):
    for doctor in doctors:
        if doctor["id"] == doctor_id:
            return doctor
    return None


def find_patient(patients, patient_id):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    return None


def find_appointment(appointments, appointment_id):
    for appt in appointments:
        if appt["id"] == appointment_id:
            return appt
    return None


def get_free_slots(doctor, date_text):
    build_slots_for_date(doctor, date_text)
    return [slot for slot in doctor["slots"] if slot["date"] == date_text and not slot["booked"] and not slot["emergency"]]


def show_slots(doctor, date_text):
    free_slots = get_free_slots(doctor, date_text)
    if not free_slots:
        print("No slots available")
        return
    print(f"Available slots for {doctor['name']} on {date_text}:")
    for slot in free_slots:
        print(f"{slot['id']} {slot['time']}")


def cancel_appointment(appointments, doctors, appt_id):
    appt = find_appointment(appointments, appt_id)
    if not appt:
        return False
    appt["status"] = "CANCELLED"
    for doctor in doctors:
        for slot in doctor["slots"]:
            if slot["id"] == appt["slot_id"]:
                slot["booked"] = False
                return True
    return True


def show_patient_history(appointments, patient_id):
    found = [appt for appt in appointments if appt["patient_id"] == patient_id]
    if not found:
        print("No history for this patient")
        return
    for appt in found:
        print(f"{appt['id']} doctor={appt['doctor_id']} date={appt['date']} time={appt['time']} status={appt['status']}")


def main():
    doctors, patients, appointments = setup_demo()
    next_appt_id = 1

    print("Simple hospital appointment demo")

    while True:
        print("\nMenu:")
        print("1. Register patient")
        print("2. Search doctor")
        print("3. Show slots")
        print("4. Book")
        print("5. Cancel")
        print("6. History")
        print("0. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            patient_id = input("Patient ID: ").strip()
            name = input("Name: ").strip()
            age = input("Age: ").strip()
            phone = input("Phone: ").strip()
            if not patient_id or not age.isdigit():
                print("Bad input")
                continue
            if find_patient(patients, patient_id):
                print("Already registered")
                continue
            patients.append({"id": patient_id, "name": name, "age": int(age), "phone": phone})
            print("Patient added")

        elif choice == "2":
            term = input("Doctor name or specialty: ").strip().lower()
            found = [doc for doc in doctors if term in doc["name"].lower() or term in doc["specialty"].lower()]
            if not found:
                print("No doctor found")
                continue
            for doc in found:
                print(f"{doc['id']} {doc['name']} ({doc['specialty']})")

        elif choice == "3":
            doctor_id = input("Doctor ID: ").strip()
            date_text = input("Date YYYY-MM-DD: ").strip()
            if not parse_date(date_text):
                print("Bad date")
                continue
            doctor = find_doctor(doctors, doctor_id)
            if not doctor:
                print("Doctor missing")
                continue
            show_slots(doctor, date_text)

        elif choice == "4":
            patient_id = input("Patient ID: ").strip()
            doctor_id = input("Doctor ID: ").strip()
            date_text = input("Date YYYY-MM-DD: ").strip()
            if not parse_date(date_text):
                print("Bad date")
                continue
            patient = find_patient(patients, patient_id)
            doctor = find_doctor(doctors, doctor_id)
            if not patient or not doctor:
                print("Patient or doctor not found")
                continue
            free_slots = get_free_slots(doctor, date_text)
            if not free_slots:
                print("No slots available")
                continue
            print(f"Available slots for {doctor['name']} on {date_text}:")
            for slot in free_slots:
                print(f"{slot['id']} {slot['time']}")
            slot_id = input("Slot ID: ").strip()
            for slot in doctor["slots"]:
                if slot["id"] == slot_id:
                    if slot["booked"] or slot["emergency"]:
                        print("Can't book this slot")
                        break
                    slot["booked"] = True
                    appt_id = f"A{next_appt_id}"
                    next_appt_id += 1
                    appointments.append({
                        "id": appt_id,
                        "patient_id": patient_id,
                        "doctor_id": doctor_id,
                        "slot_id": slot_id,
                        "date": slot["date"],
                        "time": slot["time"],
                        "status": "CONFIRMED",
                    })
                    print(f"Booked {appt_id}: {doctor['name']} ({doctor['specialty']}) on {slot['date']} at {slot['time']}")
                    break
            else:
                print("Slot not found")

        elif choice == "5":
            appt_id = input("Appointment ID: ").strip()
            if cancel_appointment(appointments, doctors, appt_id):
                print("Cancelled")
            else:
                print("No appointment")

        elif choice == "6":
            patient_id = input("Patient ID: ").strip()
            if not find_patient(patients, patient_id):
                print("Patient not found")
                continue
            show_patient_history(appointments, patient_id)

        elif choice == "0":
            print("Goodbye")
            break

        else:
            print("Try again")


if __name__ == "__main__":
    main()
