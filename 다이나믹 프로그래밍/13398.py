# 연속합 2 G5

import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [[0] * n for i in range(2)]
# dp[0]은 제거하지 않은 연속합
# dp[1]은 제거하는 연속합
dp[0][0] = arr[0]
dp[1][0] = -1 * sys.maxsize
for i in range(1, n):
    dp[0][i] = max(arr[i], dp[0][i - 1] + arr[i])
    # 숫자를 제거하는 연속합
    # 1. i번째 원소를 제거하는 경우 -> arr[i]를 더하지 않음
    # 2. i번째 이전에서 이미 특정 원소를 제거하였기 때문에 i번째 원소를 더하는 경우
    # -> 이미 특정 원소를 제거했기 때문에 arr[i]를 더함
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])

print(max(max(dp[0]), max(dp[1])))
