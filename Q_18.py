import random

'''
while True:
    print('This Programmed will be print sum of n number \nBut n numer == 10 then printing 55')
    def n_add_ten_logic(n_num):
        ran_dom = random.randint(0,100)
        add = n_num + ran_dom


        if n_num == 10:
            print('55')
        else :
            print(add)
    n_num = float(input('Enter Number : '))
    n_add_ten_logic(n_num)
'''

def sum_of_n_number(n):
    sum_of_number = 0
    for i in range(1, n+1):
        sum_of_number += i
    return sum_of_number
user_n = int(input('Enter N Number : '))

sum_result = sum_of_n_number(user_n)

print(sum_result)


