from sys import exit


def require_admin(func):
    def wrapper(*args, **kwargs):

        limit = 3

        while True:
            password = "secret"
            user_input = input("Enter the password: ")

            if limit <= 1:
                print("\nOut of attempts! Access Denied")
                exit()

            elif user_input == password:
                print("\nAccess Granted\n")
                break

            else:
                limit -= 1
                print(f"\nIncorrect Password: Attempt(s) remaining: {limit}\n")
                continue

        result = func(*args, **kwargs)

        return result

    return wrapper


@require_admin
def add(a, b):
    return a + b


# print(add(1, 2))


def require_admin_2(func):
    def wrapper(*args, **kwargs):
        pin = 1909
        limit = 3
        while limit > 0:
            try:
                user_input = int(input("Enter the pin: "))

            except ValueError:
                print("\nPlease enter a numeric value\n")
                continue

            if user_input == pin:
                print("\nAccess Granted\n")
                return func(*args, **kwargs)

            else:
                limit -= 1
                print(f"\nTry again! Attempts Remaining {limit}\n")

        print("\nAccess Denied! Out of attempts")
        exit()

    return wrapper


@require_admin_2
def sub(a, b):
    return a - b


print(sub(2, 1))