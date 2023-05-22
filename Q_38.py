

# Checking String Palindrome or Not

def ispalindrome(s):
   return s == s[::-1]


user = input('Write a String To Check is Palindrome or Not : ')
ans = ispalindrome(user)

if ans:
   print('Yes')
else:
   print("No")
