# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 21:02:03 2016

@author: preetha
"""
from math import sqrt

def permutations(a):
    
    def permutations_str(a):
        if len(str(a))==1:
            return [str(a)]
            
        if len(str(a))==2:
            b=str(a)
            c=b[::-1]
            if b!=c:
                return [b,c]
            else: return [b]
        if len(str(a))>=3:
            b=str(a)
            perm=[]
            for i in range(len(b)):
                num=b[:i]+b[i+1:]
                lst=permutations_str(num)
                lst=[b[i]+str(j) for j in lst]
                perm+=lst
            return perm
            
    lst_perms=permutations_str(a)
    lst_perms=[int(i) for i in lst_perms]
    return list(set(lst_perms))
    
def atleast_3_primes(nums):    
    count=0
    for i in nums:
        if is_prime(i):
            count+=1
    if count>=3:
        return True
    

def is_prime(num):
    for i in range(2,int(sqrt(num))+1):
        if num%i==0:
            return False
    return True


def is_ap(lst):
    lst.sort()
    lst_ap=[]
    for i in lst:
        for j in lst:
            for k in lst:
                if i<j<k:
                    if (j-i)==(k-j):
                        lst_ap+= [str(i)+str(j)+str(k)]
    lst_ap=list(set(lst_ap))
    if len(lst_ap)>=1:
        return lst_ap
    return False
    
    
    
    
x=1000

while x<=9998:
    x+=1
    nums=list(set(permutations(x)))
    if atleast_3_primes(nums):
        lst_primes=[i for i in nums if is_prime(i)]
        lst_primes=[i for i in lst_primes if len(str(i))==4]
        lst_primes.sort()
    if len(lst_primes)>=3:
        if is_ap(lst_primes):
            print is_ap(lst_primes)
