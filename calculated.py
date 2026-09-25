import math


def calculate_circle_area(diameter):
    # 1. Calculamos el radio del círculo (el radio es exactamente la mitad del diámetro).
    radius = diameter / 2

    # 2. Aplicamos la fórmula del área del círculo: Pi multiplicado por el radio al cuadrado (π * r²).
    area = math.pi * (radius**2)

    # 3. Mostramos el resultado del área en la pantalla.
    print(area)


# Esta línea le dice a Python: "Si ejecutas este archivo directamente, ¡empieza aquí!"
if __name__ == "__main__":
    calculate_circle_area(1)
