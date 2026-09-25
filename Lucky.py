def lucky_number(name):
    # 1. Contamos las letras del nombre y las multiplicamos por 9.
    number = len(name) * 9

    # 2. Mostramos el nombre y su número de la suerte en pantalla.
    print(f"Hello {name}. Your lucky number is {number}")


if __name__ == "__main__":
    lucky_number("Kay")

