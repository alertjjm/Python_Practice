H,Y=map(int,input().split(" "))
def maxmoney(H,Y):
    resultlist=[]
    if Y==0:
        return H
    #case 1: 1년 5%
    if(Y>=1):
        case1=maxmoney(H,Y-1)*1.05
        resultlist.append(int(case1))
    #case 2: 3년 20%
    if(Y>=3):
        case2=maxmoney(H,Y-3)*1.2
        resultlist.append(int(case2))
    #case 3: 5년 35%
    if(Y>=5):
        case3=maxmoney(H,Y-5)*1.35
        resultlist.append(int(case3))
    return max(resultlist)
print(maxmoney(H,Y))