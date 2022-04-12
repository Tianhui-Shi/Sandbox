def main():
    #1.Basic list operations
    numbers = []
    for i in range(5):
        number = get_input()
        numbers.append(number)
    # The first number
    print("The first number is {}".format(numbers[0]))

    # The last number
    print("The last number is {}".format(numbers[-1]))

    # The smallest number
    print("The smallest number is {}".format(min(numbers)))

    # The largest number
    print("The largest number is {}".format(max(numbers)))

    # The average of the numbers
    print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))

    # 2.Woefully inadequate security checker
    user_name = str(input("What's you user name: "))
    username_checker(user_name)

def get_input():
    number = int(input("Number: "))
    return number

def username_checker(name):
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    if name in usernames:
        print("Access granted")
    else:
        print("Access denied")

main()