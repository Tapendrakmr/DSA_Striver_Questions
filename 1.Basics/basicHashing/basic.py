def frequencey(arr):
    dict={}
    for i in range(len(arr)):
        if arr[i] in dict:
            dict[arr[i]]+=1
        else:
            dict[arr[i]]=1
    print(dict)
    maxx=-9999999
    maxele=0
    minn=9999999
    minele=0
    for x in dict:
        if dict[x]>maxx:
            maxx=dict[x]
            maxele=x
        if dict[x]<minn:
            minn=dict[x]
            minele=x
    print(maxele)
    print(minele)
    
arr=[int(x) for x in input().split()]
frequencey(arr)