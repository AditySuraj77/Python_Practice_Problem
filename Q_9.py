
# Triangle condition

# 1.The sum of all the angles of a triangle (of all types) is equal to 180°.

''''
while True:

    print('Checking the number is ')


    num1 = float(input('Enter First Number : '))
    num2 = float(input('Enter Second Number : '))
    num3 = float(input('Enter Third Number : '))

    angle = (num1+num2+num3)

    if angle == 180:
        print('Triangle')
    else:
        print('Not Triangle')
'''

# 2.The sum of the length of the two sides of a triangle is greater than the length of the third side
'''
def checking_triangle():

    side1 = float(input('Enter the length of first side : '))
    side2 = float(input('Enter the length of first side : '))
    side3 = float(input('Enter the length of first side : '))

    if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
         print('The side can form Triangle')
    else:
         print('The side cannot form Triangle')

checking_triangle()
'''

# 3.The difference between the two sides of a triangle is less than the length of the third side.

def checking_triangle():

    side1 = float(input('Enter the length of first side : '))
    side2 = float(input('Enter the length of first side : '))
    side3 = float(input('Enter the length of first side : '))

    if side1 - side2 < side3 and side2 - side3 < side1 and side3 - side1 < side2:
         print('The side can form Triangle')
    else:
         print('The side cannot form Triangle')

checking_triangle()