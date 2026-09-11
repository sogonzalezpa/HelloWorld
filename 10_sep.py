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





if __name__ == "__main__":
    hint_username("Sisi")

