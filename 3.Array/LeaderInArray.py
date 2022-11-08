def leader(ans):
    maxi=ans[-1]
    print(maxi)
    for i in range(len(ans)-2,-1,-1):
        # print(ans[i])
        if ans[i]>maxi:
            print(ans[i])
            maxi=ans[i]
ans=[int(x) for x in input().split()]
leader(ans)