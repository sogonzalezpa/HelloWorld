def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    else:
        print("Valid username.")

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def is_positive(number):
  if number > 0:
    return True
  else:
    return False


def hind_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    else:
        if len(username) == 15:
            print("Valid username. Must be at least 15 characters long.")
        else:
            print("Invalid username.")

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    elif len(username) > 15:
        print("Invalid username. Must be at least 15 characters long.")
    else:
        print("Valid username.")




if __name__ == "__main__":
    hint_username("Sisi")

