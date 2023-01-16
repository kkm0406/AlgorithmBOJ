# 1, 2, 3 더하기 3 S2
import sys

t = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for i in range(t)]
dp = [0] * (max(arr) + 1)  # 정수 n의 최대값+1만큼 배열 미리 선언
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, max(arr) + 1):
    # dp[5] = dp[4]+dp[3]+dp[2] = 7+4+2
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

for i in arr:
    print(dp[i])
