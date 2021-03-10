import sys
N=int(input())
M=int(input())
buttons=[str(i) for i in range(10)]
broken=sys.stdin.readline().split()
for b in broken:
    buttons.remove(b)
if(len(buttons)==0):
    print(abs(N-100))
else:
    mini=abs(N-100)
    for i in range(999999):
        temp=list(str(i))
        st=True
        for t in temp:
            if(t in buttons):
                pass
            else:
                st=False
                break
        if(st==True):
            mini=min(mini,len(str(i))+abs(i-N))
    print(mini)
