#2. Experimente con el concepto de scope: a. Intente accesar a una variable definida dentro de una función desde afuera. b. Intente accesar a una variable global desde una función y cambiar su valor.

# A global variable is a variable that is declared outside of any function and can be accessed throughout the entire script, including inside functions. However, modifying a global variable inside a function requires special handling using the global keyword.

example_outside  = "Hello this is the second exercise"

def print_example_outside ():
    print(example_outside)

print_example_outside ()