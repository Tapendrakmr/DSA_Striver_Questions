def largest(arr):
    maxx=-99999
    for i in range(len(arr)):
        if arr[i]>maxx:
            maxx=arr[i]
    print(maxx)

def secondlargest(arr):
    maxx=-1
    secondMaxx=-1
    for i in range(len(arr)):
        if arr[i]>maxx:
            secondMaxx=maxx
            maxx=arr[i] 
        elif secondMaxx <arr[i] and arr[i]!=maxx:
            secondMaxx=arr[i]
            
    print(secondMaxx)

def arraySorted(arr):
    for i in range(len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True

def removeDuplicate(arr):
    i=0
    for k in range(len(arr)):
        if arr[k]!=arr[i]:
            i+=1
            arr[i]=arr[k]
    # if arr[i]!=arr[len(arr)-1]:
    #     arr[i+1]=arr[len(arr)-1]
    #     i=i+1
    for j in range(i+1,len(arr)):
        arr[j]='_'
    print(arr)

def rotateArray(arr,k):
    l=len(arr)
    temp=[0]*l
    for i in range(l):
        x=(l+k+i)%l
        # print(x)
        temp[x]=arr[i]
    print(temp)
def moveZeros(arr):
    x=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[x]=arr[i]
            x+=1
    for i in range(x,len(arr)):
        arr[i]=0
    print(arr)

def union(arr1,arr2):
    i=0
    j=0
    union=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            
            if len(union)>0 and union[-1]!=arr1[i]:
                union.append(arr1[i])
            elif len(union)==0:
                union.append(arr1[i])
            i+=1
        else:

            if len(union)>0 and union[-1]!=arr2[j]:
                union.append[arr2[j]]
            elif len(union)==0:
                union.append(arr2[j])
            j+=1
    print(union)


def findRepAndMiss(arr):
    last=len()

arr=[int(x) for x in input().split()]
arr2=[int(x) for x in input().split()]
# k=int(input())
union(arr,arr2)