def hint_username(username):
    """Valida que el nombre de usuario tenga entre 3 y 15 caracteres."""
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    elif len(username) > 15:
        print("Invalid username. Must be 15 characters or fewer.")
    else:
        print("Valid username.")


def is_even(num):
    """Retorna True si el número es par, False de lo contrario."""
    return num % 2 == 0


def is_positive(number):
    """Retorna True si el número es positivo, False de lo contrario."""
    return number > 0


if __name__ == "__main__":
    hint_username("Sisi")