import operator
N=int(input())
numlist=[]
maxlen=0
numdict={}
maxindex=-1
for i in range(N):
    number=input()
    numlist.append(number)
    if(maxlen<len(number)):
        maxlen=len(number)
        maxindex=i
curlen=maxlen
possessednum=9
firstlist=set()
for number in numlist:
    firstlist.add(number[0])
    mask=0
    for i in range(len(number)-1,-1,-1):
        if(number[i] in numdict):
            numdict[number[i]]+=pow(10,len(number)-1-i)
        else:
            numdict[number[i]]=pow(10,len(number)-1-i)
valuelist=list(numdict.values())
valuelist.sort()
sdict=sorted(numdict.items(), key=operator.itemgetter(0),reverse=True)
result=0
if(len(valuelist)==10):
    for i in range(len(valuelist)):
        if(sdict[i][0] not in firstlist):
            del valuelist[i]
            break;
possessednum=10-len(valuelist)
for i in valuelist:
    result+=(possessednum)*i
    possessednum+=1
print(result)