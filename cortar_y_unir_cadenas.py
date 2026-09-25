def cleandro():
    # 1. Muestra letras específicas usando sus posiciones en la cadena.
    string1 = "Greetings, Earthlings"
    print(string1[0])      # G (primera letra)
    print(string1[4:8])    # ting (de la posición 4 a la 7)
    print(string1[11:])    # Earthlings (desde la posición 11 hasta el final)
    print(string1[:5])     # Greet (las primeras 5 letras)


def casandro(string1="¡Hola mundo desde Python"):
    # 2. Imprime los últimos 10 caracteres usando un índice negativo (-10).
    print(string1[-10:])   # desde Python


def lisandro():
    # 3. Salta de 2 en 2 caracteres o voltea la palabra al revés.
    string1 = "Greetings, Earthlings"
    print(string1[0::2])   # Geng,Erlns (salta una letra de por medio)
    print(string1[::-1])   # sgnilhtraE ,sgniteerG (al revés)


def leandro():
    # 4. Une tres cadenas de texto usando el signo '+'.
    print("Hello" + " " + "world")


def apolonio():
    # 5. Une una lista con espacios (" ".join) y usa f-strings para saludar.
    greeting = ["Hello", "world"]
    print(" ".join(greeting))

    name = "Alice"
    print(f"Hello, {name}!")


def aristoteles():
    # 6. Formatea un número e imprime el resultado directamente.
    phonenum = "2025551212"
    area_code = f"({phonenum[:3]})"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    print(f"{area_code} {exchange}-{line}")


def format_phone(phonenum):
    # 7. Formatea el número y lo 'devuelve' (return) para usarlo en otra parte.
    area_code = f"({phonenum[:3]})"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return f"{area_code} {exchange}-{line}"


# Punto de inicio que ejecuta todas las funciones en orden
if __name__ == "__main__":
    cleandro()
    casandro()
    lisandro()
    leandro()
    apolonio()
    aristoteles()

    resultado = format_phone("2025551212")
    print(resultado)