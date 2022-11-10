def freqCount(arr):
    dict={}
    for x in arr:
        if x in dict:
            dict[x]=dict[x]+1
        else:
            dict[x]=1
    HighAndLow(dict)
    return dict
def HighAndLow(dict):
    a=sorted(dict.items(),key=lambda x:x[1])
    print(a[0][0],a[-1][0])
arr=[int(x) for x in input().split()]
print(freqCount(arr))