def reverseNumber(digit,newNumber):
    if digit==0:
        return newNumber
    last=digit%10
    digit=digit//10
    newNumber=newNumber*10+last
    y=reverseNumber(digit,newNumber)
    return y
def checkPalindrome(digit):
    reverse=reverseNumber(digit,0)
    if digit==reverse:
        return 'Palindrome'
    return 'Not Palindrome'
digit=int(input())
print(checkPalindrome(digit))