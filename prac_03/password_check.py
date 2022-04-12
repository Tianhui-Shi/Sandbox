"""Module docstring"""


# imports
# CONSTANTS

def main():
    MIN_LENGTH = int(input("PLease input min digits of password: "))
    password = get_password(MIN_LENGTH)
    asterisks(password)

def get_password(MIN_LENGTH):
    password = input("Please input password with {} digits".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        print("Too short \n")
        password = input("Input your password at least {} digits".format(MIN_LENGTH))
    return password

def asterisks(password):
    print('*' * len(password))

main()