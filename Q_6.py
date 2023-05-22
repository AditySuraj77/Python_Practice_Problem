                 # Checking is the Number is Odd or Even

while True:

    user_num = int(input('Enter a Number : '))

    if user_num%2 == 0:
        print(user_num,'is Even Number')
    else:
        print(user_num,'is Odd Number')

    next = input('Press key  y to Close Programme and n to continue Programme : ')

    if next == 'y':
        print('Programe end')
    else:
        continue