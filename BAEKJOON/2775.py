t = int(input())
result=[]
for _ in range(t):
    floor = int(input())
    num = int(input())
    f0 = [x for x in range(1, num+1)]
    for k in range(floor):
        for i in range(1, num):
            f0[i] += f0[i-1]
    result.append(f0[-1])
for r in result:
    print(r)
