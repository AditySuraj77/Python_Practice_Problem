
# Reverse Strings

'''
userInput = input('Enter a String To Reversing : ')
split_user = userInput.split()
rev_user = split_user[::-1]
join_rev = ''.join(rev_user)


print(join_rev)
'''

# Counting Number of word
'''
user = input('Enter a Sentences : ')

user_split = user.split()
count_word = len(user_split)

print('Number of Word = ',count_word)'''

# Find given list ascending order or not

test_list = input('Enter a Number : ')

#test_list = [1, 4, 5, 8, 10]

# printing original list
print("Original list : " + str(test_list))

# using naive method to
# check sorted list
flag = 0
i = 1
while i < len(test_list):
    if (test_list[i] < test_list[i - 1]):
        flag = 1
    i += 1

# printing result
if (not flag):
    print("Yes, List is sorted.")
else:
    print("No, List is not sorted.")