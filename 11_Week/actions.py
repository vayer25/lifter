import csv

class Student:
    def __init__(self, name, section, spanish, english, social, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social = social
        self.science = science
        self.average = (spanish + english + social + science) / 4

    def to_dict(self):
        return {
            "name": self.name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "social": self.social,
            "science": self.science,
            "average": round(self.average, 2)
        }

def export_to_csv(students, filename="students.csv"):
    if not students:
        print("⚠️ No students to export.")
        return
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as f:
            fieldnames = ["name", "section", "spanish", "english", "social", "science", "average"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows([s.to_dict() for s in students])
        print(f"✅ Data exported successfully to '{filename}'.")
    except Exception as e:
        print(f"❌ Failed to export data: {e}")
