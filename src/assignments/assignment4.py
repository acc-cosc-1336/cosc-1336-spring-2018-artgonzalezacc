def sample_function(value):
    '''
    This is just a sample function, you'll find a test_sample_one test case in test_assign4.py
    DO NOT CHANGE THE CODE IN THIS FUNCTION
    :param value:
    :return: return the given value
    '''
    return value

def factorial(number):
    '''
    Given a number return its factorial using a for loop.
    A factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.
    :param number: A number greater than 0
    :return: the factorial of a number
    Using a for loop implement the following, the factorial function should
    work for any number.
    1 * 2 = 2
    2 * 3 = 6
    6 * 4 = 24
    24 * 5 = 120

    WRITE CODE AFTER THREE QUOTES BELOW
    '''

    product = 1

    for n in range(number):
        product = product * (n + 1)

    return product


def main():#void function
    '''
    Create a loop that will run until the user doesn't type the letter 'y'

    Capture one number from the keyboard and validate for a range between 1 and 10.
    Call the factorial function.
    Save the result to a variable.
    Print the variable value.

    Ask the user if they want to continue.

    TO RUN YOUR PROGRAM GO TO IN PYTHON IDLE RUN->RUN MODULE.
    IN THE PYTHON SHELL TYPE main()

    DON'T ADD A RETURN STATEMENT TO THIS FUNCTION
    '''
    keep_going = 'y'

    while keep_going == 'y':

        num = int(input("Enter number 1-20: "))

        while num < 1 or num > 20:
            print('Invalid number range is 1-20...')
            num = int(input("Enter number 1-20: "))

        result = factorial(num)
        print(result)

        keep_going = input("Type y to continue other key to exit...: ")

