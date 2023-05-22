''''
num = int(input('Enter a Numertor : '))
den = int(input('Enter a Denominator : '))

if num == 5 and den == 10:
    print(round(num/den,2))
elif num == 6 and den == 9:
    print(round(num/den,2))
else:
    print(round(num/den,2))

'''


import math

num = int(input("Enter the numerator: "))
den = int(input("Enter the denominator: "))

gcd = math.gcd(num, den)
simplified_num = num // gcd
simplified_den = den // gcd

print("The simplified fraction is: {}/{}".format(simplified_num, simplified_den))