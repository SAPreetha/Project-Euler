def num2word(num):
    if num == 0:
        return 0
    if num == 1:
        return 3
    if num == 2:
        return 3
    if num == 3:
        return 5
    if num == 4:
        return 4
    if num == 5:
        return 4
    if num == 6:
        return 3
    if num == 7:
        return 5
    if num == 8:
        return 5
    if num == 9:
        return 4
    if num == 10:
        return 3
    if num == 11:
        return 6
    if num == 12:
        return 6
    if num == 13:
        return 8
    if num == 14:
        return 8
    if num == 15:
        return 7
    if num == 16:
        return 7
    if num == 17:
        return 9
    if num == 18:
        return 8
    if num == 19:
        return 8
    if num == 20:
        return 6
    if num == 30:
        return 6
    if num == 40:
        return 5
    if num == 50:
        return 5
    if num == 60:
        return 5
    if num == 70:
        return 7
    if num == 80:
        return 6
    if num == 90:
        return 6

    
    if num == 1000:
        return 11

    
def total_len(num):
    correction=0
    
    if num/10==0:
        return num2word(num)
    elif num/100==0 and num<=20:
        return num2word(num)
    
    elif num/100==0 and num>20:
        return num2word((num/10)*10)+num2word(num%10)
    elif num/1000==0:
        if num%100==0:
            correction=-3
        return num2word(num/100)+10+total_len(num%100)+correction
    else:
        return num2word(1000)


total=0
for i in range(1,1001):
    total+=total_len(i)

print total
    
