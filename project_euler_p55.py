def is_palindrome(num):
    num=str(num)
    length=len(num)
    for i in range(length):
        if num[i]!=num[length-1-i]:
            return False
    return True
        

def rev(num):
    num=str(num)
    return int(num[-1::-1])
    
def num_iter(num):
    count_iter=1
    num=num+rev(num)
    for i in range(55):
        if not is_palindrome(num):
            count_iter+=1
            num=num+rev(num)
        else:
            return num, count_iter
    
    return False


count=0
for i in range(1,10000):
    if not num_iter(i):
        print i
        count+=1

print count
