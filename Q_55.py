
# Find Factorial WithOut Using Loop

def factorial(n):

        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
userInput = int(input('Enter a Number : '))
fact = factorial(userInput)

print(f'Factorial of {userInput} is = ',fact)