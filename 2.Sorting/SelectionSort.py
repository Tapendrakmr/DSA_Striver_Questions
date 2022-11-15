def SelectionSort(arr):
    for i in range(len(arr)):
        minEle=0
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minEle]:
                minEle=j
        arr[j],arr[minEle]=arr[minEle],arr[j]

    return arr

arr=[int(x) for x in input().split()]
print(SelectionSort(arr))