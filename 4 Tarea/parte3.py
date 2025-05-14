import random  # Iesto es lo que debiamos investigar de como generar el numero random

secret_number = random.randint(1, 10)

print("I have selected a secret number between 1 and 10. Try to guess it!")
# Bucle
while True:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        break  
    else:
        print("Incorrect guess. Try again.")
