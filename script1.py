def main():
    print("hello girls")

def convert_seconds():
    seconds = int(input("Enter seconds: "))
    hours = seconds // 3600
    minutes = (seconds - hours *3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

if __name__ == "__main__":
    main()
    print(convert_seconds())


