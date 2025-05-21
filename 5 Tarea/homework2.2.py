# Cree un programa que use una lista para eliminar keys de un diccionario.

list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

user_data = dict(zip(list_a, list_b))

print (user_data)

# Cree un programa que use una lista para eliminar keys de un diccionario.
list_of_keys = ["access_level", "age"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}

deleted_item = employee.pop("age", "access_level")
deleted_access_level = employee.pop("access_level")
print(employee)
