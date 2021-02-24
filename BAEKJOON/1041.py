N=int(input())
dicelist=list(map(int, input().split(' ')))
pointlist=[[0,1,2],[0,1,3],[0,3,4],[0,4,2],[5,1,2],[5,1,3],[5,3,4],[5,4,2]]
if(N<2):
    print(sum(dicelist)-max(dicelist))
else:
    onenum=pow(N-2,2)*5+(N-2)*4
    twonum=(N-2)*8+4
    threenum=4
    minone=min(dicelist)
    mintwo=1000
    for i in range(6):
        for j in range(6):
            if(i+j!=5 and i!=j and dicelist[i]+dicelist[j]<mintwo):
                mintwo=dicelist[i]+dicelist[j]
    minthree=1000
    for point in pointlist:
        if(dicelist[point[0]]+dicelist[point[1]]+dicelist[point[2]]<minthree):
            minthree=dicelist[point[0]]+dicelist[point[1]]+dicelist[point[2]]
    total=onenum*minone+twonum*mintwo+threenum*minthree
    print(total)