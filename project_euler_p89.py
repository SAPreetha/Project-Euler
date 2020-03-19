def minimize(x):
    length=len(x)
    x=x.replace("IIII","IV")
    x=x.replace("VIV","IX")
    x=x.replace("XXXX","XL")
    x=x.replace("LXL","XC")
    x=x.replace("CCCC","CD")
    x=x.replace("DCD","CM")
    return length-len(x)
    
    
    

fp=open("c:/Users/aaveg/Desktop/roman.txt","r")
l=fp.readlines()


l=[i.rstrip() for i in l]
s=0
for i in l:
    s+=minimize(i)

print s
