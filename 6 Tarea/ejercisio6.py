# Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#a. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#b. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def sort_words (text):
    words = text.split("-")
    words_sorted = sorted (words)
    return "-".join(words_sorted)

text= "python-variable-funcion-computadora-monitor"

result = sort_words(text)

print(result)
    

# Explicación paso a paso:
# Convertir el string a una lista usando split("-"):  palabras = texto.split("-") # Resultado: ['python', 'variable', 'funcion', 'computadora', 'monitor']

# Ordenar la lista alfabéticamente usando sorted():  palabras_ordenadas = sorted(palabras) # Resultado: ['computadora', 'funcion', 'monitor', 'python', 'variable']

# Convertir la lista nuevamente a string usando "-".join(lista):  "-".join(palabras_ordenadas) # Resultado: "computadora-funcion-monitor-python-variable"

