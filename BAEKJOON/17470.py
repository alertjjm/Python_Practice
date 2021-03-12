import sys
N,M,R=map(int,input().split())
temparr = [[0 for i in range(M)] for j in range(N)]
array=[[] for i in range(N)]
for i in range(N):
    array[i]=list(map(int,sys.stdin.readline().split()))
ops=list(map(int,input().split()))
def turn(op,arr):
    if(op==1):
        return [arr[len(arr)-1-j] for j in range(N)]
    elif(op==2):
        for i in range(len(arr)):
            arr[i].reverse()
        return arr
    elif(op==3):
        return [[arr[N-1-i][j] for i in range(N)] for j in range(M)]
    elif(op==4):
        return [[arr[i][M-1-j] for i in range(N)] for j in range(M)]
    elif(op==5):
        xlimit=M//2 #미만
        ylimit=N//2
        for i in range(N):
            for j in range(M):
                if(i<ylimit and j<xlimit):
                    #1영역
                    newarr[i][j+xlimit]=arr[i][j]
                elif(i<ylimit and j>=xlimit):
                    #2영역
                    newarr[i+ylimit][j]=arr[i][j]
                elif(i>=ylimit and j<xlimit):
                    #3영역
                    newarr[i-ylimit][j]=arr[i][j]
                elif(i>=ylimit and j>=xlimit):
                    #4영역
                    newarr[i][j-xlimit]=arr[i][j]
        return newarr
    else:
        newarr = [[0 for i in range(M)] for j in range(N)]
        xlimit=M//2 #미만
        ylimit=N//2
        for i in range(N):
            for j in range(M):
                if(i<ylimit and j<xlimit):
                    #1영역
                    newarr[i+ylimit][j]=arr[i][j]
                elif(i<ylimit and j>=xlimit):
                    #2영역
                    newarr[i][j-xlimit]=arr[i][j]
                elif(i>=ylimit and j<xlimit):
                    #4영역
                    newarr[i][j + xlimit] = arr[i][j]
                elif(i>=ylimit and j>=xlimit):
                    #3영역
                    newarr[i - ylimit][j] = arr[i][j]
        return newarr
for i in range(R):
    array=turn(ops[i],array)
    N=len(array)
    M=len(array[0])
for line in array:
    for j in line:
        print(j,end=' ')
    print()