import numpy as np
a=[]
with open('Input.txt') as ifile:
    for line in ifile:
        a.append(int(line))
b=np.array([int(x) for x in a])
print(str(sorted(b))+'\n')
print('max is:',str(sorted(b)[0]))
print('max is:',str(sorted(b)[len(sorted(b))-1]))
print('mean5 is:',((b-b.mean())**5).mean())
print('RMS is:',np.std(b).round(3))

complexb=np.genfromtxt('ComplexInput.txt', delimiter='\n', dtype=complex)
s=sorted(complexb, key=abs(complexb[0]))
print(str(s))



