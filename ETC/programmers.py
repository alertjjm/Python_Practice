def solution(N, number):
    dyli=[{0}]
    for i in range(1,9):
        temp=set([])
        s=str(N)
        s=s*i
        temp.add(int(s))
        dyli.append(temp)
    for i in range(2,9):
        for j in range(1,i):
            op1=dyli[j]
            op2=dyli[i-j]
            for o1 in op1:
                for o2 in op2:
                    dyli[i].add(o1*o2)
                    dyli[i].add(o1-o2)
                    try:
                        dyli[i].add(o1//o2)
                    except:
                        pass
                    dyli[i].add(o1+o2)
    for i in range(1,9):
        if(number in dyli[i]):
            return i
    return -1
print(solution(2,11))