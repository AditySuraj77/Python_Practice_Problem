
sum = 0
while True:
    usr_input = input('Enter your price : ')

    if usr_input != 'q':
        sum += int(usr_input)
        print(sum)
    else:
        print('Close')
        break
