def comparacion():

    print(10*4 > 14+23)

    print("tall < short")

def product(a,b):
    return (a*b)

print(product(product(2,4), product(3,5)))

def difference(a,b):
    return (a-b)

def sum(a,b):
    return (a+b)
print(difference(sum(2,2), sum(3,3)))
print((5 >= 2*4) and (5 <= 4*3))

x = 3
if x+5 >x**2 or x % 4 != 0:
    print("This comparison is True")

number = 6
if number * 2 < 14:
    print(number * 6 % 3)

elif number > 7:
    print(100 / number)
else: print(7 - number)

def get_remainder(x ,y):
    if x == 0 or y == 0 or x == y:
        remainder = 0
    else:
        remainder = (x % y) / y
    return remainder
print(get_remainder(10,3))

if __name__ == "__main__":
    comparacion()