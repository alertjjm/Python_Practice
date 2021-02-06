num=int(input())
status=[]
for i in range(num):
    li=[]
    n,m=map(int, input().split())
    for j in range(n):
        matrix=[[0,0],[0,0]]
        matrix[0][0],matrix[0][1]=map(int, input().split())
        matrix[1][0],matrix[1][1]=map(int, input().split())
        li.append(matrix)
    if m%2==1:
        status.append('NO')
    else:
        leftstatus=False
        rightstatus=False
        for t in li:
            if(t[1][0]==t[0][1]):
                rightstatus=True
        if(rightstatus==True):
            status.append('YES')
        else:
            status.append('NO')
for i in status:
    print(i)
