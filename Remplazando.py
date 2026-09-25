def replace_domain(email, old_domain, new_domain):
    # 1. Busca el dominio antiguo en el correo y lo reemplaza por el nuevo.
    domain_target = "@" + old_domain
    if domain_target in email:
        index = email.index(domain_target)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email


def anim():
    # 2. Métodos de búsqueda en texto (.index y 'in')
    animals = "lions tigers and bears"
    print(f"Posición de 'g': {animals.index('g')}")          # Posición 8
    print(f"Posición de 'bears': {animals.index('bears')}")  # Posición 17
    print(f"¿'horses' está en la cadena?: {'horses' in animals}")  # False
    print(f"¿'tigers' está en la cadena?: {'tigers' in animals}")  # True

    # 3. Mayúsculas y minúsculas (.upper y .lower)
    print("Mountains".upper())  # MOUNTAINS
    print("Mountains".lower())  # mountains

    answer = "YES"
    if answer.lower() == "yes":
        print("User said yes")

    # 4. Eliminar espacios sobrantes (.strip, .lstrip, .rstrip)
    print(repr(" yes ".strip()))   # 'yes' (quita espacios a ambos lados)
    print(repr(" yes ".lstrip()))  # 'yes ' (quita espacio a la izquierda)
    print(repr(" yes ".rstrip()))  # ' yes' (quita espacio a la derecha)

    # 5. Contar e inspeccionar textos (.count, .endswith, .isnumeric)
    texto = "The number of times e occurs in this string is 4"
    print(f"Cantidad de letras 'e': {texto.count('e')}")
    print(f"¿Termina en 'rest'?: {'Forest'.endswith('rest')}")

    print(f"¿'Forest' son solo números?: {'Forest'.isnumeric()}")
    print(f"¿'12345' son solo números?: {'12345'.isnumeric()}")

    # 6. Convertir texto a número entero y sumar
    print(f"Suma de textos convertidos: {int('12345') + int('54321')}")

    # 7. Unir (.join) y separar (.split) cadenas
    words = ["This", "is", "a", "phrase", "joined", "by", "spaces"]
    print(" ".join(words))

    dots = ["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]
    print("...".join(dots))

    print("This is another example".split())


# Un único punto de entrada para ejecutar todo en orden
if __name__ == "__main__":
    email = "user@olddomain.com"
    nuevo_correo = replace_domain(email, "olddomain.com", "newdomain.com")
    print(f"Correo actualizado: {nuevo_correo}")

    print("\n--- Pruebas de manipulación de texto ---")
    anim()

