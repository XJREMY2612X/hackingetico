# 3. Entrada de edad validada[cite: 9]
def solicitar_edad():
    while True:
        try:
            edad = int(input("Introduce una edad válida (0-120): "))
            if 0 <= edad <= 120:
                return edad
            print("Fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Error: Debes introducir un número entero.")
