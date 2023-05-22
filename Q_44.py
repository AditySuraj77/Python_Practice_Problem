# Using Index to Replacing Values
'''
l = ['Kohli','FAF','Bracewell','Rawat','Maxwell','Karan','Siraj']

l[4] = 'MahiPal'

print(l)'''

# USing for Loop to Replacing Values
'''
l = ['Kohli','FAF','Bracewell','Rawat','Maxwell','Karan','Siraj']

for i in range(len(l)):

    if l[i] == 'Kohli':
        l[i] = 'Virat'
        
    if l[i] == 'Rawat':
        l[i] = 'MahiPal'

print(l)'''


# Replace Values in a List using While Loop
'''
l = ['Kohli','FAF','Bracewell','Rawat','Maxwell','Karan','Siraj']

i = 0
while i < len(l):

    if l[i] == 'Bracewell':
        l[i] = 'Karthik'

    if l[i] == 'Karan':
        l[i] = 'Hasranga'

    i += 1

print(l)'''


# Replace Values in a List using Lambda Function

l = ['Kohli','FAF','Bracewell','Rawat','Maxwell','Karan','Siraj']

l = list(map(lambda x: x.replace, ('FAF', 'Du Plesis'),l))

print(l)








