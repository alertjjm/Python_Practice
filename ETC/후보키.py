from itertools import combinations
def solution(relation):
    answerSet=[]
    L=len(relation[0])
    keyIdx=[i for i in range(L)]
    for i in range(1,L+1):
        keySets = list(combinations(keyIdx,i))
        for key in keySets:
            resultList = []
            for a in relation:
                temp=[]
                for k in key:
                    temp.append(a[k])
                resultList.append(tuple(temp))
            resultSet=set(resultList)
            if(len(resultList)==len(resultSet)):
                status=True
                for ans in answerSet:
                    if(len(set(key).intersection(ans))==len(ans)):
                        status=False
                        break
                if(status):
                    answerSet.append(set(key))
    return len(answerSet)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))