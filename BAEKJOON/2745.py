result=0
arr=list(map(int,input().split()))
for i in arr:
    result+=i**2
print(result%10)