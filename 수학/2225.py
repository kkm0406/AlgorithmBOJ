# 합분해 G5
import sys

n, k = map(int, sys.stdin.readline().split())

# 행: 0 ~ n까지의 수, 열: 0 ~ k개의 수로 만들 수 있는 방법
dp = [[0] * (k + 1) for i in range(n + 1)]

# 1개의 수로 만들 방법은 1가지
for i in range(1, n + 1):
    dp[i][1] = 1

# 1은 1+0, 1+0+0 이런 경우 밖에 없음
for i in range(1, k + 1):
    dp[1][i] = i

for i in range(2, n + 1):
    for j in range(2, k + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000

print(dp[n][k])
