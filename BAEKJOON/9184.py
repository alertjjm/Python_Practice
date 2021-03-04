INF=-99999999
dplist=[[[1 if(i<=50 or j<=50 or k<=50) else INF for i in range(102)] for j in range(102)] for k in range(102)]
pairlist=[]

while True:
    a,b,c =map(int,input().split())
    if(a==-1 and b==-1 and c==-1):
        break
    pairlist.append([a+50,b+50,c+50])
def dp(a,b,c):
    ret=0
    if(dplist[a][b][c]!=INF):
        return dplist[a][b][c]
    if(a>70 or b>70 or c>70):
        ret= dp(70,70,70)
    elif(a < b and b < c):
        ret= dp(a, b, c-1) + dp(a, b-1, c-1) - dp(a, b-1, c)
    else:
        ret=dp(a-1, b, c) + dp(a-1, b-1, c) + dp(a-1, b, c-1) - dp(a-1, b-1, c-1)
    dplist[a][b][c]=ret
    return ret
for case in pairlist:
    a,b,c=case
    print("w("+str(a-50)+", "+str(b-50)+", "+str(c-50)+") = "+str(dp(a,b,c)))
