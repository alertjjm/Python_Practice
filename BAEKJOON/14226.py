from collections import deque
s=int(input())
q=deque()
q.append([1,0])
dp=[[-1]*(s+1) for i in range(s+1)]
dp[1][0]=0
while q:
    num, copy=q.popleft()
    #1
    if(dp[num][num]==-1):
        dp[num][num]=dp[num][copy]+1
        q.append([num,num])
    if(num+copy<=s and dp[num+copy][copy]==-1):
        dp[num+copy][copy]=dp[num][copy]+1
        q.append([num+copy,copy])
    if(num-1>=0 and dp[num-1][copy]==-1):
        dp[num-1][copy]=dp[num][copy]+1
        q.append([num-1,copy])
print(min(dp[s][1:]))

