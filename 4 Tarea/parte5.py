total_de_notas = int(input("Ingrese la cantidad de notas: "))


contador_de_nota = 1
nota_actual = 0 
cantidad_de_notas_aprobadas = 0
cantidad_de_notas_desaprobadas =0
promedio_de_notas_aprobadas = 0
promedio_de_notas_desaprobadas = 0
promedio_de_notas_total = 0

while contador_de_nota <= total_de_notas:
    # Mostrar mensaje e ingresar la nota
    nota_actual = int(input(f"Ingrese la nota número {contador_de_nota}: "))
 

    if nota_actual < 70:
        cantidad_de_notas_desaprobadas += 1
        promedio_de_notas_desaprobadas += nota_actual
    else:
        cantidad_de_notas_aprobadas += 1
        promedio_de_notas_aprobadas += nota_actual

    promedio_de_notas_total += nota_actual / total_de_notas

    contador_de_nota += 1

if cantidad_de_notas_desaprobadas > 0:
    promedio_de_notas_desaprobadas /= cantidad_de_notas_desaprobadas
else:
    promedio_de_notas_desaprobadas = 0

if cantidad_de_notas_aprobadas > 0:
    promedio_de_notas_aprobadas /= cantidad_de_notas_aprobadas
else:
    promedio_de_notas_aprobadas = 0

print("El estudiante tiene esta cantidad de notas aprobadas")
print(cantidad_de_notas_aprobadas)

print("Este es el promedio de notas aprobadas")
print(promedio_de_notas_aprobadas)

print("El estudiante tiene esta cantidad de notas desaprobadas")
print(cantidad_de_notas_desaprobadas)

print("Este es el promedio de notas desaprobadas")
print(promedio_de_notas_desaprobadas)

print("Este es el promedio total de notas")
print(promedio_de_notas_total)
