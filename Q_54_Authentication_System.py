user_registred = {}

def register():
    #while True:

        print('=========Registration=========')

        username = input('Enter a UserName : ')
        password = input('Enter a Password : ')

        if username in user_registred:
            print('Invalid Username and Password Already Exists')
        else:
            user_registred[username] = password
            print('Registration Sucessfully')
            print(user_registred)

register()
                         #key       #values
       # user_registred[username] = password

def login():
    print('===========Login===========')

    username = input('Enter a username : ')
    password = input('Enter a Password : ')

    if username not in user_registred or user_registred[username] != password:
        print('Invalid UserName & Password Please try Again')
    else:
        print('Login SucessFully')

login()
