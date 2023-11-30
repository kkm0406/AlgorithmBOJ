# Maximum Subarray S4

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = x[0]
    for i in range(1, n):
        dp.append(max(dp[i - 1] + x[i], x[i]))
    print(max(dp))
