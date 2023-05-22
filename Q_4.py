# Sum of three Digit
print('Program that will give you the sum of 3 digits')
while True:
    inp_1 = float(input('Enter First Number : '))
    inp_2 = float(input('Enter Second Number : '))
    inp_3 = float(input('Enter Third Number : '))

    add = inp_1 + inp_2 + inp_3

    print('Sum of Three Numbers You Entered = ', add)

    next = input('Lets Add More Number (yes/no)')

    if next == 'no':
        print('Programmed end')
        break
    else:
        continue
