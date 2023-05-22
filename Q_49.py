# Sorting a List
'''
my_list = [5,3,2,5,4,7,8,6,7,-1,-2,-5,-7]
new_list = []

while my_list:
    min = my_list[0]
    for x in my_list:
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)
print('Sorted List',new_list)'''

# List to dictionary
'''
my_list = [1,2,3,4,5,6,7,8,9,10]
square_num = []
for i in my_list:
    square = i ** 2
    square_num.append(square)

print(square_num)
dictti = {}
i = 0
while i == 10:

    for key in my_list:
        for values in square_num:
            dictionary = dict({i:values})
            print(dictionary.keys())
            print(dictionary.values())
    i += 1
'''
# Simple & Fast way to doing above task
number = list(range(1,11))

number_dict = {num:num**2 for num in number}

print(number_dict)