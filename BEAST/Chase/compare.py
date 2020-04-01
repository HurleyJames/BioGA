from matplotlib import pyplot as plt
import numpy as np
from scipy import interpolate

filename1 = "chase_prey.txt"
filename2 = "chase_pred.txt"
generation, aver1, best1 = [], [], []
aver2, best2 = [], []

a = np.loadtxt(filename1)
b = np.loadtxt(filename2)
generation = a[:,0]
aver1 = a[:,1]
best1 = a[:,2]
aver2 = b[:,1]
best2 = b[:,2]

plt.figure()
plt.plot(generation, aver1, 'red', linestyle='-', label='average_prey')
plt.plot(generation, best1, 'blue', linestyle='-', label='best_prey')
plt.plot(generation, aver2, 'red', linestyle='--', label='average_pred')
plt.plot(generation, best2, 'blue', linestyle='--', label='best_pred')
plt.legend()
plt.xlabel('epoch')
plt.ylabel('fitness')

plt.savefig('chase.png')
plt.show()
