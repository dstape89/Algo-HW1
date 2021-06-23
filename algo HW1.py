'''
Compute the sum of digits in all numbers from 1 to n. When a user enters a number n, find the sum of digits in all numbers from
1 to n.
Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
'''

def addition(n):
    result = 0

    if n != 0:
        for i in range(0, n+1):
            result += i
    print(f'The total of {n} is {result}')


number = int(input('Input number: '))
addition(number)

