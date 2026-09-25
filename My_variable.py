def my_variable():
    # 1. Guardamos el resultado de 3 * 5 en la variable (3 * 5 = 15)
    val = 3 * 5
    print(val)  # Imprime: 15

    # 2. ¿Es 15 igual a 3 * 5?
    print(val == 3 * 5)  # Imprime: True (Verdadero)

    # 3. ¿Es 11 mayor que 9 (3 * 3)?
    print(11 > 3 * 3)  # Imprime: True (Verdadero)

    # 4. ¿Es 2.0 (4 / 2) mayor que 4 (8 - 4)?
    print(4 / 2 > 8 - 4)  # Imprime: False (Falso)

    # 5. ¿Es 2.0 (4 / 2) menor que 4 (8 - 4)?
    print(4 / 2 < 8 - 4)  # Imprime: True (Verdadero)

    # 6. ¿Es 11 menor que 9 (3 * 3)?
    print(11 < 3 * 3)  # Imprime: False (Falso)

    # 7. ¿Es 24 (12 * 2) mayor o igual a 24?
    print(12 * 2 >= 24)  # Imprime: True (Verdadero)

    # 8. ¿Es 9.0 (18 / 2) mayor o igual a 15?
    print(18 / 2 >= 15)  # Imprime: False (Falso)

    # 9. ¿Es 24 (12 * 2) menor o igual a 30?
    print(12 * 2 <= 30)  # Imprime: True (Verdadero)

    # 10. ¿Es 15 menor o igual a 9.0 (18 / 2)?
    print(15 <= 18 / 2)  # Imprime: False (Falso)


# Punto de inicio del programa
if __name__ == "__main__":
    my_variable()