# 안녕 S2
import sys

input = sys.stdin.readline
n = int(input())
L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))
dp = [[0] * 101 for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, 101):  # 체력이 1~100인 경우
        if L[i] <= j:  # 현재 체력으로 현재 사람을 만날 수 있는 경우
            # i-1번째 dp에서 L[i]만큼 체력을 빠졌을 때 J[i]만큼 기쁨을 선택할 경우와 비교
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - L[i]] + J[i])
        else:  # 사람을 만나지 않음
            dp[i][j] = dp[i - 1][j]

print(dp[n][99])
