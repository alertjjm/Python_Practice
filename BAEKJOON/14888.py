from itertools import permutations
N=int(input())
numlist=list(map(int, input().split()))
plus,minus,multi,divide=map(int,input().split())
op=[]
for i in range(plus):
    op.append("+")
for i in range(minus):
    op.append("-")
for i in range(multi):
    op.append("*")
for i in range(divide):
    op.append("//")
opcases=list(set(permutations(op,len(op))))
def pack(nums,opcase):
    result=nums[0]
    for i in range(len(opcase)):
        if(opcase[i]=="//"):
            if(result<0):
                result=0
            else:
                result=result//nums[i+1]
        elif(opcase[i]=="*"):
            result = result*nums[i+1]
        elif(opcase[i]=="-"):
            result = result-nums[i+1]
        elif(opcase[i]=="+"):
            result = result+nums[i+1]
    return result
maxnum=-10000000000
minnum=10000000000
for case in opcases:
    result=pack(numlist,case)
    if(maxnum<result):
        maxnum=result
    if(minnum>result):
        minnum=result
print(maxnum)
print(minnum)