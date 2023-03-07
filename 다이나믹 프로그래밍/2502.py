# 떡 먹는 호랑이 S1
import sys

input = sys.stdin.readline
d, k = map(int, input().split())

dp = [[0, 0] for i in range(d + 1)]
dp[1] = [1, 0]
dp[2] = [0, 1]
dp[3] = [1, 1]
for i in range(4, d + 1):
    dp[i] = [dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]]

x, y = dp[-1][0], dp[-1][1]
a = 1
while True:
    result = k - (x * a)
    if result % y == 0:
        print(a)
        print(result // y)
        break
    a += 1
