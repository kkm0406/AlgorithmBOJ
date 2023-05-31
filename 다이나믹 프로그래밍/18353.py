# 병사 배치하기 S2

import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
# 가장 긴 증가하는 부분 수열로 풀기 위해 reverse
arr.reverse()
dp = [1] * n

for i in range(n):
    # i-1 인덱스까지
    for j in range(i):
        # 현재 i번째 값이 j번째 값보다 크다면
        if arr[i] > arr[j]:
            # j번째 값을 추가할 경우, 그냥 진행할 경우
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
