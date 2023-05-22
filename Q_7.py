
                 # Calculating Leap Year
while True:

    year = int(input('Year Name : '))

    if year%4 ==0 and year%100 != 0 or year%400 == 0:
        print(year,' Leap Year')
    else:
        print(year,'Not Leap Year')
