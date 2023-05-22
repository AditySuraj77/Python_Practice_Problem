
'''
import random

ran_dom = random.randint(1,100)

if ran_dom%2 != 0:
    lst_odd = ran_dom
    print(lst_odd)
else:
    print('')
'''

cont = 0
number = 1

while cont< 25:
    if number %2 != 0:
        print(number)
    else:
       print('')
    cont += 1
    number += 1