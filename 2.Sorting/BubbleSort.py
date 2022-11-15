def BubbleSort(arr):
    cnt=0
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                cnt+=1
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print("bubbleSort timmer",cnt)
    return arr      


def advancedBubbleSort(array):
    cnt=0
    for i in range(len(array)):
        swapped=False
        for j in range(len(array)-i-1):
            if arr[j]>arr[j+1]:
                cnt+=1
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

                swapped=True
        if not swapped:
            break
    print("advanced",cnt)
    

arr=[int(x) for x in input().split()]
print(BubbleSort(arr))
print(advancedBubbleSort(arr))