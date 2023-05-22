# Swapping Variable
    #                  Code no.1

'''
first_num = int(input('Enter First Number : '))
second_num = int(input('Enter Second Number : '))

var_1 = first_num
var_2 = second_num

print('Before Swap the number ', 'First_number =',var_1,',','Second_number =',var_2)

First_number = var_2
Second_Number = var_1
print('After Swap the number')

user_type_1= input('Type the F: ')
if user_type_1 == 'F':
    print('After swapping First_Number : ', First_number)
user_type_2 = input('Type the S : ')
if user_type_2 == 'S':
    print('After swapping Second_Number : ', Second_Number)
'''




#                                  Swapping Numbers

num1 = float(input('Enter First Number : '))
num2 = float(input('Enter Second Number : '))

print('Before Swaping the Number')
print('Number1 = ',num1)
print('Number2 = ',num2)

# Swapping the numbers using a temporary variable
temp = num1
num1 =num2
num2 = temp

print('After Swaping the Number')

print('Number1',num1)
print('Number2',num2)
