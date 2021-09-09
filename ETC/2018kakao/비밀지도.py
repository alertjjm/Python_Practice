def solution(n, arr1, arr2):
    secretMap=[[' ']*n for _ in range(n)]
    for a1 in range(len(arr1)):
        a=arr1[a1]
        for i in range(n):
            left=a%2
            a=a//2
            if(left==1):
                secretMap[a1][n-i-1]='#'
    for a2 in range(len(arr2)):
        a=arr2[a2]
        for i in range(n):
            left=a%2
            a=a//2
            if(left==1):
                secretMap[a2][n-i-1]='#'
    for i in range(len(secretMap)):
        secretMap[i]=''.join(secretMap[i])
    return secretMap

print(solution(5, [9, 20, 28, 18, 11], 	[30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))