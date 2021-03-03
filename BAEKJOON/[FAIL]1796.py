alphas='abcdefghijklmnopqrstuvwxyz'
INF=9999999
S=input()
S=[ord(_)-ord('a') for _ in S]
dplist=[[-1 for i in range(26)] for j in range(len(S))]
def distance(a,b,c,d):
    return abs(a-c)+abs(c-d)+abs(d-b)
def dp(alpha, pos):
    ret=INF/2
    if(alpha==26):
        return 0
    if(dplist[pos][alpha]>=0):
        return dplist[pos][alpha]
    if(alpha in S):
        for k in range(len(S)):
            for low in range(len(S)):
                if(S[low]==alpha):
                    break
            for high in range(len(S)-1,-1,-1):
                if(S[high]==alpha):
                    break
            ret=min(ret,dp(alpha-1,k)+distance(k,pos,low,high),dp(alpha-1,k)+distance(k,pos,high,low))
            dplist[pos][alpha]=ret
            return ret

print(dp(0,0))
