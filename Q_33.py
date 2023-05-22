

while True:
    print('This Programme will take your email and give username from extracting your email')
    def extract_username(user):

        # user_len = user[0:13]
        user_len = user.split('@')[0]

        print('User name is = ', user_len)

    user = input('Enter Email : ')

    extract_username(user)