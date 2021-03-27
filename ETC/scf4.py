import sys
N=int(input())
indexes=[]
for i in range(N):
    indexes.append(sys.stdin.readline().rstrip())
Q=int(input())
result=[]
def findPattern(pattern):
    idx = 0
    result = [0]
    for j in pattern[1:]:
        if(j == pattern[idx]):
            result.append(idx)
            idx += 1
        else:
            idx = 0
            result.append(idx)
    return result
def kmp(target, pattern):
    patternList = findPattern(pattern)
    idx = 0
    for j in target:
        if(idx == len(pattern)):
            return True
        if(j == pattern[idx]):
            idx += 1
            continue
        while(j != pattern[idx] and idx != 0):
            idx = patternList[idx - 1]
        if(idx == 0 and j == pattern[idx]):
                idx += 1
    if(idx == len(pattern)):
        return True
    return False
    
for i in range(Q):
    search=sys.stdin.readline().rstrip()
    cnt=0
    for index in indexes:
        if(kmp(index,search)):
            cnt+=1
    result.append(cnt)
for r in result:
    print(r)