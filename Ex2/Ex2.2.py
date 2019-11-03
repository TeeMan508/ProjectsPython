import matplotlib.pyplot as plt
import numpy as np
import random
import math
N=10**7
r = np.random.uniform(0, 1, (N,2))-0.5
truescat = np.sum(r**2, axis=1) < 0.25
res=np.count_nonzero(truescat)
print('pi equals', res/N/0.25)


def pi_error(arg):
    return math.sqrt(math.pi*0.25*(1-math.pi*0.25)/(arg))


xs = [2**k for k in range(10,25)]
ys = [pi_error(x) for x in xs]
plt.plot(xs,ys, color='red')
plt.xscale('log')
plt.xlabel('Number of points')
plt.ylabel('Error')
plt.title('The dependence of the error on the number of points')
plt.grid(True)
plt.show()

