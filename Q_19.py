import numpy as np
# Multiply without using *

def multiply(a,b):

    multiply = np.multiply(a,b)
    print(multiply)

num1 = float(input('Enter First Number to Multiply : '))
num2 = float(input('Enter Second Number to Multiply : '))

multiply(num1,num2)