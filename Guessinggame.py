import random
for i in range(10):
    user_input=int(input("Enter a number;"))
    random_number=random.randint(1,10)
    if user_input== random_number:
        print(f"Your guess is {user_input} and the random number is {random_number}")
        print("Welldone")

    else:
        print(f"Your guess is {user_input} and the  random number is {random_number}")
        print("Try again")