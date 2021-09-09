from datetime import datetime

def solution(lines):
    timeDict={}
    for l in range(len(lines)):
        line=lines[l]
        timeTokens=line.split()
        a=datetime.strptime(timeTokens[0]+" "+timeTokens[1], "%Y-%m-%d %H:%M:%S.%f")
        millisec = int(a.timestamp() * 1000)
        duration=int(float(timeTokens[2][:-1])*1000)
        for i in range(duration):
            key=millisec-i
            if(key in timeDict):
                timeDict[key].add(l)
            else:
                timeDict[key]= {l}
    answer=-1
    for key in timeDict:
        tempSet=set()
        for i in range(1000):
            if(key+i in timeDict):
                tempSet=tempSet.union(timeDict[key+i])
        answer=max(answer,len(tempSet))
    return answer

print(solution( [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))