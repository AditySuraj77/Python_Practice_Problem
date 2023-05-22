'''
num1 = float(input('Enter First Number : '))
num2 = float(input('Enter Second Number : '))
num3 = float(input('Enter Third Number : '))

num1_square = pow(num1,2)
num2_square = pow(num2,2)
num3_square = pow(num3,2)

print(num1_square+num2_square+num3_square)
'''

def square_of_digit(number):
   sum_of_square  = 0

   for digit in str(number):
       square = int(digit)**2
       sum_of_square += square
       return sum_of_square

number = int(input('Enter a Three Digit Number : '))

if number>=100 and number <=999:
    result = square_of_digit(number)
    print('The sum square digit : ',result)
else:
    print('Invalid Input')




'''
# Simple Logic
number = int(input('Enter three digit number : '))

sum_of_square = 0

for digit in str(number):
    square = int(digit)**2
    sum_of_square += square

print(sum_of_square)
'''

