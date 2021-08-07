numbers=[]
#꺼져야하는게 켜지는경우 없고, 켜져야되는게 꺼지는 경우는 있음 - 켜진거 위주로 만들어보기
numbers.append({1,2,3,4,6,7,9,10,12,13,14,15})
numbers.append({3,6,9,12,15})
numbers.append({1,2,3,6,7,8,9,10,13,14,15})
numbers.append({1,2,3,6,7,8,9,12,13,14,15})
numbers.append({1,3,4,6,7,8,9,12,15})
numbers.append({1,2,3,4,7,8,9,12,13,14,15})
numbers.append({1,2,3,4,7,8,9,10,12,13,14,15})
numbers.append({1,2,3,6,9,12,15})
numbers.append({1,2,3,4,6,7,8,9,10,12,13,14,15})
numbers.append({1,2,3,4,6,7,8,9,12,13,14,15})
a=set()
N=int(input())
candidates=[set() for i in range(N)]
for _ in range(5):
    line=input()
    for i in range(N):
        start=4*i
        end=4*i+2
        for j in range(start,end+1):
            if(line[j]=='#'):
                candidates[i].add(_*3+1+j-start)
results=[[] for i in range(N)]
for j in range(len(candidates)):
    c=candidates[j]
    for i in range(len(numbers)):
        if(c==c.intersection(numbers[i])):
            results[j].append(i)
division=1
basemul=1
sum=0
status=True
for i in range(N):
    r = results[i]
    if(len(r)==0):
        status=False
        break
    division *= len(r)
if(status):
    for i in range(N):
        r=results[i]
        mul=pow(10,N-i-1)*(division/len(r))
        for a in r:
            sum+=a*mul
    print(sum/division)
else:
    print(-1)