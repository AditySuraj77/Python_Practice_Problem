# Union And Intersection using set method

'''
lst_1 = [1,2,3,4,5,0]
lst_2 = [6,7,8,9,10,0]

set_1 = set(lst_1)
set_2 = set(lst_2)

#print(type(set_1))
#print(type(set_2))

union = set_1.union(set_2)
intersection = set_2.intersection(set_1)
print('The Union of Set = ',list(union))
print('The Intersection of Set = ',list(intersection))'''

# Intersection without using set method
lst_1 = [1, 2, 3, 4, 5, 0]
lst_2 = [6, 7, 8, 9, 10, 0]

lst_3 = [value for value in lst_1 if value in lst_2]
print('Union of List Without using Set Method = ', lst_3)

lst_1 = [1, 2, 3, 4, 5, 0]
lst_2 = [6, 7, 8, 9, 10, 0]

lst_3 = []

for i in (lst_1, lst_2):
    lst_3.extend(i)

print('Intersection of List Without using Set Method = ', lst_3)
