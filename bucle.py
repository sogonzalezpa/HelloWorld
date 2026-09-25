
def intento():
    # 1. Cuenta desde 0 hasta 4 imprimiendo un mensaje, y termina en 5.
    x = 0
    while x < 5:
        print(f"Not there yet, x={x}")
        x += 1
    print(f"x={x}")


def attempts(n):
    # 2. Cuenta los intentos del 1 hasta el número 'n' que le indiques.
    x = 1
    while x <= n:
        print(f"Attempt {x}")
        x += 1
    print("Done")


def valid_username(username):
    # 3. Comprueba que el usuario no esté vacío y solo tenga letras y números.
    return len(username) > 0 and username.isalnum()


def get_username():
    # 4. Pide un usuario en pantalla hasta que escribas uno válido.
    username = input("Enter your username: ")
    while not valid_username(username):
        print("Invalid username")
        username = input("Enter your username: ")
    return username


def my_variable():
    # 5. Imprime "hello" exactamente 5 veces (del 5 al 9).
    val = 5
    while val < 10:
        print("hello")
        val += 1


def xion():
    # 6. Suma los números del 1 al 9 y luego multiplica los números del 1 al 9.
    x = 1
    sum_val = 0
    while x < 10:
        sum_val += x
        x += 1

    x = 1
    product = 1
    while x < 10:
        product *= x
        x += 1

    print(sum_val, product)


def anaximandro():
    # 7. Muestra la tabla del 5 (5, 10, 15...) hasta llegar a 50.
    multiplier = 1
    result = multiplier * 5
    while result <= 50:
        print(result)
        multiplier += 1
        result = multiplier * 5
    print("Done")


def count_factors(given_number):
    # 8. Cuenta cuántos números dividen de forma exacta a un número dado.
    if given_number == 0:
        return 0

    factor = 1
    count = 0
    while factor <= given_number:
        if given_number % factor == 0:
            count += 1
        factor += 1
    return count


def addition_table(given_number):
    # 9. Suma un número con los valores del 1 al 5 (se detiene si la suma supera 20).
    iterated_number = 1
    while iterated_number <= 5:
        my_sum = given_number + iterated_number
        if my_sum > 20:
            break

        print(f"{given_number} + {iterated_number} = {my_sum}")
        iterated_number += 1


# Punto de inicio del programa
if __name__ == "__main__":
    addition_table(5)