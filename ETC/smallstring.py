def solution(ipt):
    leftresult=[]
    rightresult=[]
    middle=ipt
    left=0
    right=len(ipt)-1
    st=True
    while(st):
        t=False
        for i in range(1,len(middle)//2+1):
            lt=middle[:i]
            rt=middle[len(middle)-i:]
            if(lt==rt):
                leftresult=leftresult+[lt]
                rightresult=[rt]+rightresult
                middle=middle[i:len(middle)-i]
                t=True
                break
        if(t==False and len(middle)>0):
            return leftresult+[middle]+rightresult
        elif(t==False):
            return leftresult+rightresult

print(solution("abcxyabcdabcdxyabc"))
print(solution("abcdxyefghixyabcd"))
print(solution("xxxxxx"))
print(solution("llttaattll"))