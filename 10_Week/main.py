from menu import show_menu
from actions import (
    add_student, view_all_students,
    view_top_3_students, calculate_overall_average,
    show_top_student_each_subject
)
from data import export_to_csv, import_from_csv

students = []

while True:
    show_menu()
    option = input("Choose an option (0-7): ").strip()

    if option == "1":
        add_student(students)
    elif option == "2":
        view_all_students(students)
    elif option == "3":
        view_top_3_students(students)
    elif option == "4":
        calculate_overall_average(students)
    elif option == "5":
        export_to_csv(students)
    elif option == "6":
        students = import_from_csv()
    elif option == "7":
        show_top_student_each_subject(students)
    elif option == "0":
        print("🙌 Thanks for using the tool!")
        break
    else:
        print("👎 Invalid option. Please enter a number between 0 and 7.")
