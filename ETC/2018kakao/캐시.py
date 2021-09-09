def solution(cacheSize, cities):
    answer = 0
    cacheDict={}
    time=0
    for city in cities:
        city=city.lower()
        if city in cacheDict: ##cache hit
            answer+=1
        else:                 ##cache miss
            answer+=5
            if(len(cacheDict)==cacheSize): ##cache full
                #LRU
                minKey=-1
                minVal=10**9
                for key in cacheDict:
                    if(cacheDict[key]<minVal):
                        minVal=cacheDict[key]
                        minKey=key
                if(minKey!=-1):
                    cacheDict.pop(minKey)
        if(cacheSize!=0):
            cacheDict[city]=time
            time+=1
    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]))
print(solution(5,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "jeju", "Seoul", "NewYork", "LA"]))
print(solution(0,["LA", "LA"]))
