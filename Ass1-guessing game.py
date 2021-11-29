import random


def Number_Guess(num, guess):
    if 1 <= guess <= 100:
        print(f'Your guessed number is {guess}. The random number is {num}.')
        if guess != num:
            while True:
                if guess > num:
                    return 'The guessed number is greater than the random number!!!'
                elif guess < num:
                    return 'The guessed number is less than the random number!!!'
                # else:
                #     return 'Please try again'
        else:
            return 'You are absolutely correct!!!'
    elif guess==0:
        return 0
    else:
        return 'opps! Number outta range'


for i in range(10):
        number = random.randint(1, 100)
        guessed_number = int(input('Guess a number: '))

        G = Number_Guess(number, guessed_number)
        print(G)



# x = random.randint(1, 100)
# y = int(input('Guess a number: '))

# B = Number_Guess(x, y)
# print(B)
