def reverseArray(arr,start,end):
    if start>=end:
        return arr
    temp=arr[start]
    arr[start]=arr[end]
    arr[end]=temp
    x=reverseArray(arr,start+1,end-1)
    return x

arr=[int(x) for x in input().split()]
start=0
end=len(arr)-1
print(reverseArray(arr,start,end))