def search_matrix(mat,target):
    n=len(mat)
    m=len(mat[0])
    l=0
    hi =(n*m)-1
    while l<=hi:
        mid=l+(hi-l)//2
        if target==mat[int(mid/m)][int(mid%m)]:
            return True
        elif mat[int(mid/m)][int(mid%m)]<target:
            l=mid+1
        else:
            hi=mid-1
    return False