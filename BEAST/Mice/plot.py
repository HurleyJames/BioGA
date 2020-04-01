from matplotlib import pyplot as plt
import numpy as np
from scipy import interpolate

filename = "log.txt"
generation, aver, best = [], [], []

a = np.loadtxt(filename)
generation = a[:,0]
aver = a[:,1]
best = a[:,2]

tck1 = interpolate.splrep(generation, aver)
tck2 = interpolate.splrep(generation, best)
x = np.linspace(min(generation), max(generation), 100)
y1 = interpolate.splev(x, tck1, der=0)
y2 = interpolate.splev(x, tck2, der=0)
print(x)

plt.figure()
plt.plot(generation, aver, 'red', label='average')
plt.plot(generation, best, 'blue', label='best')
plt.legend()
plt.xlabel('epoch')
plt.ylabel('fitness')

plt.savefig('log.png')
plt.show()
