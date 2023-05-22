from statistics import mean

num_lst = []
while True:
    user_num = int(input('Enter a number : '))
    # print(user_num)
    num_lst.append(user_num)
    # print(num_lst)

    if user_num == 0:
        print('Sum of Total number you entered = ',sum(num_lst))
        print('Average of Numbers = ',mean(num_lst))
        break

