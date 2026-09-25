def to_celsius(fahrenheit):
    # Convierte grados Fahrenheit a Celsius usando la fórmula matemática.
    return (fahrenheit - 32) * 5 / 9


def aristoteles():
    # 1. Cuenta del 0 al 4 usando range(5).
    print("--- Contar del 0 al 4 ---")
    for numero in range(5):
        print(numero)

    # 2. Saluda a cada amigo de la lista agregando un espacio correcto.
    print("\n--- Saludar amigos ---")
    amigos = ["Taylor", "Alex", "Pat", "Eli"]
    for amigo in amigos:
        print(f"Hi {amigo}")

    # 3. Suma números de una lista y calcula el promedio paso a paso.
    print("\n--- Calcular suma y promedio ---")
    valores = [23, 52, 59, 37, 48]
    suma_total = 0
    cantidad = 0
    for valor in valores:
        suma_total += valor
        cantidad += 1
        promedio = suma_total / cantidad
        print(f"Suma actual: {suma_total} | Promedio actual: {promedio:.2f}")

    # 4. Multiplica los números del 1 al 9 (1 * 2 * 3 * ... * 9).
    print("\n--- Multiplicación acumulada (1 al 9) ---")
    producto = 1
    for numero in range(1, 10):
        producto *= numero
    print(f"Resultado final: {producto}")


def conversor_temperaturas():
    # 5. Muestra una tabla de temperaturas saltando de 10 en 10 del 0 al 100.
    print("\n--- Tabla Fahrenheit a Celsius ---")
    for fahrenheit in range(0, 101, 10):
        celsius = to_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {celsius:.2f}°C")


def trucos_de_conteo():
    # 6. Intenta contar de 12 en 12 del 0 al 11 (solo alcanza a mostrar el 0).
    print("\n--- Bucle con paso gigante ---")
    for numero in range(0, 11, 12):
        print(numero)

    # 7. Cuenta regresiva hacia atrás desde 2 hasta -1.
    print("\n--- Cuenta regresiva ---")
    for numero in range(2, -2, -1):
        print(numero)


def fichas_domino():
    # 8. Genera todas las fichas del juego de dominó del 0 al 6 sin repetir.
    print("\n--- Fichas de Dominó ---")
    for lado_izq in range(7):
        for lado_der in range(lado_izq, 7):
            print(f"[{lado_izq}|{lado_der}]", end="")
        print()


def torneo_equipos():
    # 9. Combina 4 equipos para armar partidos (evitando que jueguen contra sí mismos).
    print("\n--- Partidos del Torneo ---")
    equipos = ["Dragons", "Wolves", "Pandas", "Unicorns"]
    for local in equipos:
        for visitante in equipos:
            if local != visitante:
                print(f"{local} vs {visitante}")


# Este es el punto de inicio que ejecuta todas las tareas en orden
if __name__ == "__main__":
    aristoteles()
    conversor_temperaturas()
    trucos_de_conteo()
    fichas_domino()
    torneo_equipos()


