

# print * number of time user expect
'''
user = int(input('Enter a Row Number : '))

for i in range(1, user + 1):
    for j in range(0,i):
        print('*',end='')
    print('')'''

''''
user = int(input('Enter a Row Number : '))

for i in range(1, user + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()'''




user = int(input('Enter a Row Number : '))
number = 1

for i in range(1, user + 1):
    for j in range(1, i + 1):
        print(number, end=" ")
        number += 1
    print()