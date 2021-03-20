from queue import PriorityQueue
que = PriorityQueue()
points=list(map(float,input().split()))
N,M=map(int,input().split())
showed=[]
categories=[]
catepoints={'A':points[0],'B':points[1],'C':points[2],'D':points[3],'E':points[4]}
isreadpoints={'O':10,'W':0, 'Y':100}
for i in range(N):
    showed.append(list(input()))
for i in range(N):
    categories.append(list(input()))
cnt=0
for i in range(N):
    for j in range(M):
        if(showed[i][j]!='W'):
            que.put((-catepoints[categories[i][j]]-isreadpoints[showed[i][j]],[i,j]))
            cnt+=1
for i in range(cnt):
    item=que.get()[1]
    print(categories[item[0]][item[1]]+" "+str(catepoints[categories[item[0]][item[1]]])+" "+str(item[0])+" "+str(item[1]))


