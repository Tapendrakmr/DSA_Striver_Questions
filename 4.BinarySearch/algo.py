def bSearch(target,arr):
    lo=0
    hi=len(arr)-1
    while lo<=hi:
        mid=lo+(hi-lo)//2
        if arr[mid]==target:
            return mid
        if arr[mid]>target:
            hi=mid-1
        else:
            lo=mid+1
    return -1
arr=[int(x) for x in input().split()]
target=int(input('Enter number :'))
print(bSearch(target,arr))