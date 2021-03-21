t = int(input())
for i in range(t):
    n = int(input())
    sample = list(map(int, input().split()))
    m = max(sample) + 1
    if (sample[0] > sample[1]):
        print(-1)
    else:
        c = sample[1] - sample[0]
        m = -1
        for j in range(1, n - 1):
            if (m == -1 and sample[j] != sample[j - 1] + c):
                m = sample[j - 1] + c - sample[j]
            elif (sample[j] != sample[j - 1] + c):
                m2 = sample[j - 1] + c - sample[j]
                if (m != m):
                    print(-1)
                    break
        st=True
        for i in range(len(sample)):
            if(sample[i]!=sample[0]):
                st=False
                break
        if(st):
            print(0)
        elif(m==-1):
            print(-1)
        else:
            print(m, c)
