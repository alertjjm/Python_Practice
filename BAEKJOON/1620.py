import sys
N,M=map(int,input().split())
pokemons=dict()
for i in range(N):
    inputvalue=sys.stdin.readline().rstrip()
    pokemons[str(i+1)]=inputvalue
    pokemons[inputvalue]=str(i+1)
for i in range(M):
    q=sys.stdin.readline().rstrip()
    print(pokemons[q])
