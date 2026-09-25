import pandas as pd


def main():
    # 1. Creamos 4 listas dividiendo el alfabeto en bloques de 13 letras.
    # Usamos chr() para convertir el código numérico (Unicode) en su letra correspondiente.
    u1 = [(65 + i, chr(65 + i)) for i in range(13)]   # Mayúsculas A-M (65 a 77)
    u2 = [(78 + i, chr(78 + i)) for i in range(13)]   # Mayúsculas N-Z (78 a 90)
    l1 = [(97 + i, chr(97 + i)) for i in range(13)]   # Minúsculas a-m (97 a 109)
    l2 = [(110 + i, chr(110 + i)) for i in range(13)] # Minúsculas n-z (110 a 122)

    # 2. Juntamos las 4 secciones en cada fila para ponerlas lado a lado (13 filas en total).
    filas = [
        [
            u1[i][0], u1[i][1],  # Número y letra de A-M
            u2[i][0], u2[i][1],  # Número y letra de N-Z
            l1[i][0], l1[i][1],  # Número y letra de a-m
            l2[i][0], l2[i][1],  # Número y letra de n-z
        ]
        for i in range(13)
    ]

    # 3. Creamos un título de doble piso para la tabla (nivel superior y nivel inferior).
    columnas = pd.MultiIndex.from_tuples([
        ('Uppercase (A-M)', 'Unicode #'), ('Uppercase (A-M)', 'Character'),
        ('Uppercase (N-Z)', 'Unicode #'), ('Uppercase (N-Z)', 'Character'),
        ('Lowercase (a-m)', 'Unicode #'), ('Lowercase (a-m)', 'Character'),
        ('Lowercase (n-z)', 'Unicode #'), ('Lowercase (n-z)', 'Character'),
    ])

    # 4. Construimos la tabla de datos organizada (DataFrame).
    df = pd.DataFrame(filas, columns=columnas)

    # Configuración para que la tabla no se corte al mostrarla en pantalla.
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)

    # 5. Imprimimos la tabla completa sin el contador lateral de filas.
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()