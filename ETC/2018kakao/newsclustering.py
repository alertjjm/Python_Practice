import re
def solution(str1, str2):
    answer = 0
    sSet1=[]
    sSet2=[]
    for i in range(len(str1)-1):
        if(str1[i].isalpha() and str1[i+1].isalpha()):
            sSet1.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        if(str2[i].isalpha() and str2[i+1].isalpha()):
            sSet2.append(str2[i:i+2].lower())
    inSet=[]
    for a in sSet1:
        if a in sSet2 and a not in inSet:
            cnt=min(sSet1.count(a),sSet2.count(a))
            for _ in range(cnt):
                inSet.append(a)
    unLen=len(sSet1)+len(sSet2)-len(inSet)
    if(unLen==0 and len(inSet)==0):
        return 65536
    return int(len(inSet)/unLen*65536)

print(solution("FRANCE","french"))
print(solution("handshake","shake hands"))
print(solution("aa1+aa2","AAAA12"))
print(solution("E=M*C^2","e=m*c^2"))