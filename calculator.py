from time import sleep as wait
class CR():

    def sum(a, b):
        return (a + b)

    def diff(a, b):
        return(a - b)

    c = str(input('What Operation Would You Like To Use: '))

    if c == 'Addition':
        a = int(input('Enter 1st number: '))
        b = int(input('Enter 2nd number: '))

        print(f'Sum of {a} and {b} is {sum(a, b)}')
    elif c == 'Subtraction':
        a = int(input('Enter 1st number: '))
        b = int(input('Enter 2nd number: '))

        print(f'Difference of {a} and {b} is {diff(a, b)}')