# 악수 S3

import sys

input = sys.stdin.readline

n = int(input())

dp = [0, 0, 2, 3, 5]

for i in range(5, n + 1):
    dp.append((dp[i - 2] + dp[i - 1]) % 10)

print(dp[n])
