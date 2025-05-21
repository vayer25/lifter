def mostrar_menu():
    print("\nSeleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Reiniciar (volver a 0)")
    print("6. Salir")

def obtener_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))  
        except ValueError:
            print("❌ Entrada no válida. Por favor, ingrese un número.")

resultado = 0  
reiniciar = True  

while True:
    print(f"\n📌 Número actual: {resultado}")  
    mostrar_menu()

    entrada = input("Ingrese el número de la operación (1-6): ").strip()

    try:
        opcion = int(entrada)  
        if opcion not in [1, 2, 3, 4, 5, 6]:
            raise ValueError  
    except ValueError:
        print("❌ Opción no válida. Debe ser un número entre 1 y 6.")
        continue  

    if opcion == 6:
        print("¡Gracias por usar la calculadora!")
        break


    if opcion == 5: 
        resultado = 0
        print("✅ Resultado reiniciado a 0.")
        reiniciar = True
        continue

    if reiniciar:
        num1 = obtener_numero("Ingrese el primer número: ")
        num2 = obtener_numero("Ingrese el segundo número: ")
        reiniciar = False
    else:
        num1 = resultado 
        num2 = obtener_numero("Ingrese el nuevo número: ")

    try:
        if opcion == 1:
            resultado = num1 + num2
        elif opcion == 2:
            resultado = num1 - num2
        elif opcion == 3:
            resultado = num1 * num2
        elif opcion == 4:
            if num2 == 0:
                raise ZeroDivisionError("❌ Error: No se puede dividir por cero.")
            resultado = num1 / num2

        print(f"✅ Nuevo número actual: {resultado}")

    except ZeroDivisionError as e:
        print(e)

    continuar = input("¿Desea realizar otra operación? (sí/no): ").strip().lower()
    if continuar not in ["sí", "si"]:
        print("¡Gracias por usar la calculadora!")
        break
