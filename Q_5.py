# Reversing Number digit
while True:

    num1 = int(input('Enter First Digit Number : '))
    num2 = int(input('Enter Second Digit Number : '))
    num3 = int(input('Enter Third Digit Number : '))
    num4 = int(input('Enter Fourth Digit Number : '))



    lst_num = list([num1,num2,num3,num4])

    #print(lst_num)

    rev = lst_num.copy()

    rev.reverse()
    #print(rev)

    if lst_num == rev:
        print('Palindrome')
    else:
        print('Not Palindrome')

    next = input('Do You Continue Programme (yes/no) : ')

    if next == 'no':
        print('Programmed End')
        break
    else:
        continue
