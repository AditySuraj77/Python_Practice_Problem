
# Calculate simple Intrest

def simple_intrest():
    principle = float(input('Enter Principal Amount : '))
    rate = float(input('Enter Rate of Interest : '))
    time_period = float(input('Enter Time period : '))

    SI = principle * rate * time_period/100

    print('Simple Interest is = ', SI)
simple_intrest()