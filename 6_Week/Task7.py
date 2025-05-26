# Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
# a. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
# b. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
# c. Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar otra función para revisar si el numero es primo o no.

def filter_prime(lst):
    prime = []  # List to store prime numbers
    for num in lst:  # Iterate through each number in the list
        if num > 1:  # Primes are greater than 1
            is_prime = True  # Assume the number is prime
            for i in range(2, num):  # Check divisibility from 2 to num-1
                if num % i == 0:  # If divisible, it's not prime
                    is_prime = False
                    break
            if is_prime:  # If no divisors found, it's prime
                prime.append(num)  # Add to the prime list
    return prime  # Return the list of prime numbers

# Example usage:
numbers = [1, 4, 6, 7, 13, 9, 67]
prime = filter_prime(numbers)
print(prime)  # Output: [7, 13, 67]
