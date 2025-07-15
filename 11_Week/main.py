from student_manager import StudentManager

def main():
    manager = StudentManager()

    while True:
        print("\nMenu:")
        print("1. Add student")
        print("2. View all students")
        print("3. View top 3 students")
        print("4. View overall average")
        print("5. View top student per subject")
        print("0. Exit")

        option = input("Choose an option: ")

        if option == "1":
            manager.add_student()
        elif option == "2":
            manager.view_all_students()
        elif option == "3":
            manager.view_top_3_students()
        elif option == "4":
            manager.calculate_overall_average()
        elif option == "5":
            manager.show_top_student_each_subject()
        elif option == "0":
            print("👋 Bye!")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
