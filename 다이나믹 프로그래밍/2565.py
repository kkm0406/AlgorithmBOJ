# 전깃줄 G5
import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

arr.sort(key=lambda x: x[0])  # 왼쪽 전봇대 기준 정렬
dp = [1 for i in range(n)]  # 오른쪽 전봇대의 LIS 저장
right = []

for i in arr:
    right.append(i[1])

for i in range(n):
    for j in range(i):
        # LIS
        if right[i] > right[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# 전체 전봇대 개수에서 LIS의 max를 뺌
print(n - max(dp))
