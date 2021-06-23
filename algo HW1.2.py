'''
Count odd and even numbers. Count odd and even digits of the whole number.
Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).
'''


def original_number(i):
    print('The number is ' + str(input_number))
    number_list = [int(x) for x in str(input_number)]
    print(f'The list from {i} is ' + str(number_list))

    for x in number_list:
        if x % 2 == 0:
            print(f'{x} is even')
        else:
            print(f'{x} is odd')


input_number = int(input('Input number: '))
original_number(input_number)
