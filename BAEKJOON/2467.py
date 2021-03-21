import sys
N=int(input())
liquids=list(map(int,sys.stdin.readline().split()))
a=0
b=0
result=1000000000*3
left=0
right=N-1
while(left<right):
    if(abs(liquids[left]+liquids[right])<result):
        a=left
        b=right
        result=abs(liquids[left]+liquids[right])
    if(liquids[left]+liquids[right]<0):
        left+=1
    elif(liquids[left]+liquids[right]==0):
        break
    else:
        right-=1
    if(left==right):
        break
print(liquids[a],liquids[b])

