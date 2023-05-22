

def swap_number(a,b):
    print('Before swap Number')
    print('a = ',a)
    print('b = ',b)

    a,b = b,a

    print('After swap Number')
    print('a = ',a)
    print('b = ',b)

f_num = float(input('Enter First Number : '))
s_num = float(input('Enter Second Number : '))

swap_number(f_num,s_num)