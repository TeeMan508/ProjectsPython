import numpy as np
a=[]
#a=np.array(x for x in f)
with open('Input.txt') as ifile:
    for line in ifile:
        a.append(int(line))
print(str(a)+'\n')
def max(b=np.array([int(x) for x in a])):
    res = 0
    for x in b:
        if x>res:
            res=x
    return res
def min(b=np.array([int(x) for x in a])):
    res= 0
    for x in b:
        if x<res:
            res=x
    return res
print('max is: '+str(min(b))+' '+'min is:'+str(min(b)))

#test commit