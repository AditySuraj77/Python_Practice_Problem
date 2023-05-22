
import math
# Finding volume

def volume():
    radius = float(input("Enter Radius : "))
    height = float(input('Enter Height : '))

    pi = math.pi

    V = pi * radius**2 * height

    return V

def cost_litere(V):
    cost_per_liter = 40
    total_cost = V * cost_per_liter
    return total_cost


total_volume = volume()
total_cost = cost_litere(total_volume)

print('Total Cylinder Volume is : ',total_volume)
print('Cost of Milk : ',total_cost)

