from student_manager import StudentManager
from actions import export_to_csv
from data import import_from_csv

def show_menu():
    print("\n===== Student Management Menu =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. View Top 3 Students")
    print("4. Calculate Overall Average")
    print("5. Show Top Student Per Subject")
    print("6. Export Data to CSV")
    print("7. Import Data from CSV")
    print("8. Exit")

def main():
    manager = StudentManager()
    # Auto-load students from CSV if exists on start (optional)
    students_dicts = import_from_csv()
    manager.load_students_from_dicts(students_dicts)

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
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
            filename = input("Enter filename for CSV export (default students.csv): ").strip()
            if not filename:
                filename = "students.csv"
            export_to_csv(manager.students, filename)
        elif choice == "7":
            filename = input("Enter filename for CSV import (default students.csv): ").strip()
            if not filename:
                filename = "students.csv"
            dicts = import_from_csv(filename)
            manager.load_students_from_dicts(dicts)
            print("✅ Students loaded from CSV.")
        elif choice == "8":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
