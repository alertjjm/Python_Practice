from collections import deque
def solution(n, k, cmd):
    freelist=deque()
    linkedlist=[[n-1,0,1]]
    for i in range(1,n-1):
        linkedlist.append([i-1,i,i+1])
    linkedlist.append([n-2,n-1,0])
    cursor=k
    end=n-1
    for c in cmd:
        if (c[0] == 'D'):
            temp = c.split()
            num = int(temp[1])
            for i in range(num):
                cursor=linkedlist[cursor][2]
        elif (c[0] == 'U'):
            temp = c.split()
            num = int(temp[1])
            for i in range(num):
                cursor=linkedlist[cursor][0]
        elif (c[0] == 'C'):
            linkedlist[linkedlist[cursor][0]][2]=linkedlist[cursor][2]
            linkedlist[linkedlist[cursor][2]][0] = linkedlist[cursor][0]
            freelist.append(cursor)
            if(cursor==end):
                cursor=linkedlist[cursor][0]
                end=cursor
            else:
                cursor=linkedlist[cursor][2]
        elif (c[0] == 'Z'):
            rollback=freelist.pop()
            left=linkedlist[cursor][0]
            right=linkedlist[cursor][2]
            while(left in freelist):
                left=linkedlist[left][0]
            while(right in freelist):
                right=linkedlist[right][2]
                linkedlist[left][2]=rollback
                linkedlist[rollback][0]=left
                linkedlist[right][0]=rollback
                linkedlist[rollback][2]=right
    answer=['O' for i in range(n)]
    while freelist:
        a=freelist.popleft()
        answer[a]='X'
    return ''.join(answer)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))