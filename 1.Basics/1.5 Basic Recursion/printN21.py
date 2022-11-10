def printN21(digit):
    if digit<=0:
        return
    print(digit,end=' ')
    printN21(digit-1)

digit=int(input("Enter a digit "))
printN21(digit)