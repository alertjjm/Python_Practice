DIVISION=1000000
encrypted=input()
N=len(encrypted)
dplist=[0]*(5001)
dplist[0]=1
dplist[1]=1
st=False
if(encrypted[0]=='0'):
    print(0)
else:
    for i in range(1,N):
        if(encrypted[i]!='0'):
            dplist[i+1]=dplist[i]
        twonum=int(encrypted[i-1:i+1])
        if(encrypted[i]=='0' and twonum>26 or twonum<1):
            st=True
            break
        if(10<=int(encrypted[i-1:i+1])<=26):
            dplist[i+1]+=dplist[i-1]
    if(st):
        print(0)
    else:
        print(dplist[N]%DIVISION)