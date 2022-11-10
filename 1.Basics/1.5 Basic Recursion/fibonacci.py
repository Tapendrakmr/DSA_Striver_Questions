def fibonacci(digit):
    if digit<=1:
        return digit
    last=fibonacci(digit-1)
    secondlast=fibonacci(digit-2)
    arr[digit]=last+secondlast
    return last+secondlast
    
digit=int(input("Enter number"))
arr=[0]*(digit+5)
print(fibonacci(digit))
print(arr)
