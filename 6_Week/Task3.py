# Cree una función que retorne la suma de todos los números de una lista.
# a. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
# b. [4, 6, 2, 29] → 41


def sum_list (list1, list2, list3, list4):
    return list1 + list2 + list3 + list4
result = sum_list (4,6,2,29)

print(result)



def sum_list(numbers):
    return sum(numbers)  

result = sum_list([4, 6, 2, 29])

print(result)  # Output: 41




