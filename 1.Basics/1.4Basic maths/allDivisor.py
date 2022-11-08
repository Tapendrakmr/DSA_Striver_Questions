import math
def allDivisor(digit):
    if digit==0:
        return 0
    digit=abs(digit)
    for i in range(1,int(math.sqrt(digit))+1):
        if (digit%i==0):
            print(i,end= ' ')
            if(i!=digit//i): print(digit//i,end=' ')
    
digit=int(input("Enter number"))
print(allDivisor(digit))