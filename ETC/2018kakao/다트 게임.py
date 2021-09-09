bounusDict={'S':1, 'D':2, 'T':3}
def solution(dartResult):
    answer=0
    idx=0
    L=len(dartResult)
    prev=0
    while(idx<L):
        pos=idx
        while(dartResult[pos].isdigit()):
            pos+=1
        point=int(dartResult[idx:pos])
        idx=pos-1
        bonus=dartResult[idx+1]
        if(idx+2 < L and (dartResult[idx+2]=='*' or dartResult[idx+2]=='#')):
            option=dartResult[idx+2]
            if(option=='*'):
                answer+=prev
                answer+=pow(point,bounusDict[bonus])*2
                prev=pow(point,bounusDict[bonus])*2
            else:
                answer-=pow(point,bounusDict[bonus])
                prev=-pow(point,bounusDict[bonus])
            idx=idx+3
        else:
            answer+=pow(point,bounusDict[bonus])
            prev=pow(point,bounusDict[bonus])
            idx=idx+2
    return answer

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))