#마지막엔 무조건 1광년
#1 -> 1
#2 -> 1+1=2
#3 -> 1+1+1=3
#4 -> 1+2+1=3
#5 -> 1+2+1+1=4
#6 -> 1+2+2+1=4
#7 -> 1+2+2+1+1=5
#8 -> 1+2+2+2+1=5
#9 -> 1+2+3+2+1=5
#10 -> 1+2+3+2+1+1=6 // #9+1
#11 -> 1+2+3+2+2+1=6 //
#12 -> 1 2 3 3 2 1 =6
#13 -> 1 2 3 3 2 1 1=7
#14
# 1 2 3 3 4 4 5 5 5 6 6 6 7 7 7 7 8 8 8 8 9 9 9 9 9
# 1 2 3 4 5 6 7 8 9
# 1 2 4 6 9 12
# 1제곱, 1제곱+1, 2제곱, 2제곱+2, 3제곱, 3제곱+3
def calc(d):
    cnt=1
    i=1
    sum=0
    while True:
        sum=i*i
        if(sum>=d):
            return cnt
        cnt+=1
        sum+=i
        if(sum>=d):
            return cnt
        cnt+=1
        i+=1

T=int(input())
testcases=[]
for i in range(T):
    a,b=map(int, input().split(" "))
    testcases.append([a,b])
for i in testcases:
    distance=i[1]-i[0]
    print(calc(distance))