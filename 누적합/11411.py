# 합 구하기 S3

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0]

# 누적합 계산
for i in range(n):
    dp.append(dp[-1] + arr[i])

for _ in range(int(input())):
    i, j = map(int, input().split())
    # 주어진 범위 내 합 계산
    print(dp[j] - dp[i - 1])
