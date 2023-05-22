# converting 2d list into 1d list
# using chain.from_iterables

#import numpy as np
'''
from itertools import chain
initial_list = [[1,2,3],
                [3,2,1],
                [3,4,3]]
#dim= np.ndim(initial_list) # Checkinh the dimension of list
#print(dim)

initial_list_1D_list = list(chain.from_iterable(initial_list))

print('1D List is = ',initial_list_1D_list)'''


# converting 2d list into 1d list
# using list comprehension
'''

initial_list = [[1,2,3],
                [3,2,1],
                [3,4,3]]
print('2D List is = ',str(initial_list))

initial_list_1D = [j for i in initial_list for j in i]

print('1D List is = ',str(initial_list_1D))'''

# converting 2d list into 1d list
# using functools.reduce
'''
from functools import reduce
initial_list = [[1,2,3],
                [3,2,1],
                [3,4,3]]
print('2D List is = ',str(initial_list))

flatten_list = reduce(lambda x,y : x+y ,initial_list)

print('1D List is = ',flatten_list)'''

# converting 2d list into 1d list using NumPy
'''
import numpy as np

initial_list = [[1,2,3],
                [3,2,1],
                [3,4,3]]
print('2D List is = ',str(initial_list))

flatten_list = list(np.concatenate(initial_list).flat)

print('1D List is = ',flatten_list)'''

initial_list = [[1,2,3],
                [3,2,1],
                [3,4,3]]
print('2D List is = ',str(initial_list))
one_D_List = []
for i in initial_list:
    one_D_List.extend(i)
print('1D List is = ',one_D_List)




