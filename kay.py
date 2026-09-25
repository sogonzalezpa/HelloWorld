def main():
    # 1. Guardamos el nombre "Kay" en la variable 'name'
    name = "Kay"

    # 2. Contamos cuántas letras tiene "Kay" (3 letras) y lo multiplicamos por 9 (3 * 9 = 27)
    number = len(name) * 9

    # 3. Usamos una f-string para armar la frase de forma limpia y con los espacios correctos
    print(f"Hello {name}, your lucky number is {number}")


if __name__ == "__main__":
    main()




