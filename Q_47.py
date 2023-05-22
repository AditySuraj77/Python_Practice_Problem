
# Extract max value from Matrix
'''
arr = [[3, 4, 1, 8],
       [1, 4, 9, 11],
       [76, 34, 21, 1],
       [2, 1, 4, 5]]

for i in arr:
    print(max(i))'''

# Extract max value from Matrix using Map()
'''
def max_valu(matrix):
    max_val = list(map(lambda x: max(x),matrix))
    return max_val

arr = [[3, 4, 1, 8],
       [1, 4, 9, 11],
       [76, 34, 21, 1],
       [2, 1, 4, 5]]

max_values = max_valu(arr)
print(max_values)'''

import numpy as np

arr = [[3, 4, 1, 8],
       [1, 4, 9, 11],
       [76, 34, 21, 1],
       [2, 1, 4, 5]]

max_elemnt = lambda arr: [print(np.max(row),end=' ') for row in arr]

max_elemnt(arr)






