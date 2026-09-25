def string():
    # Comparaciones de cadenas de texto (Strings)
    print("a string" == "a string")  # True  (cadenas idénticas)
    print("rabbit" != "frog")        # True  (cadenas diferentes)

    # Comparación de variables
    even_city = "Shangai"
    print(even_city != "Shangai")    # False (son iguales, por lo que no son diferentes)

    # Comparaciones de distintos tipos de datos (String vs Número)
    print("4+5" == 4 + 5)             # False (la cadena "4+5" no es igual al entero 9)
    print("three" == 3)              # False (la cadena "three" no es igual al entero 3)


if __name__ == "__main__":
    string()