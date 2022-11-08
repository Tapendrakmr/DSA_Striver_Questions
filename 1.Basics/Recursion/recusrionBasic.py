def printNtimes(x):
    if x==0:
        return
    print('Tapendra')
    printNtimes(x-1)
def printNto1(x):
    if x==0:
        return
    print(x)
    printNto1(x-1)
def print1toN(x,cur):
    if x==0:
        return
    print(cur+1)
    print1toN(x-1,cur+1)

def sumFirstN(x):
    return int(x*(x+1)/2)
    # if x==0:
    #     print(summ)
    #     return summ
    # summ+=x
    # sumFirstN(x-1,summ)
def factorial(x):
    if x<=1:
        return 1
    return x*factorial(x-1)

def reverseArray(arr,start,end):
    if start<=end:
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        reverseArray(arr,start+1,end-1)
    return arr
def checkPalindrome(s,start,end):
    if start<end:
        if s[start]!=s[end]:
            return False
        checkPalindrome(s,start+1,end-1)
    return True  
def fibonnaci(n):
    if n<=1:
        return 1
    return fibonnaci(n-1)+fibonnaci(n-2)
    
x=int(input('Enter lengt'))
# arr=[int(x) for x in input().split()]
# S=input()
# reverseArray(arr,0,x-1)
for i in range(x+1):
    print(fibonnaci(i))