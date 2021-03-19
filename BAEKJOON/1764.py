import sys
from queue import PriorityQueue
result=PriorityQueue()
N,M=map(int,input().split())
find=set()
for i in range(N):
    find.add(sys.stdin.readline().rstrip())
cnt=0
for i in range(M):
    temp=sys.stdin.readline().rstrip()
    if(temp in find):
        result.put(temp)
        find.remove(temp)
        cnt+=1
print(cnt)
for i in range(cnt):
    print(result.get())