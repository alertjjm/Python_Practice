N=int(input())
dplist=list(map(int, input().split(' ')))
def solve(n):
    childs=[]
    for i in range(len(dplist)):
        item=dplist[i]
        if(item==n):
            childs.append(i)
    if(len(childs)==0):
        return 0
    else:
        timelist=[]
        for child in childs:
            timelist.append(solve(child)+1)
        timelist.sort(reverse=True)
        for i in range(len(timelist)):
            timelist[i]+=i
        return max(timelist)
print(solve(0))
#각 직속자식들의 걸리는 시간을 측정(Dp재귀)
#직속 자식들 중에 가장 오래걸리는 거부터 차례대로