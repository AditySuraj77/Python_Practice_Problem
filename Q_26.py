

def CI(principal,rate,time):
    amount = principal * (1 + rate / 100) ** time
    compound_intr = principal - amount
    return compound_intr


P = int(input('Enter your Principal Amount : '))
r = float(input('Enter your rate amount : '))
t = int(input('Enter TimePeriod : '))

compound_intrest = CI(P,r,t)
print(compound_intrest)

