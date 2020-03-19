def prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

def check(x):
    if len(x)!=9:
        return False
    lst=list(x)
    lst.sort()
    for i in "123456789":
        if i not in lst:
            return False
    return True

l=[]
a=[]
i=1
while True:
    for j in range(1,10000):
        s=str(i)+str(j)+str(i*j)
        if len(s)>9:
            break
        if check(s):
            print i,j,i*j,s
            l+=[int(i*j)]
            a+=[i]
    i+=1
    if i>=10000:
        break
