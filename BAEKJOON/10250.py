T=int(input())
tests=[]
for i in range(T):
    tests.append(map(int,input().split()))
for test in tests:
    H,W,N=test
    floor=N%H
    room=N//H+1
    if(floor==0):
        floor=H
        room-=1
    if(room<10):
        print(str(floor)+"0"+str(room))
    else:
        print(str(floor)+str(room))