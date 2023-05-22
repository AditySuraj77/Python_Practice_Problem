# Finding the item present in ist
'''
def list_item(user_list, user_search_item):

    for item in user_list:
        if item == user_search_item:
            print('Yes Item was Found',item)
            break
user_list = list(input('Enter a item : '))

user_search_item = input('Enter a Item to Search : ')

list_item(user_list,user_search_item)'''


def old_list_new_lst(lst):
    new_list = []
    for item in lst:
        #print((type(item)))
        square = item ** 2
        new_list.append(square)
    return new_list


usr_input = [2,4,6,8,10,12,14,16,18,20]

squared_lst = old_list_new_lst(usr_input)

print('Original List = ',usr_input)
print('Squared List = ',squared_lst)
