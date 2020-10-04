def solution(triangle):
    l=len(triangle)
    dyli=[[triangle[0][0]]]
    for i in range(1,l):
        temp=[0,]*(i+1)
        for j in range(i+1):
            now=triangle[i][j]
            if(j>=1):
                op1=dyli[i-1][j-1]
                if(temp[j]<now+op1):
                    temp[j]=now+op1
            try:
                op2=dyli[i-1][j]
                if(temp[j]<now+op2):
                    temp[j]=now+op2
            except:
                pass
        dyli.append(temp)
    print(dyli)
    return max(dyli[l-1])
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))