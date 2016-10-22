"""This is the entry point of the program."""


def basic_calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    if operation == 'subtract':
        return num1 - num2
    if operation == 'multiply':
        return num1 * num2
    if operation == 'divide':
        return num1 / num2
    else:
        return 'Invalid operation'
        

        

