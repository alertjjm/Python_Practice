def isPalindrome(s):
    l=len(s)
    fst=False
    sst=False
    for i in range(l//2):
        if(s[i]!=s[len(s)-i-1]):
            for j in range(i, len(s) // 2):
                if s[j + 1] != s[len(s) - 1 - j]:
                    fst = True
            for j in range(i, len(s) // 2):
                if s[j] != s[len(s) - 1 - j - 1]:
                    sst = True
            if(fst and sst):
                return 2
            elif(fst or sst):
                return 1
    return 0
T=int(input())
result=[]
for i in range(T):
    sin=input()
    result.append(isPalindrome(sin))
for r in result:
    print(r)
