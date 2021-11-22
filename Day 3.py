n = int(input('Enter a crazy number: '))



if n % 5 == 0:
    if n % 3 == 0:
        if n % 2 ==0:
            print('It is divisible by 5, 3, 2')
        else:
            print('It is divisible by 5 and 3')
    elif n % 2 == 0:
        print('it is divisible by 5, and 2')
    else:
        print('it is divisible by 5 only')

elif n % 3 == 0:
    if n % 2 == 0:
        print('It is divisible by 3 and 2')
    else:
        print('it is divisible by 3 only')

elif n % 2 == 0:
    print('it is divisible by 2 only')
else:
    print('There is no divisor')
