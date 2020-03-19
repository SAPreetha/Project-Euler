import random

def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def prime_in_place(lst):
    count=0
    for i in range(2,len(lst)+1):
        if (i==lst[i-1] and (i in prime_lst)):
            count+=1
    return count
    
prime_lst=[i for i in range(2,101) if prime(i)]
disks=range(1,101)
t_trials=10000
s_trials=0
for i in range(t_trials):
    random.shuffle(disks)
    if prime_in_place(disks)== 3:
        s_trials+=1

print float(s_trials)/t_trials
    
    
