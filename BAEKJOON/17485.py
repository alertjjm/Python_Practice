N, M = map(int, input().split())
spaces = []
for i in range(N):
    spaces.append([0] + list(map(int, input().split())))
dp = [[[10 ** 6] * (3) for i in range(M + 2)] for j in range(N)]
for i in range(M):
    dp[0][i + 1] = [spaces[0][i + 1]] * 3
for j in range(1, N):
    for i in range(1, M + 1):
        dp[j][i][0] = min(dp[j - 1][i + 1][1], dp[j - 1][i + 1][2]) + spaces[j][i]
        dp[j][i][1] = min(dp[j - 1][i][0], dp[j - 1][i][2]) + spaces[j][i]
        dp[j][i][2] = min(dp[j - 1][i - 1][0], dp[j - 1][i - 1][1]) + spaces[j][i]
candidates = dp[-1]
result = dp[-1][0][0]
for i in candidates:
    for j in i:
        result = min(j, result)
print(result)
