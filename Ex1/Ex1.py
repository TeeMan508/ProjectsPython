import math
def simple(n):
    if n==1:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
             return False
    return True
res=[a for a in range(1,10**7) if simple(a)]
f=open('text.txt','w')
for x in range(0,10):
    f.write(str(res.pop())+' ')
f.close()

#TestChange



