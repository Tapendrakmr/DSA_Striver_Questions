def SumOfN(digit,nSum):
    if digit<=0:
        return nSum
    nSum+=digit
    res=SumOfN(digit-1,nSum)
    return res
def directApproch(digit):
    return int((digit*(digit+1))/2)
digit=int(input("Enter a number :"))
nSum=0
print(SumOfN(digit,nSum))
print(directApproch(digit))