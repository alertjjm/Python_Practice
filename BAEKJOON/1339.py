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
for number in numlist:
    mask=0
    for i in range(len(number)):
        if(number[i] in numdict):
            numdict[number[i]]+=pow(10,len(number)-1-i)
        else:
            numdict[number[i]]=pow(10,len(number)-1-i)
valuelist=list(numdict.values())
valuelist.sort(reverse=True)
result=0
for i in valuelist:
    result+=possessednum*i
    possessednum-=1
print(result)

