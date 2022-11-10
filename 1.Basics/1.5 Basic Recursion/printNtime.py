def printNtime(orgDigit,tempDigit):
    
    if tempDigit<=0:
        print("")
        return
    x=orgDigit-tempDigit
    print(x,end=' ')
    printNtime(orgDigit,tempDigit-1)
    
digit=int(input("Enter number"))
printNtime(digit+1,digit)