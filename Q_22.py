'''
from itertools import combinations

numbers = [1, 2, 3, 4]

print("All unique combinations of", numbers, "are:")

for r in range(1, len(numbers) + 1):
    combinations_list = list(combinations(numbers, r))
    for combination in combinations_list:
        print(combination)
'''
# while loop
'''
i = 0

while i < 10:
    print('Hello')
    i += 1
    '''
'''
i = 0

while i < 10:
    print(i)
    if i == 6:
        break
    i += 1
    '''
'''
i = 0

while i < 10:
    i += 1

    if i < 7:
        continue
    print(i)
'''
'''
i = 0

while i < 10:
    print(i)
    i += 1
else:
    print('i is no longer than 10')
    '''

# For Loop Revision
'''
fruits = ['apple','banana','orange']
for i in fruits:
    print(i)
'''
'''
for x in 'banana':
    print(x)
'''
'''
fruits = ['apple','banana','orange']
for i in fruits:
    if i == 'banana':
        break
    print(i)
'''

'''
fruits = ['apple','banana','orange']
for i in fruits:
    if i == 'banana':
        continue
    print(i)
'''

#for x in range(5):
   # print(x)

#for x in range(2,9):
 #   print(x)

#for i in range(0,50,5):
 #   print(i)

'''

for i in range(5):
    print(i)
else:
    print('NO')
'''
'''
for i in range(5):

    if i == 6: break
    else:
        print('Anyway')
'''