'''
Find max number from 3 values, entered manually from a keyboard.
Example: 124, 21, 32. Result = 124.
'''


def numbers(x, y, z):
    if x > y and x > z:
        print(f'{x} is the greatest of the three numbers.')
    elif y > x and y > z:
        print(f'{y} is the greatest of the three numbers.')
    else:
        print(f'{z} is the greatest of the three numbers.')


n1 = int(input('Input number: '))
n2 = int(input('Input number: '))
n3 = int(input('Input number: '))

numbers(n1, n2, n3)
