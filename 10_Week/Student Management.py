name = input("Please enter your name: ")
session=input("Please enter your seccion(example 11B): ")


def get_grade(subject):
    while True:
        try:
            grade = int(input(f"Enter your final grade for {subject} (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("❌ Invalid input. Grade must be between 0 and 100.")
        except ValueError:
            print("❌ Invalid input. Please enter numbers only.")

score_spanish = get_grade("Spanish")
score_english = get_grade("English")
score_social = get_grade("Social")
score_science = get_grade("Science")


