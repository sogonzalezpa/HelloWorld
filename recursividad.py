def factorial(n):
    # 1. Calcula el factorial usando recursividad (se llama a sí misma).
    if n < 2:
        return 1
    return n * factorial(n - 1)


def factorial_iterativo(n):
    # 2. Calcula el factorial usando un bucle for (ideal para números muy grandes).
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def is_power_of(number, base):
    # 3. Comprueba si un número es potencia de una base dividiendo recursivamente.
    if number < base:
        return number == 1
    return is_power_of(number / base, base)


def count_by_10(end):
    # 4. Genera una cadena contando de 10 en 10 desde el 0 hasta el límite 'end'.
    count = ""
    for number in range(0, end + 1, 10):
        count += str(number) + " "
    return count.strip()


def matrix(initial_number, end_of_first_row):
    # 5. Imprime una tabla de multiplicar en forma de matriz cuadrada.
    n1 = initial_number
    n2 = end_of_first_row + 1

    for row in range(n1, n2):
        for column in range(n1, n2):
            print(column * row, end=" ")
        print()


def cuenta_regresiva():
    # 6. Muestra una cuenta hacia atrás restando de 3 en 3 desde 18 hasta 0.
    starting_number = 18
    while starting_number >= 0:
        print(starting_number, end=" ")
        starting_number -= 3
    print()


def x_figure(salary):
    # 7. Cuenta cuántas cifras (dígitos) tiene un sueldo dividiendo entre 10.
    tally = 0
    if salary == 0:
        tally = 1

    while salary >= 1:
        salary = salary / 10
        tally += 1

    return tally


def elevator_floor(enter, exit_floor):
    # 8. Simula los pisos que recorre un ascensor al subir o bajar.
    floor = enter
    elevator_direction = ""

    if enter > exit_floor:
        elevator_direction = "Going down: "
        while floor >= exit_floor:
            elevator_direction += str(floor)
            if floor > exit_floor:
                elevator_direction += " | "
            floor -= 1
    else:
        elevator_direction = "Going up: "
        while floor <= exit_floor:
            elevator_direction += str(floor)
            if floor < exit_floor:
                elevator_direction += " | "
            floor += 1

    return elevator_direction


# Punto de inicio que ejecuta todas las funciones ordenadamente
if __name__ == "__main__":
    print(f"El factorial de 5 es: {factorial(5)}")
    print(f"Factorial de 100 (primeros dígitos): {str(factorial_iterativo(100))[:10]}...")

    print("\n--- Potencias ---")
    print(f"¿8 es potencia de 2?: {is_power_of(8, 2)}")
    print(f"¿64 es potencia de 4?: {is_power_of(64, 4)}")
    print(f"¿70 es potencia de 10?: {is_power_of(70, 10)}")

    print("\n--- Conteo de 10 en 10 ---")
    print(count_by_10(100))

    print("\n--- Matriz de multiplicación (1 al 4) ---")
    matrix(1, 4)

    print("\n--- Cuenta regresiva de 3 en 3 ---")
    cuenta_regresiva()

    print("\n--- Cifras del salario ---")
    print(f"The CEO has a {x_figure(2300000)}-figure salary.")

    print("\n--- Simulación del ascensor ---")
    print(elevator_floor(1, 4))
    print(elevator_floor(6, 2))