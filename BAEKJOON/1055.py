S=input()
base=input()
T=int(input())
start,end=map(int,input().split())
change=base.replace("$",S)
st=False
for i in range(T-1):
    change=base.replace("$",change)
    if(len(change)>=end-start):
        if (len(change) < end):
            result = change[start - 1:end] + '-' * (end - len(change))
        print(result)
        print(change[start-1:end])
        st=True
        break

if(st==False):
    if(len(change)<end):
        result=change[start-1:end]+'-'*(end-len(change))
    print(result)