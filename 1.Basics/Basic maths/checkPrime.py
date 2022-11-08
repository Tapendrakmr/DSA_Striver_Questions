import math
def checkPrime(digit):
    if digit<1:
        return 0
    if digit==1:
        return 'Prime'
    for i in range(2,int(math.sqrt(digit))+1):
        if (digit%i==0):
            return 'Not Prime'
    return 'Prime'

digit=int(input("Enter digit "))
print(checkPrime(digit))