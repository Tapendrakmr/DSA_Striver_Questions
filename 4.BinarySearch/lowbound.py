def lowBound(target,arr):
    lo=0
    hi=len(arr)-1
    res=-1
    while lo<=hi:
        mid=lo+(hi-lo)//2
        if arr[mid]==target:
            return mid
        if arr[mid]<target:
            res=mid
            lo=mid+1
        else:
            hi=mid-1
    return res
arr=[int(x) for x in input().split()]
target=int(input('Enter number :'))
print(lowBound(target,arr))