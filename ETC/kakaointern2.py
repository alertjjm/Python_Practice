from copy import deepcopy
def solution(expression):
    answer = 0
    exps=[]
    tokenizing=expression
    for i in range(len(expression)):
        if(expression[i] in '*+-'):
            exps.append(int(tokenizing.split(expression[i])[0]))
            tokenizing=expression[i+1:]
            exps.append(expression[i])
    exps.append(int(tokenizing))
    priority=['*-+','*+-','-+*','-*+','+-*','+*-']
    for p in priority:
        exp=deepcopy(exps)
        for op in p:
            while(op in exp):
                idx=exp.index(op)
                cal=str(exp[idx-1])+op+str(exp[idx+1])
                del exp[idx+1]
                del exp[idx]
                del exp[idx-1]
                exp.insert(idx-1,eval(cal))
        answer=max(answer,abs(exp[0]))
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))