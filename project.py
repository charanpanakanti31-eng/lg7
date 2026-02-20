from datetime import datetime

#Person Parent class...................
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Doctor Child class .............. 
class Doctor(Person):
    def get_role(self):
        return "General Doctor"

class SpecialistDoctor(Doctor):
    def __init__(self, id, name, specialty):
        super().__init__(id, name)
        self.specialty = specialty

    def get_role(self):
        return (f"Specialist ({self.specialty})")

# Medical History.......................
class MedicalHistory:
    def __init__(self):
        self.__records = []

    def add(self, record):
        self.__records.append(record)

    def show(self):
        return self.__records

# Patient Child class.....................
class Patient(Person):
    def __init__(self, id, name, age):
        super().__init__(id, name)
        self.age = age
        self.history = MedicalHistory()

# Hospital System..................
class Hospital:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = []

    def add_patient(self):
        id = input("Patient ID: ")
        if id in self.patients:
            print("Patient exists."); 
            return
        self.patients[id] = Patient(id, input("Name: "), input("Age: "))
        print("Patient added.")

    def add_doctor(self):
        id = input("Doctor ID: ")
        if id in self.doctors:
            print("Doctor exists."); return
        name = input("Name: ")
        if input("1.General 2.Specialist: ") == "2":
            self.doctors[id] = SpecialistDoctor(id, name, input("Specialty: "))
        else:
            self.doctors[id] = Doctor(id, name)
        print("Doctor added.")

    def book(self):
        pid = input("Patient ID: ")
        did = input("Doctor ID: ")
        if pid not in self.patients or did not in self.doctors:
            print("Patient/Doctor not found."); return
        try:
            dt = datetime.strptime(input("Date (YYYY-MM-DD HH:MM): "),"%Y-%m-%d %H:%M")
        except:
            print("Wrong format."); return
        for a in self.appointments:
            if a[1] == did and a[2] == dt:
                print("Appointment clash!"); return
        self.appointments.append((pid, did, dt))
        print("Appointment booked.")

    def add_record(self):
        pid = input("Patient ID: ")
        if pid in self.patients:
            self.patients[pid].history.add(input("Diagnosis: "))
            print("Record added.")
        else:
            print("Patient not found.")

    def view_history(self):
        pid = input("Patient ID: ")
        if pid in self.patients:
            print(self.patients[pid].history.show())
        else:
            print("Patient not found.")

    def save(self):
        with open("records.txt", "w") as f:
            for p in self.patients.values():
                f.write(f"Patient:{p.id},{p.name},{p.age}\n")
            for d in self.doctors.values():
                f.write(f"Doctor:{d.id},{d.name},{d.get_role()}\n")
            for a in self.appointments:
                f.write(f"Appointment:{a[0]},{a[1]},{a[2]}\n")
        print("Data saved.")

# creating object..........
h = Hospital()
while True:
    print("\nHospital Patient Management System")
    print("1.Register Patient \n2.Register Doctor \n3.Book Appointment \n4.Add Record  \n5.View History \n6.Save Data \n7.Exit")
    ch = input("Choice: ")
    if ch == "1":
        h.add_patient()
    elif ch == "2":
        h.add_doctor()
    elif ch == "3":
        h.book()
    elif ch == "4":
        h.add_record()
    elif ch == "5":
        h.view_history()
    elif ch == "6":
        h.save()
    elif ch == "7":
         h.save(); break
    else:
        print("Invalid choice.")
