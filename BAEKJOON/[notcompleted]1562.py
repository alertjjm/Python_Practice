DIVIDOR=1000000000
N=int(input())
sp=[[] for i in range(N+1)]

def solution(n):
    if(n<10):
        return 0
    if(n==10):
        return 1
    sp[10] = ["9876543210"]
    for i in range(10,n):
        for item in sp[i]:
            tempint=item + str(int(item[-1]) - 1)
            if('-' not in tempint):
                sp[i+1].append(tempint)
            tempint=item + str(int(item[-1]) + 1)
            if(len(item)+1==len(tempint)):
                sp[i+1].append(tempint)
            tempint=str(int(item[0]) + 1)+item
            if (len(item)+1 == len(tempint)):
                sp[i+1].append(tempint)
            tempint=str(int(item[0]) -1)+item
            if (len(item)+1 == len(tempint)):
                sp[i+1].append(tempint)
            leng=len(sp[i+1])
            for t in range(leng):
                temp=''.join(reversed(sp[i+1][t]))
                if(temp not in sp[i+1] and temp[0]!='0'):
                    sp[i+1].append(sp[i+1][t])

    return len(sp[n])%DIVIDOR
print(solution(N))