def main():
    try:
        num1 = int(input('Enter the first number'))
        pass
    except valueError:
        print('Make sure you entered in a number')

    try:
        num2 = int(input('Enter the second number'))
        pass
    except valueError:
        print('Make sure you entered in a number')

    calculate(num1, num2)

def calculate(num1, num2):
    if num1 > num2:
        print('Num 1 is bigger than num 2')
    elif num1 < num2:
        print('Num2 is bigger than num 1')
    elif num1 = num2:
        print('Num 1 is equal to num2')
