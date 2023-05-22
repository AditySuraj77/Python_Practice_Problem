

#    Calculating HCF and LCM in Pythonic Ways

import  math
print('Calculate LCM ')
def lcm(number1, number2):

    lcm= math.lcm(number1,number2)
    print(lcm)

user_num1 = int(input('Enter Your Number : '))
user_num2 = int(input('Enter Your Number : '))


lcm(user_num1,user_num2)


print('Calculate HCF ')
def hcf(number1,number2):
    hcf = math.gcd(number1,number2)
    print(hcf)

user_num1 = int(input('Enter Your Number : '))
user_num2 = int(input('Enter Your Number : '))

hcf(user_num1,user_num2)
