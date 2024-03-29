import numpy as np
import this
print('\n')
a=[]
with open('Input.txt') as ifile:
    for line in ifile:
        a.append(int(line))
b=np.array([int(x) for x in a])
print('Sorted array:',str(sorted(b)))
print('min is:',str(sorted(b)[0]))
print('max is:',str(sorted(b)[len(sorted(b))-1]))
print('mean is:',b.mean())
print('mean^5 is:',((b-b.mean())**5).mean())
print('RMS is:',np.std(b).round(3))


complexb=tuple(np.genfromtxt('ComplexInput.txt', delimiter='\n', dtype=complex))
print('Absolute sorting:',str(sorted(complexb, key=lambda x: abs(x))))
print('Reverse real sorting:',str(sorted(complexb, key=lambda x: x.real, reverse=True)))

stringb=tuple(np.genfromtxt('StringInput.txt', delimiter=' ', dtype=str))
print('Lenght sorting:',str(sorted(stringb, key=lambda x: len(x))))
print('Lexical and graphic order sorting:',str(sorted(stringb)))

