def armstrong(digit):
    countLen=0
    temp=digit
    digitPowSum=0
    while temp!=0:
        countLen+=1
        temp=temp//10
    secondtemp=digit
    while secondtemp!=0:
        last=secondtemp%10
        secondtemp=secondtemp//10
        digitPowSum+=pow(last,countLen)
    print(digitPowSum)
    if digit==digitPowSum:
        return 'Armstrong'
    return 'Not Armstrong'
digit=int(input("Enter number"))
print(armstrong(digit))