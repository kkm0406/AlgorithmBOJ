# 극장 좌석 S1
import sys

input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())

arr = []
for i in range(m):
    arr.append(int(input()))

dp = [1, 1, 2]
for i in range(3, n + 1):
    # 점화식: 자리를 옮기거나, 옮기지 않거나
    dp.append(dp[i - 2] + dp[i - 1])

result = 1
if m >= 1:
    tmp = 0  # 이전 vip 인덱스
    for i in range(m):
        # dp의 idx는 vip자리-1-tmp
        idx = arr[i] - 1 - tmp
        result *= dp[idx]
        tmp = arr[i]
    result *= dp[n - tmp]  # vip이후 자리 계산
else:
    result = dp[n]

print(result)
