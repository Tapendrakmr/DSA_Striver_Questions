def factorial(digit):
    if digit<=1:
        return 1
    ans=digit*factorial(digit-1)
    return ans
    
def factorialUptoN(digit):
    for i in range(1,digit+1):
        fact=factorial(i)
        if fact>digit:
            break
        print(fact,end=' ')
    return
digit=int(input())
print(factorialUptoN(digit))