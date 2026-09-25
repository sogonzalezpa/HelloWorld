def septiembre():
    # 1. Recorremos la palabra "Hello" letra por letra y la imprimimos.
    saludo = "Hello"
    for letra in saludo:
        print(letra)


def diez():
    # 2. Imprimimos los números del 0 al 2 usando range(0, 3).
    for numero in range(0, 3):
        print("The next value is:", numero)


def anaxagoras_letras():
    # 3. Otra forma de recorrer la palabra "Hello" letra por letra.
    saludo = "Hello"
    for letra in saludo:
        print(letra)


def anaxarco():
    # 4. Imprimimos la posición (índice) de cada letra en "Hello" (del 0 al 4).
    saludo = "Hello"
    for posicion in range(len(saludo)):
        print(posicion)


def anaxipo():
    # 5. Recorremos e imprimimos "Hello" letra por letra usando un bucle 'while'.
    saludo = "Hello"
    posicion = 0
    while posicion < len(saludo):
        print(saludo[posicion])
        posicion += 1


def anaxagoras_cuadrados():
    # 6. Elevamos cada número de una lista al cuadrado usando comprensión de listas.
    numeros = [1, 2, 3, 4, 5]
    cuadrados = [x**2 for x in numeros]
    print(cuadrados)


# Un único punto de entrada principal para ejecutar todas las funciones
if __name__ == "__main__":
    septiembre()
    diez()
    anaxagoras_letras()
    anaxarco()
    anaxipo()
    anaxagoras_cuadrados()