
# Integer to strings

'''
userInput = int(input('Enter a Number : '))
print(userInput,'Type before conversion = ',type(userInput))

userInput_str = str(userInput)

print(userInput_str,'Type After conversion = ',type(userInput_str))
'''


# Print The Shape of Matrix

import  numpy as np

mat_rics = [ [1,2,3],
             [3,2,1],
             [2,4,6]]

shape = np.shape(mat_rics)
print('Shape of Matrics is = ',shape)



'''
user = float(input('Enter a Number two Converting a List : '))
list_list = list([user])
con_lst = np.asarray(list_list)
print(type(con_lst))'''

# 2 Matrics Multiplication

mat_rics1 = [[1,2,3],
             [3,2,1],# 3 X 3
             [2,4,6]]


mat_rics2 = [[1,2,3],
             [3,2,1], # 3X3
             [2,4,6]]


result = np.dot(mat_rics1,mat_rics2)

for r in result:
    print(r)