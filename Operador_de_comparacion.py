def comparacion():
    # 1. ¿Es 40 (10 * 4) mayor que 37 (14 + 23)? -> True
    print(10 * 4 > 14 + 23)

    # 2. Imprime directamente el texto "tall < short" en la pantalla
    print("tall < short")


def product(a, b):
    # 3. Multiplica dos números y devuelve el resultado
    return a * b


def sum_values(a, b):
    # 4. Suma dos números y devuelve el resultado
    return a + b


def difference(a, b):
    # 5. Resta dos números y devuelve el resultado
    return a - b


def evaluar_condiciones():
    # 6. Evalúa dos comparaciones conectadas con 'and' (ambas deben ser verdaderas)
    # (5 >= 8) es Falso y (5 <= 12) es Verdadero -> False
    print((5 >= 2 * 4) and (5 <= 4 * 3))

    # 7. Evalúa condiciones con 'or' (al menos una debe ser verdadera)
    x = 3
    # (8 > 9) es Falso, pero (3 % 4 != 0) es Verdadero -> True
    if x + 5 > x**2 or x % 4 != 0:
        print("This comparison is True")

    # 8. Toma decisiones con if / elif / else
    number = 6
    if number * 2 < 14:  # 12 < 14 es Verdadero
        print((number * 6) % 3)  # 36 % 3 es 0
    elif number > 7:
        print(100 / number)
    else:
        print(7 - number)


def get_remainder(x, y):
    # 9. Calcula el residuo relativo de una división
    if x == 0 or y == 0 or x == y:
        remainder = 0
    else:
        remainder = (x % y) / y
    return remainder


# Punto de inicio que ejecuta todo de forma ordenada
if __name__ == "__main__":
    comparacion()

    # Cálculo del producto anidado: product(8, 15) -> 120
    print(product(product(2, 4), product(3, 5)))

    # Cálculo de diferencia de sumas: difference(4, 6) -> -2
    print(difference(sum_values(2, 2), sum_values(3, 3)))

    evaluar_condiciones()

    # Muestra el residuo de (10 % 3) / 3 -> 1 / 3 -> 0.3333...
    print(get_remainder(10, 3))