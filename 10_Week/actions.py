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

def add_student(students):
    name = input("Please enter the student's full name: ").strip()
    
    while True:
        section = input("Please enter the student's section (1 number + 1 letter, e.g., 1A or B2): ").strip()
        if validate_section(section):
            break
        else:
            print("👎 Invalid section format.")

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

def view_all_students(students):
    if not students:
        print("⚠️ No student data found.")
    else:
        for i, student in enumerate(students, start=1):
            print(f"Student {i}:")
            for key, value in student.items():
                print(f"  {key.capitalize()}: {value}")
            print("-" * 30)

def view_top_3_students(students):
    if not students:
        print("⚠️ No student data available.")
        return

    sorted_students = sorted(students, key=lambda s: s['average'], reverse=True)
    print("\n🏆 Top 3 Students by Average Grade:\n")
    for i, student in enumerate(sorted_students[:3], start=1):
        print(f"Top {i}:")
        print(f"  Name: {student['name']}")
        print(f"  Section: {student['section']}")
        print(f"  Average: {student['average']:.2f}")
        print("-" * 30)

def calculate_overall_average(students):
    if not students:
        print("⚠️ No student data available yet.")
        return
    total_sum = sum(s['average'] for s in students)
    overall_avg = total_sum / len(students)
    print(f"\n📊 Overall average grade: {overall_avg:.2f}")

def show_top_student_each_subject(students):
    if not students:
        print("⚠️ No student data available yet.")
        return
    subjects = ["spanish", "english", "social", "science"]
    for subject in subjects:
        top_student = max(students, key=lambda s: s[subject])
        print(f"{subject.capitalize()}: {top_student['name']} - {top_student[subject]}")
