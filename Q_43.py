
# Seprating two list
'''
def seprate_odd_even(lst):
    odd_num = []
    even_num = []

    for num in lst:
        if num % 2 == 0:
            even_num.append(num)
        else:
            odd_num.append(num)
    print('Odd Number = ',odd_num)
    print('Even Number = ',even_num)

input_list = input('Enter a Number : ').split()
input_list = [int(num) for num in input_list]
seprate_odd_even(input_list)'''


# merging 2Lists

user_input1 = input('Enter a Number : ').split()
user_input1 = [int(num) for num in user_input1]

user_input2 = input('Enter a Number : ').split()
user_input2 = [int(num) for num in user_input2]

merge_lst = user_input1.extend(user_input2)

print(user_input1)

