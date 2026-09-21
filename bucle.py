from subprocess import check_output


def intento():
    x= 0
    while x < 5:
        print("Not there yet, x=" + str(x))
        x = x + 1
    print("x=" + str(x))

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
        print("Done")


def attemps2(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
        print("Done")
def get_username():
    username = input("Enter your username: ")
    while not valid_username(username):
        print("Invalid username")
        username = get_username()
def valid_username(username):
    return len(username) > 0 and username.isalnum()




def my_variable():
    my_variable = 5
    while my_variable < 10:
        print("hello")
        my_variable = my_variable + 1


def xion():
    x = 1
    sum = 0
    while x < 10:
        sum = sum + x
        x = x + 1

    product = 1
    while x < 10:
        product = product + x
        x = x + 1

    print(sum,product)

def anaximandro():
    multiplier = 1
    result = multiplier * 5
    while result <= 50:
        print(result)
        multiplier += 1
        result = multiplier * 5
    print("Done")


def count_factors(given_number):
    factor = 1
    count = 1
    if given_number == 0:
        return 0

    while factor < given_number:
        if given_number % factor == 0:
            count += 1
        factor += 1
    return count


def addition_table(given_number):
    interated_number = 1
    my_sum = 1

    while interated_number <= 5:
        my_sum = given_number + interated_number
        if my_sum > 20:
            brea

        print(f"{given_number} + {interated_number} = {my_sum}")
        interated_number += 1


if __name__ == "__main__":
    addition_table(5)