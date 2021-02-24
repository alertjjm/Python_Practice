N=int(input())
drinks=list(map(int, input().split(" ")))
drinks.sort()
for i in range(len(drinks)-1):
    drinks[len(drinks)-1]+=drinks[i]/2
print(drinks[len(drinks)-1])
