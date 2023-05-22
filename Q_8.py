
#              Calculating the distance between two coordinates points
import math

# Find the Euclidean Distance 1D
'''
p_1 = float(input('Enter Number : '))
p_2 = float(input('Enter Number : '))


def eculidian_distances(p_1,p_2):
    distances = (p_1 - p_2)**2
    sqtr = math.sqrt(distances)
    print(sqtr)
eculidian_distances(p_1,p_2)
'''

# Find the Euclidean Distance 2D
x_1 = float(input('Enter Number : '))
y_1 = float(input('Enter Number : '))
x_2 = float(input('Enter Number : '))
y_2 = float(input('Enter Number : '))


def eculidian_distances(x_1,y_1,x_2,y_2):
    distances = (x_1 - y_1)**2 + (x_2 - y_2)**2
    sqtr = math.sqrt(distances)
    print(sqtr)
eculidian_distances(x_1,y_1,x_2,y_2)

