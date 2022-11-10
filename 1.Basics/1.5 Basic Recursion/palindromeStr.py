def palindrome(str,start,end):
    if str[start]!=str[end]:
        return 'Not Plaindrome'
    if start>=end:
        return 'Palindrome'
    x=palindrome(str,start+1,end-1)
    return x
str=input("Enter String :")
start=0
end=len(str)-1
print(palindrome(str,start,end))