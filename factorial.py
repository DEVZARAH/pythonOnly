n = int(input('Enter a number: '))
x = 1
for i in range(1, n+1):
    x *= i


print(f'The factorial of {n} is {x}')
