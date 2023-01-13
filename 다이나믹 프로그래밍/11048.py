# 이동하기 S2
import sys

n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * (m + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = maze[i - 1][j - 1] + max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])
