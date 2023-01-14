# 가장 큰 증가 부분 수열 S2
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [i for i in arr]  # 현재 위치에서 부분 증가수열의 총합

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:  # 현재 원소값이 이전의 원소값보다 크면
            dp[i] = max(dp[i], dp[j] + arr[i])  # 이전 위치의 lis 총합+현위치 원소값과 비교

print(max(dp))
