class Student:
    def __init__(self, name, section, spanish, english, social, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social = social
        self.science = science
        self.average = (spanish + english + social + science) / 4

    def get_subject_score(self, subject):
        return getattr(self, subject, 0)


class StudentManager:
    def __init__(self):
        self.students = []

    def get_grade(self, subject):
        while True:
            try:
                grade = int(input(f"Enter your final grade for {subject} (0-100): "))
                if 0 <= grade <= 100:
                    return grade
                else:
                    print("👎 Invalid input. Grade must be between 0 and 100.")
            except ValueError:
                print("👎 Invalid input. Please enter numbers only.")

    def validate_section(self, section):
        return len(section) == 2 and (
            (section[0].isdigit() and section[1].isalpha()) or
            (section[0].isalpha() and section[1].isdigit())
        )

    def add_student(self):
        name = input("Please enter the student's full name: ").strip()
        
        while True:
            section = input("Please enter the student's section (1 number + 1 letter, e.g., 1A or B2): ").strip()
            if self.validate_section(section):
                break
            else:
                print("👎 Invalid section format.")

        scores = {
            "spanish": self.get_grade("Spanish"),
            "english": self.get_grade("English"),
            "social": self.get_grade("Social"),
            "science": self.get_grade("Science"),
        }

        student = Student(name, section, **scores)
        self.students.append(student)
        print(f"✅ Student '{name}' added successfully!")

    def view_all_students(self):
        if not self.students:
            print("⚠️ No student data found.")
            return
        for i, student in enumerate(self.students, start=1):
            print(f"Student {i}:")
            print(f"  Name: {student.name}")
            print(f"  Section: {student.section}")
            print(f"  Spanish: {student.spanish}")
            print(f"  English: {student.english}")
            print(f"  Social: {student.social}")
            print(f"  Science: {student.science}")
            print(f"  Average: {student.average:.2f}")
            print("-" * 30)

    def view_top_3_students(self):
        if not self.students:
            print("⚠️ No student data available.")
            return
        sorted_students = sorted(self.students, key=lambda s: s.average, reverse=True)
        print("\n🏆 Top 3 Students by Average Grade:\n")
        for i, student in enumerate(sorted_students[:3], start=1):
            print(f"Top {i}:")
            print(f"  Name: {student.name}")
            print(f"  Section: {student.section}")
            print(f"  Average: {student.average:.2f}")
            print("-" * 30)

    def calculate_overall_average(self):
        if not self.students:
            print("⚠️ No student data available yet.")
            return
        total = sum(student.average for student in self.students)
        avg = total / len(self.students)
        print(f"\n📊 Overall average grade: {avg:.2f}")

    def show_top_student_each_subject(self):
        if not self.students:
            print("⚠️ No student data available yet.")
            return
        subjects = ["spanish", "english", "social", "science"]
        for subject in subjects:
            top_student = max(self.students, key=lambda s: getattr(s, subject))
            print(f"{subject.capitalize()}: {top_student.name} - {getattr(top_student, subject)}")



if __name__ == "__main__":
    manager = StudentManager()

    while True:
        print("\n--- Student Management ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Top 3 Students")
        print("4. Overall Average Grade")
        print("5. Top Student in Each Subject")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_all_students()
        elif choice == "3":
            manager.view_top_3_students()
        elif choice == "4":
            manager.calculate_overall_average()
        elif choice == "5":
            manager.show_top_student_each_subject()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")