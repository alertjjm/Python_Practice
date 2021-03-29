import sys
N,S=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
start=0
end=N-1
result=sum(arr)
if(result<S):
    print(0)
else:
    answer=N
    start=0
    end=0
    summation=arr[start]
    while(start<=end and end<N):
        if(summation<S):
            end+=1
            if(end==N):
                break
            summation+=arr[end]
        else:
            answer=min(answer,end-start+1)
            summation-=arr[start]
            start+=1
    print(answer)
