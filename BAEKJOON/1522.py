str = input()
aCnt = str.count('a')
bCnt = str.count('b')
L=len(str)
result=0
for i in range(L):
    count = aCnt
    start = i
    for j in range(i,i+L):
        end = j % L
        if (end < aCnt):
            if (str[end] == 'a'):
                count += 1
        else:
            result = max(count, result)
            if (str[start] == 'a'):
                count -= 1
            if (str[end] == 'a'):
                count += 1
            start = (start + 1) % L
print(aCnt-result)