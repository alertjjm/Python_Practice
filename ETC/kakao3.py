def solution(n, k, cmd):
    answer = ''
    status=[True]*n
    cursor=k
    deletestack=[]
    for c in cmd:
        if(c[0]=='D'):
            temp=c.split()
            num=int(temp[1])
            i = 0
            j = 1
            while (i != num):
                if (status[(cursor + j) % n]):
                    i += 1
                j = j + 1
            cursor = (cursor + j - 1) % n
        elif(c[0]=='U'):
            temp = c.split()
            num = int(temp[1])
            i = 0
            j = 1
            while (i != num):
                if (cursor - j < 0):
                    cursor = n-1
                    j = 0
                if (status[cursor - j]):
                    i += 1
                j += 1
            cursor = cursor - j + 1
        elif(c[0]=='C'):
            status[cursor]=False
            deletestack.append(cursor)
            st=False
            i = 0
            j = 1
            for idx in range(cursor,n):
                if(status[idx]):
                    st=True
                    cursor=idx
                    break
            if(not st):
                while (i != 1):
                    if (cursor - j < 0):
                        cursor = n - 1
                        j = 0
                    if (status[cursor - j]):
                        i += 1
                    j += 1
                cursor = cursor - j + 1
        elif(c[0]=='Z'):
            rollbacknum=deletestack.pop()
            status[rollbacknum]=True
    for a in status:
        if(a):
            answer+='O'
        else:
            answer+='X'
    return answer

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))