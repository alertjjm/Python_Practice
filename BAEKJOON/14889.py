from itertools import combinations
N=int(input())
players=[[] for i in range(N)]
for i in range(N):
    players[i]=list(map(int, input().split()))
nums=[i for i in range(N)]
teamnum=combinations(nums,len(nums)//2)
mini=9999999999999
for team in teamnum:
    otherteam=[x for x in nums if x not in team]
    teamcomb=combinations(team,2)
    otherteamcomb=combinations(otherteam,2)
    scorea=0
    scoreb=0
    for case in teamcomb:
        x,y=case
        scorea+=players[x][y]
        scorea+=players[y][x]
    for case in otherteamcomb:
        x, y = case
        scoreb += players[x][y]
        scoreb += players[y][x]
    minus=abs(scorea-scoreb)
    if(mini>minus):
        mini=minus
print(mini)