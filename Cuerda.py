def combination():
    # 1. Concatenación y f-strings
    name = "Sasha"
    color = "Gold"
    print(f"Name: {name}, Favorite color: {color}")

    # 2. Repetición de cadenas
    print("example " * 3)

    # 3. Longitud de cadenas (len)
    pet = "loooooooooooong cat"
    print(f"Pet: {pet} (Length: {len(pet)})")

    # 4. Acceso por índices
    name = "Jaylen"
    print(f"First letter: {name[0]}")
    print(f"Second letter: {name[1]}")

    # 5. Índices negativos (desde el final)
    text = "Random string with a lot of characters"
    print(f"Last character: {text[-1]}")
    print(f"Penultimate character: {text[-2]}")

    # 6. Slicing (Rebanado)
    color = "Orange"
    print(f"Slice [1:4]: {color[1:4]}")

    fruit = "Pineapple"
    print(f"First 4 characters: {fruit[:4]}")
    print(f"From 4th character onward: {fruit[4:]}")

    # 7. Reemplazo de caracteres (Inmutabilidad)
    message = "A kong string with a silly typo"
    new_message = message[:2] + "l" + message[3:]
    print(f"Corrected message: {new_message}")

    # 8. Reasignación de variables
    message = "This is a new message"
    print(message)
    message = "And another one"
    print(message)


def search_and_check():
    # 9. Buscar posiciones con .index()
    pets = "Cats & Dogs"
    print(f"Posición de '&': {pets.index('&')}")
    print(f"Posición de 'C': {pets.index('C')}")
    print(f"Posición de 'Dog': {pets.index('Dog')}")
    print(f"Posición de la primera 's': {pets.index('s')}")

    # 10. Comprobar si un texto existe usando 'in'
    print(f"¿'Dragons' está en pets?: {'Dragons' in pets}")  # False
    print(f"¿'Cats' está en pets?: {'Cats' in pets}")        # True


# Punto de inicio que ejecuta todo en orden
if __name__ == "__main__":
    combination()
    search_and_check()