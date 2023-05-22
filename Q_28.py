
# finding number of digit in provided by user
'''
def find_len(n):
    digit = len(str(n))
    print('Your Total Number of digit is = ',digit)

user_num = int(input('Enter a Number : '))

find_len(user_num)'''

# Find Factors of all number given by user


def cal_factor(number):
    factors = []

    for i in range(1, number+1):
        if number%i == 0:
            factors.append(i)
            print('Your Factors of ',number,'are',factors)
number = int(input('Enter a Number : '))
cal_factor(number)


