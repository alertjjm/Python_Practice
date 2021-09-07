from bisect import bisect_left
def solution(info, query):
    answer=[]
    resultDict={}
    nan='-'
    for tokens in info:
        lang,position,career,soulfood,score = tokens.split()
        for l in [lang, nan]:
            for p in [position, nan]:
                for c in [career, nan]:
                    for s in [soulfood, nan]:
                        if l+p+c+s in resultDict:
                            resultDict[l+p+c+s].append(int(score))
                        else:
                            resultDict[l+p+c+s]=[int(score)]
    for key in resultDict:
        resultDict[key].sort()
    for tokens in query:
        tokenlist=tokens.split()
        lang,position,career,soulfood,score=tokenlist[0],tokenlist[2],tokenlist[4],tokenlist[6],tokenlist[7]
        if(lang+position+career+soulfood in resultDict):
            i=bisect_left(resultDict[lang+position+career+soulfood], int(score))
            answer.append(len(resultDict[lang + position + career + soulfood]) - i)
        else:
            answer.append(0)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))