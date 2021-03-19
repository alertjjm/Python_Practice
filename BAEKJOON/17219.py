import sys
N,M=map(int,input().split())
password=dict()
for i in range(N):
    a,b=sys.stdin.readline().rstrip().split()
    password[a]=b
for i in range(M):
    ques=sys.stdin.readline().rstrip()
    print(password[ques])