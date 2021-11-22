list_of_usernames = ['Dolly', 'Fest', 'David']
list_of_passwords = ['Dollop_123', 'Fests_456', 'David_789']


def welcome_message():
    return """
************************************************************************************************
**   Hello Dearies!!!                                                                         **
**     Welcome to Zahra's kitchen, I'm glad to have you here.                                 **
**   please kindly login to your account, to have a full access to these site,                **pyth
**   new users can kindly create a new account and then sign                                  **
**   Thank you.                                                                               **
************************************************************************************************
    """


def welcome_message_for_new_user():
    print("""
*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#* 
#*                                                                                           *#   
*#  Hi, !!!                                                                                  #*
#*     We are delighted to have you. kindly login to continue to your newly created account. *#
*#  Thank you.                                                                               #*
#*                                                                                           *#
*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#* 
    """)


def welcome_message_for_old_user():
    print("""
*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#* 
#*                                                                                           *#   
*#  Hi, !!!                                                                                  #*
#*     Yeah!!! its Zahra's Kitchen you're in the right place.                                *#
*#  Thank you.                                                                               #*
#*                                                                                           *#
*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#* 
    """)


def sign_in():
    while True:
        username = input("Enter your username: ")
        if username not in list_of_usernames:
            continue

        else:
            break
    for i in range(5):
        password = input("Enter your password: ")
        if password in list_of_passwords:
            username_index = list_of_usernames.index(username)
            password_index = list_of_passwords.index(password)
            if username_index == password_index:
                print("Access Granted!")
                welcome_message_for_old_user()
                break
            else:
                print("Invalid Password!!! Kindly re-enter your password")
        else:
            print("Kindly re-enter your password")


def sign_up():
    check_username()
    welcome_message_for_new_user()
    print("Kindly Login to continue")
    sign_in()


def check_username():
    username = input('Kindly enter a username: ')

    while True:
        if username in list_of_usernames:
            print("Username already in use!")
            input('Kindly enter a username: ')
        else:
            list_of_usernames.append(username)
            print(list_of_usernames)
            password = input("Enter a password: ")

            while not check_password(password):
                password = input("Enter a password: ")
            check_password(password)
        break


def check_password(password):
    while True:
        if len(password) < 10:
            print("Password must contain at least 10 character")
            return False
        if not password.isidentifier():
            print("Password can only accept letters, digits and '_'")
            return False
        if '_' not in password:
            print("Password must contain '_'")
            return False
        if password.count('_') > 1:
            print("Password must have only one '_' ")
            return False
        sums = 0
        for s in password:
            if s.isdigit():
                sums += len(s)
        if sums < 2:
            print("Password must contain 2 or more digits")
            return False
        print("Account Created!")
        list_of_passwords.append(password)
        print(list_of_passwords)
        return True

welcome_message()
print("Enter '1' to login and '2' to signup: ")
response = int(input())
if response == 1:
    sign_in()
elif response == 2:
    sign_up()
else:
    print('Invalid selection')
