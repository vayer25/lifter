import csv

students = []

def get_grade(subject):
    while True:
        try:
            grade = int(input(f"Enter your final grade for {subject} (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("👎 Invalid input. Grade must be between 0 and 100.")
        except ValueError:
            print("👎 Invalid input. Please enter numbers only.")

def validate_section(section):
    if len(section) != 2:
        return False
    return (section[0].isdigit() and section[1].isalpha()) or (section[0].isalpha() and section[1].isdigit())

def show_menu():
    print("\nMain Menu:")
    print("1. Enter student information")
    print("2. View all student information")
    print("3. View top 3 students by average grade")
    print("4. View overall average grade")
    print("5. Export data to CSV")
    print("6. Import data from CSV")
    print("7. View top student in each subject")
    print("0. Exit")

def export_to_csv(filename="students.csv"):
    if not students:
        print("⚠️ No data to export.")
        return
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=students[0].keys())
            writer.writeheader()
            writer.writerows(students)
        print(f"✅ Data exported successfully to '{filename}'.")
    except Exception as e:
        print(f"👎 Error exporting data: {e}")

def import_from_csv(filename="students.csv"):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            imported_students = []
            for row in reader:
                student = {
                    "name": row["name"],
                    "section": row["section"],
                    "spanish": int(row["spanish"]),
                    "english": int(row["english"]),
                    "social": int(row["social"]),
                    "science": int(row["science"]),
                    "average": float(row["average"])
                }
                imported_students.append(student)
            global students
            students = imported_students
        print(f"✅ Data imported successfully from '{filename}'.")
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")
    except Exception as e:
        print(f"❌ Error importing data: {e}")

def calculate_overall_average():
    if not students:
        print("⚠️ No student data available yet.")
        return
    total_sum = sum(s['average'] for s in students)
    overall_avg = total_sum / len(students)
    print(f"\n📊 Overall average grade of all students: {overall_avg:.2f}")

def show_top_student_each_subject():
    if not students:
        print("⚠️ No student data available yet.")
        return
    subjects = ["spanish", "english", "social", "science"]
    print("\n📊 Top student in each subject:\n")
    for subject in subjects:
        top_student = max(students, key=lambda s: s[subject])
        print(f"🏅 {subject.capitalize()}:")
        print(f"  Name: {top_student['name']}")
        print(f"  Section: {top_student['section']}")
        print(f"  Grade: {top_student[subject]}")
        print("-" * 30)

while True:
    show_menu()
    option = input("Choose an option (0-7): ").strip()

    if option == "1":
        name = input("Please enter the student's full name: ").strip()
        
        while True:
            section = input("Please enter the student's section (1 number + 1 letter, e.g., 1A or B2): ").strip()
            if validate_section(section):
                break
            else:
                print("👎 Invalid section format. It must contain exactly one number and one letter (e.g., '1A' or 'B2').")

        score_spanish = get_grade("Spanish")
        score_english = get_grade("English")
        score_social = get_grade("Social")
        score_science = get_grade("Science")

        average = (score_spanish + score_english + score_social + score_science) / 4

        student = {
            "name": name,
            "section": section,
            "spanish": score_spanish,
            "english": score_english,
            "social": score_social,
            "science": score_science,
            "average": average
        }

        students.append(student)
        print(f"✅ Student '{name}' added successfully!")

    elif option == "2":
        if not students:
            print("⚠️ No student data found. Please add a student first.")
        else:
            print("\n📋 List of all students:\n")
            for i, student in enumerate(students, start=1):
                print(f"Student {i}:")
                print(f"  Name: {student['name']}")
                print(f"  Section: {student['section']}")
                print(f"  Spanish: {student['spanish']}")
                print(f"  English: {student['english']}")
                print(f"  Social: {student['social']}")
                print(f"  Science: {student['science']}")
                print(f"  Average: {student['average']:.2f}")
                print("-" * 30)

    elif option == "3":
        if not students:
            print("⚠️ No student data available yet.")
        else:
            top_candidates = [s for s in students if s['average'] >= 90]
            top_candidates.sort(key=lambda s: s['average'], reverse=True)

            print("\n🏆 Top 3 Students by Average Grade 90:\n")

            if not top_candidates:
                print("👎 No students meet the criteria 90.")
            else:
                for i, student in enumerate(top_candidates[:3], start=1):
                    print(f"Top {i}:")
                    print(f"  Name: {student['name']}")
                    print(f"  Section: {student['section']}")
                    print(f"  Spanish: {student['spanish']}")
                    print(f"  English: {student['english']}")
                    print(f"  Social: {student['social']}")
                    print(f"  Science: {student['science']}")
                    print(f"  Average: {student['average']:.2f}")
                    print("-" * 30)

    elif option == "4":
        calculate_overall_average()

    elif option == "5":
        export_to_csv()

    elif option == "6":
        import_from_csv()

    elif option == "7":
        show_top_student_each_subject()

    elif option == "0":
        print("🙌 Thank you for using the Student Management Tool. Have a great day!")
        break

    else:
        print("👎 Invalid option. Please enter a number between 0 and 7.")
