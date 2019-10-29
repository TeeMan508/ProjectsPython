import numpy as np
a=[]
with open('Input.txt') as ifile:
    for line in ifile:
        a.append(int(line))
b=np.array([int(x) for x in a])
print(str(b)+'\n')
def max(arg):
    res =b[1]
    for x in arg:
        if x>res:
            res=x
    return res
def min(arg):
    res=b[1]
    for x in arg:
        if x<res:
            res=x
    return res
print('max is:'+str(max(b))+' '+'min is:'+str(min(b)))

#TestCommit
