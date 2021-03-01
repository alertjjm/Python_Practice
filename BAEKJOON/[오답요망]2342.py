##새로운 유형. 이걸 memoization으로 풀자니 너무 힘들다. 그래서 재귀로 풀었는데 초과가 나서 메모이제이션과 recursion을 같이 쓴다.
##dp에는 1차원만 있는게아니라 n차원도 가능하다는걸 항상 생각하자. 여기선 왼발, 오른발에 따라 i,j로 나눌수 있다.
import sys
sys.setrecursionlimit(10**6)
directions=list(map(int, input().split()))
dplist=[[[0 for i in range(5)] for k in range(5)] for l in range(len(directions)+1)]
def calc(now, next):
    if now==0:
        return 2
    elif now==next:
        return 1
    elif abs(now-next)==2:
        return 4
    else:
        return 3
def dp(left, right, index): #왼발이 left이고 오른발이 right에 있을때
    if(index==len(directions)-1):
        dplist[index][left][right]=0
        return 0
    else:
        ret=dplist[index][left][right]
        if(ret!=0):
            return ret
        moveleft=calc(left, directions[index])
        moveright=calc(right,directions[index])
        dplist[index][left][right]=min(dp(directions[index],right,index+1)+moveleft,dp(left,directions[index],index+1)+moveright)
        return dplist[index][left][right]

if(len(directions)==1):
    print(0)
elif(len(directions)==2):
    print(2)
else:
    print(dp(0,0,0))