import math

N, M, L = map(int, input().split())
start = 0
end = L
rests = [start] + list(map(int, input().split())) + [end]
rests.sort()
result = 10 ** 6
while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in range(N + 1):
        gap = rests[i + 1] - rests[i]
        cnt += (math.ceil(gap / mid) - 1)
    if (cnt <= M):
        end = mid - 1
        result = min(result, mid)
    else:
        start = mid + 1
print(result)
