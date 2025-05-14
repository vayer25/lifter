# Cree una función que retorne la suma de todos los números de una lista.
# a. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
# b. [4, 6, 2, 29] → 41


def sum_list (list1, list2, list3, list4):
    return list1 + list2 + list3 + list4
result = sum_list (4,6,2,29)

print(result)


# this is other way as per chat gpt it says that it should be 

def sum_list(numbers):
    return sum(numbers)  # Usamos sum() para sumar todos los elementos de la lista

# Llamamos a la función pasando la lista como argumento
result = sum_list([4, 6, 2, 29])

print(result)  # Output: 41


#chat gpt mentioned Errores en tu código original:
# Recibía cuatro números en lugar de una lista (list1, list2, list3, list4).
# No funcionaría con listas más grandes (tendría que definir list5, list6, etc. manualmente).
# No era escalable, porque solo sumaba exactamente 4 valores.

