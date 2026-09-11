import pandas as pd

def main():
    u1 = [(65 + i, chr(65 + i)) for i in range(13)]    # A - M
    u2 = [(78 + i, chr(78 + i)) for i in range(13)]    # N - Z
    l1 = [(97 + i, chr(97 + i)) for i in range(13)]    # a - m
    l2 = [(110 + i, chr(110 + i)) for i in range(13)]  # n - z

    filas = []
    for i in range(13):
        filas.append([
            u1[i][0], u1[i][1],
            u2[i][0], u2[i][1],
            l1[i][0], l1[i][1],
            l2[i][0], l2[i][1]
        ])

    encabezados = pd.MultiIndex.from_tuples([
        ('Uppercase', 'Unicode #'), ('Uppercase', 'Character'),
        ('Uppercase', 'Unicode #'), ('Uppercase', 'Character'),
        ('Lowercase', 'Unicode #'), ('Lowercase', 'Character'),
        ('Lowercase', 'Unicode #'), ('Lowercase', 'Character')
    ])
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)

    print(encabezados)


if __name__ == "__main__":
    main()