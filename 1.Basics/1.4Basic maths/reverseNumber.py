def reverseNumber(digit,newNumber):
    if digit==0:
        return newNumber
    last=digit%10
    digit=digit//10
    newNumber=newNumber*10+last
    y=reverseNumber(digit,newNumber)
    return y

digit=int(input())
newNumber=0
print(reverseNumber(digit,newNumber))