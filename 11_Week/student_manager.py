from actions import Student

class StudentManager:
    def __init__(self):
        self.students = []  # Lista de objetos Student

    def get_grade(self, subject):
        while True:
            try:
                grade = int(input(f"Enter the final grade for {subject} (0-100): ").strip())
                if 0 <= grade <= 100:
                    return grade
                print("👎 Grade must be between 0 and 100.")
            except ValueError:
                print("👎 Please enter a valid number.")

    def validate_section(self, section):
        section = section.strip()
        if len(section) != 2:
            return False
        return (section[0].isdigit() and section[1].isalpha()) or (section[0].isalpha() and section[1].isdigit())

    def add_student(self):
        name = input("Enter student full name: ").strip()
        while True:
            section = input("Enter section (1 number + 1 letter, e.g., 1A or B2): ").strip()
            if self.validate_section(section):
                break
            print("👎 Invalid section format. Try e.g., 1A or B2.")

        spanish = self.get_grade("Spanish")
        english = self.get_grade("English")
        social = self.get_grade("Social")
        science = self.get_grade("Science")

        student = Student(name, section, spanish, english, social, science)
        self.students.append(student)
        print(f"✅ Student '{name}' added successfully!")

    def view_all_students(self):
        if not self.students:
            print("⚠️ No students found.")
            return
        for i, s in enumerate(self.students, 1):
            print(f"Student {i}: {s.name}, Section: {s.section}")
            print(f"  Spanish: {s.spanish}, English: {s.english}, Social: {s.social}, Science: {s.science}")
            print(f"  Average: {s.average:.2f}")
            print("-" * 30)

    def view_top_3_students(self):
        if not self.students:
            print("⚠️ No students found.")
            return
        top3 = sorted(self.students, key=lambda s: s.average, reverse=True)[:3]
        print("\n🏆 Top 3 Students by Average Grade:")
        for i, s in enumerate(top3, 1):
            print(f"{i}. {s.name} - Average: {s.average:.2f}")

    def calculate_overall_average(self):
        if not self.students:
            print("⚠️ No students found.")
            return
        overall = sum(s.average for s in self.students) / len(self.students)
        print(f"📊 Overall average grade: {overall:.2f}")

    def show_top_student_each_subject(self):
        if not self.students:
            print("⚠️ No students found.")
            return
        subjects = ["spanish", "english", "social", "science"]
        print("\n⭐ Top student per subject:")
        for subject in subjects:
            top = max(self.students, key=lambda s: getattr(s, subject))
            print(f"{subject.capitalize()}: {top.name} - {getattr(top, subject)}")

    def load_students_from_dicts(self, dicts):
        self.students = []
        for d in dicts:
            s = Student(d["name"], d["section"], d["spanish"], d["english"], d["social"], d["science"])
            self.students.append(s)
