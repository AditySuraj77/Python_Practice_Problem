

def find_num_of_low_upper(string):
    lower = 0
    upper = 0

    for i in string:
        if i.islower():
            lower +=1
        else:
            upper+=1

    print('LowerCase = ',lower)
    print('UpperCase = ',upper)


userInput = input('Enter a Word to Count LowerCase and UpperCase : ')

result = find_num_of_low_upper(userInput)
print(result)


