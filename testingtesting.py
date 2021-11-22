print('''
Hello Dearies!!!
    Welcome to Zahra's kitchen, I'm glad to have you here.
please kindly login to your account, to have a full access to these site,
new users can kindly create a new account.
    Thank you.
''')


def welcome_message_for_new_user(name):
    print(f'''Hi {name}!
We are delighted to have you. Kindly create a new account to get you acquinted
to the site

    Thank you {name}
    ''')


def welcome_message_for_old_user(name):
    print(f'''Hi {name}!
Welcome to Zahra's Kitchen, kindly login to continue
Thank you {name}
''')


def username():
    old_username = ['Dolapo123', 'Festus456', 'David789']
    new_username = []
    return None


def user_password(password):
    old_password = ['Dolapo123', 'Festus456', 'David789']
    new_password = []
    if password >= 10:
        if password.isidentifier():
            if password.isdecimal() >

        else:
            return 'Your password must contain only identifiers (letters, numbers and underscore(_))'

    else:
        return 'Your password must contain 10 or more characters'


def login():
    usr = input('Enter your username: ')
    pwd = input('Enter your password: ')
    if usr == user_username():
        if pwd == user_password():
            print('Access Granted!')


print("Hi, are you a new to Zahra's kitchen")
are_you_a_new_user = input()

if are_you_a_new_user == 'Yes':
    new_name = input('Enter your name: ')
    welcome_message_for_new_user(new_name)

elif are_you_a_new_user == 'No':
    old_name = input('Enter your name: ')
    welcome_message_for_old_user(old_name)