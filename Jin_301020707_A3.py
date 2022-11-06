#Name: Jin Huang
#Student ID: 301020707

from matplotlib import pyplot as plt
import numpy as np
import random
from self import self
plt.style.use('dark_background')
class Shop:

    #constructor
    def __init__(self):
        base = 2
        min = 1
        max = 30
        delta = 5
        size = 12

    #private method
    def __Generator(self):
        return random.gauss(0,1)

    #public method
    def plotter(self):
        global base, min, max, delta
        if base >= min or base <= min:
            delta += Shop.__Generator(self)
            base = delta
            base = int(base)
            return base
        if base <= max:
            delta -= Shop.__Generator(self)
            base = delta
            base = int(base)
            return base

#driver code
base = 2
min = 2
max = 10
delta = 5
size = 12
#Plotting
OnlineShop = [Shop.plotter(self) for _  in range(size)]
plt.plot(OnlineShop, color = 'yellow')
#labeling and design
plt.legend(['Online Purchases'])
plt.title('Online Shop Purchases Througout The Hour')
plt.xlabel('Hours (Noon to Midnight)')
plt.ylabel('Purchases (Thousands)')

plt.show()