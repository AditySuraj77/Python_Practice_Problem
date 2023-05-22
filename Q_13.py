def divisible_3or_6(num):

        if num%3 == 0 and num%6 == 0:
            print(num, 'is Divisible by 3 & 6')
        else:
            print(num,'is Not Divisible by 3 & 6')
            

num = float(input('Enter a Number : '))
divisible_3or_6(num)