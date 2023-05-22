             # Code no. 1
'''
while True:

    user_1= int(input('Enter Age : '))
    user_2 = int(input('Enter Age : '))
    user_3 = int(input('Enter Age : '))

    if user_1>user_2 and user_3:
        print('Oldest Age is = ', user_1)
    elif user_2>user_2 and user_1:
        print('Oldest Age is = ',user_2)
    elif user_3>user_2 and user_1:
        print('Oldest Age is = ',user_3)
    else:
        print('Invalid Input')
'''


#                    code no. 2

while True:

    age_1 = int(input('Enter First Age : '))
    age_2 = int(input('Enter Second Age : '))
    age_3 = int(input('Enter Third Age : '))

    oldet_age = max(age_1,age_2,age_3)

    print('The Oldest Age is = ', oldet_age)

    next = input('If you continue prgramme (Y/N) : ')
    if next == 'N':
        print('Programmed End Thank You')
        break
    else:
        continue


