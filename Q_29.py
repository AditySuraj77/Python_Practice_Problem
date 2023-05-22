'''
number = int(input("Enter a number: "))

reverse = 0
while number != 0:
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number = number // 10

print("The reverse of the number is:", reverse)
'''

'''
user_num = int(input('Enter Number : '))

reverse = 0

while user_num != 0 :
    remainder = user_num % 10
    reverse = reverse * 10 + remainder
    user_num = user_num // 10

print('Reversed Number is = ', reverse)
'''


user_num = int(input('Enter a Number : '))

user_str = str(user_num)
rev= user_str[::-1]
print('The Reverse of the Number is = ',rev)
