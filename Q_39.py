# method one to remove duplicate are List comprehension
'''
userInput = input('Enter a List of Item : ')

print(userInput)

res = []
[res.append(x) for x in userInput if x not in res]

print(res)

'''

# Set are not including duplicate so we can take input from user and typecast in set to remove duplicates
'''
userInput = input('Enter a List of Item : ')

print(userInput)

rem_dup = [*set(userInput)]

print(str(rem_dup))'''

# Python 3 code to demonstrate
# removing duplicated from list
# using collections.OrderedDict.fromkeys()
'''
from collections import  OrderedDict

userInput = input('Enter a List of Item : ')

print('Your List of item = ' + str(userInput) )

res = list(OrderedDict.fromkeys(userInput))

print('After Removinf Duplicate From YOur List of Item = ' + str(res))'''



# Using Not in Operater to removing Duplicates

userInput = input('Enter a List of Item : ')

print('Your List of item = ' + str(userInput) )
res = []
for i in userInput:
    if i not in res:
        res.append(i)

print('After Removinf Duplicate From YOur List of Item = ' + str(res))

