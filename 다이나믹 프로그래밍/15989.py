# 1, 2, 3 더하기 4 S1

import sys

input = sys.stdin.readline
dp = [1] * 10001  # 1만 써서 합을 나타내는 방법

for i in range(2, 10001):
    dp[i] += dp[i - 2]  # 2가 추가되는 경우
for i in range(3, 10001):
    dp[i] += dp[i - 3]  # 3이 추가되는 경우

for i in range(int(input())):
    n = int(input())
    print(dp[n])
