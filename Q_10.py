

# Calculate Profit and Loss
'''
while True:
    print('Programmed Calculate Profit')
    Selling_price = float(input('Enter Selling Price Number : '))
    Cost_price = float(input('Enter Cost Price Number : '))

    profit = Selling_price - Cost_price

    print('Your Total Profit is = ', profit)
'''


'''
# Calculate Loss
while True:
    print('Programmed Calculate Profit')
    Selling_price = float(input('Enter Selling Price Number : '))
    Cost_price = float(input('Enter Cost Price Number : '))

    loss = Cost_price - Selling_price

    print('Your Total Loss is = ', loss)
'''

def checking_loss_and_profit():
    cost_price = float(input('Enter cost price : '))
    selling_price = float(input('Enter selling price : '))

    if selling_price > cost_price:
        profit = selling_price = cost_price
        print('Its a Profit Profit Amount = ',profit)

    elif selling_price < cost_price:
        loss = cost_price - selling_price
        print('Its Loss Loss Price = ', loss)
    else:
        print('There are no Loss and Profit')
checking_loss_and_profit()


