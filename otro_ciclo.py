from Operador_de_comparacion import product


def aristoteles():
    for x in range(5):
        print(x)

    friends = ["Taylor", "Alex", "Pat", "Eli"]
    for friend in friends:
        print("Hi" + friend)

    values = [23,52,59,37,48]
    sum = 0
    length = 0
    for value in values:
        sum += value
        length += 1
        print("Total sum:" + str(sum/length))

    product = 1
    for n in range(1,10):
        product = product * n

    print(product)

def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x, to_celsius(x))

for n in range(0, 11, 12):
    print(n)

for x in range(2, -2, -1):
    print(x)

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end="")
    print()



team = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in team:
    for away_team in team:
        if home_team != away_team:
            print(home_team +"vs" + away_team)

if __name__ == "__main__":
        to_celsius(100)
