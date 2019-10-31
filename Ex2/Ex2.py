import numpy as np
a=[]
with open('Input.txt') as ifile:
    for line in ifile:
        a.append(int(line))
b=np.array([int(x) for x in a])
bsort=sorted(b)
print(str(bsort)+'\n')
print('max is:',str(bsort[0]))
print('max is:',str(bsort[len(bsort)-1]))
print('mean5 is:',(b**5).mean().round(3))
print('RMS is:',np.std(b).round(3))


