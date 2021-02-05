i=0
order=[]
def hanoi(n,fr, by, to):
    global i
    if n==1:
        order.append((fr,to))
        i+=1
    else:
        hanoi(n - 1, fr, to, by)
        order.append((fr,to))
        i+=1
        hanoi(n-1,by,fr, to)

num=int(input())
hanoi(num,1,2,3)
print(i)
for i in order:
    print(i[0],i[1])