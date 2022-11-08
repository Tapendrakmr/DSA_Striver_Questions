def insertPos(target,arr):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=start+(end-start)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
            
    return start

arr=[int(x) for x in input().split()]
target=int(input('Enter number :'))
print(insertPos(target,arr))