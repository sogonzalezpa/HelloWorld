def wisteria():
    # 1. Creamos una lista (como una caja con varios juguetes adentro).
    # Guardamos 4 palabras separadas.
    palabras = ["Now", "we", "are", "cooking"]

    # 2. Unimos las palabras usando un espacio " " como pegamento.
    # El método .join() pega todo para formar una sola frase: "Now we are cooking"
    mensaje = " ".join(palabras)

    # 3. Mostramos la frase final en la pantalla.
    print(mensaje)

# Esta línea le dice a Python: "Si ejecutas este archivo directamente, ¡empieza aquí!"
if __name__ == "__main__":
    wisteria()