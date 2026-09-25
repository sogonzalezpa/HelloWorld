from Operador_de_comparacion import get_remainder


def Arquimedes():
   for x in range(25):
       print(x)
if __name__ == "__main__":
        Arquimedes()



def greet_friends(friends):
    if isinstance(friends, str):
        friends = [friends]
    for friend in friends:
        print("Hi " + friend)

greet_friends(["Taylor", "Luisa", "Jamaal", "Eli"])
greet_friends(["Barry"])


if __name__ == "__main__":
        greet_friends(["Barry"])




def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)





if __name__ == "__main__":
        greet_friends(["Barry"])


def M():
    for i in range(5):
        print(f"Iteracion {i}")
    for number in range(1, 6+1, 2):
        print(number * 3)
    for number in range(2, 8):
        print(number ** 2)

    for x in range(2):
        print("This is the outer loop iteration number " + str(x))
    for y in range(3 + 1):
        print("Inner loop iteration number " + str(y))
        print("Exit inner loop")

    for x in range(7):
        if x % 2 == 0:
             print(x)


    even_numbers = [x for x in range(7) if x % 2 == 0]
    print(even_numbers)


if __name__ == "__main__":
    M()


def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n - 1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result



if __name__ == "__main__":
    factorial(4)

def malveris():
    name = "Many"
    number = len(name) * 3
    print("Hello {}, your lucky number is {}".format(name, number))

    name = "Many"
    print("Your lucky number is {number}, {name}.".format(name=name, number=len(name) * 3))

    price = 7.5
    with_tax = price * 1.09
    print("Base price: $ (:.2f). With Tax: ${:.2f}".format(price, with_tax))

if __name__ == "__main__":
    malveris()

def to_celsius(x):
    return (x - 32) * 5 / 9

for x in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

if __name__ == "__main__":
    print (to_celsius(100))

def student_grade(name, grade):
    return "{} received {}% on the exam".format(name, grade)



if __name__ == "__main__":
    print(student_grade("Reed", 80))
    print(student_grade("Paige", 92))
    print(student_grade("Jesse", 85))

def lake ():
    print(len("abdce"))
    for c in "abcde":
        print(c)

    print("abc" in "abcde")
    print("def" in "abcde")

    print("AaBbcDdEe"[0:2])
    print("AaBbcDdEe"[2:])

    print("AaBbCcDdEe".lower())
    print("AaBbCcDdEe".upper())
    print(" Hello ".lstrip())
    print("  Hello ".rstrip())
    print(" Hello ".strip())

if __name__ == "__main__":
    lake()
#___________________________________________________________________________________________
def pencil ():
    test = "How much wood would a woodchuck chuck"
    print(test.count("wood"))

    print("12345".isnumeric())
    print("123.45".isnumeric())

    print("xyzzy".isalpha())
    print(test.split())

    test = "How-much-wood-would-a-woodchuck-chuck"
    print(test.split("-"))

    print(test.replace("wood", "plastic"))
    print("-".join(test.split()))


if __name__ == "__main__":
    pencil()


#______________________________________________________________________________________________________
def fruit_basket():
    basket = [
        ("Peaches", 3.0, 2.99),
        ("Pears", 5.0, 1.66),
        ("Plums", 2.5, 3.99)
    ]

    subtotal = 0.00
    for item in basket:
        fruit, weight, unit_price = item
        subtotal += (weight * unit_price)

    tax_rate = 0.06625
    tax_amt = subtotal * tax_rate
    total = subtotal + tax_amt

    print("Subtotal:", subtotal)
    print("Sales Tax:", tax_amt)
    print("Total:", total)

if __name__ == "__main__":
        fruit_basket()

#_______________________________________________________________________________________________________
def format_examples():
    # Variables de productos
    fruit = "peaches"
    weight = 3.0
    per_pound = 2.99

    # Variables de totales (calculadas para que el código funcione sin errores)
    subtotal = weight * per_pound
    tax_rate = 0.06625
    tax_amt = subtotal * tax_rate
    total = subtotal + tax_amt

    # Formato posicional básico
    output1 = "You are buying {} pounds of {} at {} per pound.".format(weight, fruit, per_pound)
    print(output1)

    # Formato usando índices explícitos {0}, {1}, {2}
    output2 = "{1} are {2} per pound, and you have {0} pounds of {1}.".format(weight, fruit, per_pound)
    print(output2)

    # Formato usando nombres de argumentos
    output3 = "{fruit} are {price} per pound, and you have {weight} pounds of {fruit}.".format(
        weight=weight, fruit=fruit, price=per_pound
    )
    print(output3)

    print()  # Salto de línea visual

    # Formato numérico con alineación y decimales
    print("Subtotal:     ${:10,.2f}".format(subtotal))
    print("Sales Tax:    ${:10,.2f}".format(tax_amt))
    print("Total:        ${:10,.2f}".format(total))


if __name__ == "__main__":
    format_examples()

#_______________________________________________________________________________________________________
def mirrored_string(my_string):
    # Declaración de variables para almacenar las letras
    forwards = ""
    backwards = ""

    # Recorremos cada carácter de la cadena original
    for character in my_string:
        # Solo procesamos si el carácter es una letra
        if character.isalpha():
            forwards += character
            backwards = character + backwards

    # Comparamos ambas cadenas convirtiéndolas a minúsculas
    if forwards.lower() == backwards.lower():
        return True
    return False


if __name__ == "__main__":
    print(mirrored_string("12 Noon"))  # Imprime: True
    print(mirrored_string("Was it a car or cat I saw"))  # Imprime: False
    print(mirrored_string("'eve, Madam Eve"))  # Imprime: True
#_____________________________________________________________________________________________
# Esta función convierte equivalencias de medidas. La salida se formatea
# como "x ounces equals y pounds", limitando y a 2 decimales.
def convert_weight(ounces):
    # Fórmula de conversión: 1 libra = 16 onzas
    pounds = ounces / 16

    # Se compone el resultado usando el método .format()
    result = "{} ounces equals {:.2f} pounds".format(ounces, pounds)
    return result


if __name__ == "__main__":
    print(convert_weight(12))    # Salida: 12 ounces equals 0.75 pounds
    print(convert_weight(50.5))  # Salida: 50.5 ounces equals 3.16 pounds
    print(convert_weight(16))    # Salida: 16 ounces equals 1.00 pounds

#________________________________________________________________________________________
# Esta función genera un nombre de usuario usando las primeras 3 letras del
# apellido de un usuario más su año de nacimiento.
def username(last_name, birth_year):
    # El método .format() usa las primeras 3 letras (posiciones [0:3]) del
    # apellido para el primer {} y el año de nacimiento para el segundo {}.
    return "{}{}".format(last_name[0:3], birth_year)


if __name__ == "__main__":
    print(username("Ivanov", "1985"))     # Muestra: "Iva1985"
    print(username("Rodríguez", "2000"))  # Muestra: "Rod2000"
    print(username("Deng", "1991"))       # Muestra: "Den1991"


def replace_date(schedule, old_date, new_date):
    # Calculamos la longitud de la fecha antigua
    p = len(old_date)

    # Verificamos si la agenda termina con la fecha antigua
    if schedule.endswith(old_date):
        # Recortamos el final y reemplazamos la fecha antigua por la nueva
        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)
        return new_schedule

    # Si no termina con la fecha antigua, retornamos el texto original
    return schedule


if __name__ == "__main__":
    print(
        replace_date(
            "Last year’s annual report will be released in March 2023",
            "2023",
            "2024",
        )
    )
    # Muestra: "Last year’s annual report will be released in March 2024"

    print(
        replace_date(
            "In April, the CEO will hold a conference",
            "April",
            "May",
        )
    )
    # Muestra: "In April, the CEO will hold a conference"

    print(
        replace_date(
            "The convention is scheduled for October",
            "October",
            "June",
        )
    )
    # Muestra: "The convention is scheduled for June"


def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""

    # Recorremos cada carácter de la frase
    for letter in input_string:
        # Si el carácter no es un espacio, lo agregamos
        if letter != " ":
            new_string = new_string + letter
            reverse_string = letter + reverse_string

    # Comparamos ambas cadenas en minúsculas
    if new_string.lower() == reverse_string.lower():
        return True

    return False


if __name__ == "__main__":
    print(is_palindrome("Never Odd or Even"))  # Devuelve: True
    print(is_palindrome("abc"))                # Devuelve: False
    print(is_palindrome("kayak"))              # Devuelve: True


def convert_distance(miles):
        km = miles * 1.6
        result = "{} miles equals {:.1f} km".format(miles, km)
        return result


if __name__ == "__main__":
        print(convert_distance(12))  # Muestra: 12 miles equals 19.2 km
        print(convert_distance(5.5))  # Muestra: 5.5 miles equals 8.8 km
        print(convert_distance(11))  # Muestra: 11 miles equals 17.6 km


def replace_ending(sentence, old, new):
    # Verifica si la subcadena 'old' está al final de la oración
    if sentence.endswith(old):
        # 'i' guarda la longitud de la subcadena
        i = len(old)
        # Recorta 'old' del final y pega 'new'
        new_sentence = sentence[:-i] + new
        return new_sentence

    # Si no coincide al final, devuelve la frase original sin cambios
    return sentence

if __name__ == "__main__":
    print(replace_ending("It's raining cats and cats", "cats", "dogs"))
    # Muestra: "It's raining cats and dogs"

    print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
    # Muestra: "She sells seashells by the seashore"

    print(replace_ending("The weather is nice in May", "may", "april"))
    # Muestra: "The weather is nice in May"

    print(replace_ending("The weather is nice in May", "May", "April"))
    # Muestra: "The weather is nice in April"


    