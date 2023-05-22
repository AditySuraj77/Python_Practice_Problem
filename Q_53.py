registred_User = {}


def registration():
    print('===========Registration===========')
    username = input('Enter a Username : ')
    password = input('Enter a Password : ')

    if username in registred_User:
        print('Username Already Exists, Please Try Again')
    else:
        registred_User[username] = password
        print('Registration Sucessfully ! ')


def login():
    print('===============Login==============')

    username = input('Enter a Username : ')
    password = input('Enter a Password : ')

    if username not in registred_User or registred_User[username] != password:
        print('Invalid Username And Password Please Try Again ! ')
    else:
        print('Login Sucessfully ! ')


def menu():
    while True:
        print('=======Menu======')
        print('Press 1 to Registration')
        print('Press 2 to Login')
        print('Press 3 to Quit')

        choice = int(input('Enter a Choice 1-3 : '))
        if choice == 1:
            registration()
        elif choice == 2:
            login()
        elif choice == 3:
            print('Good Bye')
            break
        else:
            print('Invalid Choice Please try Again')


menu()
