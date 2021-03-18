import sys
M=int(input())
S=set()
for i in range(M):
    op=sys.stdin.readline().split()
    if(len(op)==1):
        if(op[0]=='all'):
            S=set([_ for _ in range(1,21)])
        elif(op[0]=='empty'):
            S=set([])
    else:
        opcode=op[0]
        value=int(op[1])
        if(opcode=='add'):
            S.add(value)
        elif(opcode=='remove'):
            if(value in S):
                S.remove(value)
        elif(opcode=='check'):
            if(value in S):
                print(1)
            else:
                print(0)
        elif(opcode=='toggle'):
            if(value in S):
                S.remove(value)
            else:
                S.add(value)

