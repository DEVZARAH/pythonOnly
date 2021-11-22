name = input('What is your name?: ')
age = int(input('Enter your age: '))
retirement_age = 65

if age >= 20 and age <= 50:
    print('You have a long way to retirement')
elif age >= 51 and age <= 60:
    print('You are close to retirement')
elif age >= 61 and age < 65:
    print('Get ready to retire')
else:
    print('Your service is no longer required')



