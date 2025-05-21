#Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo
first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

for i in range (len(first_list)):
    print (first_list[i], second_list[i])

# cree un programa que itere e imprima un string letra por letra de derecha a izquierda 

my_string = 'pizza con piña'

for i in range (len(my_string) - 1, -1, -1):
    print (my_string[i])


for i in my_string [::-1]:
    print (i)


# cree un programa que intercambie el primer y ultimo elemento de una lista debe funcionar con listas de cualquier tamaño 


def swap_first_last(lst):
    if len(lst) > 1:  
        lst[0], lst[-1] = lst[-1], lst[0]  
    return lst

# Ejemplo de uso
my_list = [4, 3, 6, 1, 7]
print(swap_first_last(my_list))

#cree un programa que elimine todos los numero impares de una lista

my_item = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in my_item:
    if number % 2 == 0:
        print (number)

# Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto

numbers = []

for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numbers.append(num)

print("\nNúmeros ingresados:", numbers)
print("Número más alto:", max(numbers))
    
