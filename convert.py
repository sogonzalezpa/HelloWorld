def convert_seconds(seconds):
    # 1. Calculamos las horas enteras dividiendo por 3600 (los segundos que tiene 1 hora).
    hours = seconds // 3600

    # 2. Obtenemos el sobrante de las horas y lo dividimos por 60 para hallar los minutos.
    minutes = (seconds % 3600) // 60

    # 3. Guardamos los segundos finales que sobraron de las horas y minutos.
    remaining_seconds = seconds % 60

    # 4. Devolvemos los tres valores calculados.
    return hours, minutes, remaining_seconds


# Punto de inicio del programa
if __name__ == "__main__":
    # Probamos convirtiendo 3600 segundos
    hours, minutes, secs = convert_seconds(3600)
    print(f"Horas: {hours}, Minutos: {minutes}, Segundos: {secs}")

