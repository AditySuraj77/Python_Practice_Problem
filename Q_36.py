
# Find The vowels in string provided by user

string = input('Enter SomeThings : ')

vowel = 'aeiouAEIOU'
count = 0
for char in string:
    if char in vowel:
        count +=1

print("The number of vowels in the string is:", count)

