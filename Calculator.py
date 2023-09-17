# This is the file in which I will create a calculator program which is capable of
# doing unlimited calculations.

# First of all let's define the operations we want to perform
# They are certainly +. -. *. /
# And the functions for these basic operations are
# add(), subtract(), multiply(), divide()

# Now let's code

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


# Now let's define the main calculator function that will ask the user for numbers and perform
# calculations on the backend

def calculator():
    num1 = int(input("Enter first number: \n"))
    should_continue = True

    while should_continue:
        operation_symbol = input("+, -, *, / \nPick an operation: ")
        num2 = int(input("Enter second number: \n"))
        calculate = operations[operation_symbol]
        answer = calculate(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        repeat = input("Type 'yes' if you want to perform another operation else 'no'.")

        if repeat == "yes":
            num1 = answer
            should_continue = True

        elif repeat == "no":
            should_continue = False
            break

        else:
            print("Please enter a valid input!")
            break


calculator()
