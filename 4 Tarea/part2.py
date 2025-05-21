name = input("What is your name? ")
last_name = input("What is your last name? ")
age = int(input("How old are you? "))  # Convertimos age a entero

# Condiciones de edad
if age < 2:
    print("You are a baby")
elif 2 <= age <= 10:
    print("You are a child")
elif 11 <= age <= 13:
    print("You are a pre-adolescent")
elif 14 <= age <= 17:
    print("You are an adolescent")
elif 18 <= age <= 25:
    print("You are a young adult")
elif 26 <= age <= 52:
    print("You are an adult")
else:
    print("You are a senior")

